from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class FileModel(models.Model):
    '''File Model'''
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateField(auto_now=True, verbose_name=_('Updated at'))
    file = models.FileField(
        upload_to='uploads/omnistack6/%Y/%m/%d/',
        verbose_name=_('File'),
    )
    extension = models.CharField(max_length=10, blank=True, verbose_name=_('File extension'))
    user = models.ForeignKey(User, related_name='user_files', on_delete=models.CASCADE, verbose_name=_('User'))

    class Meta:
        verbose_name = _('File')
        verbose_name_plural = _('Files')

    def __str__(self):
        return f'{ self.file.name }'

    def delete(self, using=None, keep_parents=False):
        '''Exclui arquivo'''
        self.file.storage.delete(self.file.name)
        super().delete()
