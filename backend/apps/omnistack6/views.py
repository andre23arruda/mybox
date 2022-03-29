from django.contrib.auth.models import AnonymousUser, User
from django.http import HttpResponse
from rest_framework import authentication, generics, viewsets
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from rest_framework.exceptions import ValidationError

from .models import FileModel
from .serializers import FileSerializer, UserSerializer


def file_extension(file_name: str):
    '''Retorna extensão do arquivo'''
    return '.' + file_name.split('.')[-1]


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
    authentication_classes = []


class FilesViewSet(viewsets.ModelViewSet):
    '''API endpoint that allows Files to be viewed or edited.'''
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
        JSONWebTokenAuthentication,
    ]
    http_method_names = ['get', 'post', 'delete']
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    serializer_class = FileSerializer

    def get_queryset(self):
        user = self.request.user
        if user:
            return FileModel.objects.filter(user=user)
        raise ValidationError(detail={'message': 'You must be logged!!'})

    def create(self, request, *args, **kwargs):
        pass

    @action(detail=False, methods=['post'])
    def upload(self, request, *args, **kwargs):
        '''Upload files'''
        user = request.user
        data = request.data
        print(data)
        files_data = data.getlist('files')
        for file in files_data:
            FileModel.objects.create(
                file=file,
                extension=file_extension(file.name),
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
