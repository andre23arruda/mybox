from django.contrib.auth.models import AnonymousUser, User
from django.http import HttpResponse
from rest_framework import generics, status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


from .models import BoxModel, FileModel, NewFileModel
from .serializers import BoxSerializer, FileSerializer, UserSerializer


def get_user(user, token):
    if not isinstance(user, AnonymousUser):
        return user
    else:
        token = Token.objects.filter(pk=token)
        return token[0].user


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
    authentication_classes = []


class BoxesViewSet(viewsets.ModelViewSet):
    '''API endpoint that allows Box to be viewed or edited.'''
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    queryset = BoxModel.objects.all()
    serializer_class = BoxSerializer

    @action(detail=True, methods=['post'])
    def upload(self, request, *args, **kwargs):
        '''Upload files'''
        instance = self.get_object()
        data = request.data
        files_data = data.getlist('files')
        for file in files_data:
            FileModel.objects.create(
                file=file,
                box=instance
            )
        return Response({'message': 'Files uploaded!!'})


class FilesViewSet(viewsets.ModelViewSet):
    '''API endpoint that allows Files to be viewed or edited.'''
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    queryset = FileModel.objects.all()
    serializer_class = FileSerializer

    @action(detail=True, methods=['get'])
    def download(self, request, *args, **kwargs):
        '''Download file'''
        instance = self.get_object()
        filename = instance.file.name.split('/')[-1]
        response = HttpResponse(instance.file, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        return response


class NewFilesViewSet(viewsets.ModelViewSet):
    '''API endpoint that allows Files to be viewed or edited.'''
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    serializer_class = FileSerializer

    def get_queryset(self):
        return NewFileModel.objects.all()
        # token = self.request.headers.get('Authorization', None)
        # user = get_user(self.request.user, token)
        # return NewFileModel.objects.filter(user=user)

    @action(detail=False, methods=['post'])
    def upload(self, request, *args, **kwargs):
        '''Upload files'''
        user = User.objects.get(pk=1)
        data = request.data
        print(data)
        files_data = data.getlist('files')
        for file in files_data:
            NewFileModel.objects.create(
                file=file,
                user=user
            )
        return Response({'message': 'Files uploaded!!'})

    @action(detail=True, methods=['get'])
    def download(self, request, *args, **kwargs):
        '''Download file'''
        instance = self.get_object()
        filename = instance.file.name.split('/')[-1]
        response = HttpResponse(instance.file, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        return response


# class OauthPostsViewSet(viewsets.ModelViewSet):
#     '''API endpoint that allows Post to be viewed or edited.'''
#     serializer_class = PostSerializer
#     http_method_names = ['get', 'post', 'patch']
#     parser_classes = [MultiPartParser, FormParser, JSONParser]

#     def get_queryset(self, *args, **kwargs):
#         queryset = []
#         token = self.request.headers.get('Authorization')
#         if token:
#             queryset = PostModel.objects.all().order_by('-created_at')
#         return queryset

#     def get_serializer_context(self):
#         context = super(OauthPostsViewSet, self).get_serializer_context()
#         context.update({'request': self.request})
#         return context

#     @action(detail=True, methods=['get'])
#     def like(self, request, *args, **kwargs):
#         '''Like em Post'''
#         token = request.headers.get('Authorization')
#         instance = self.get_object()
#         liked = instance.add_like(token, request.user)
#         return Response({'liked': liked})


# class BoxesViewSet(viewsets.ModelViewSet):
#     '''API endpoint that allows Box to be viewed or edited.'''
#     authentication_classes = [JSONWebTokenAuthentication]
#     http_method_names = ['get', 'post', 'patch']
#     parser_classes = [MultiPartParser, FormParser, JSONParser]
#     queryset = PostModel.objects.all().order_by('-created_at')
#     serializer_class = PostSerializer

#     def get_serializer_context(self):
#         context = super(PostsViewSet, self).get_serializer_context()
#         context.update({'request': self.request})
#         return context

#     @action(detail=True, methods=['get'])
#     def like(self, request, *args, **kwargs):
#         '''Like em Post'''
#         token = request.headers.get('Authorization')
#         instance = self.get_object()
#         liked = instance.add_like(token, request.user)
#         return Response({'liked': liked})
