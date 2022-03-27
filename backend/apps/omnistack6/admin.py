from django.contrib import admin
from django.conf.locale.pt_BR import formats as portuguese
from django.conf.locale.en import formats as english
from rangefilter.filters import DateRangeFilter
from .models import BoxModel, FileModel, NewFileModel

portuguese.DATE_FORMAT = 'd/m/Y'
english.DATE_FORMAT = 'd/m/Y'


@admin.register(BoxModel)
class BoxRegister(admin.ModelAdmin):
    list_display = ['id', 'name', 'user', 'created_at']
    list_display_links = ['id', 'name']
    list_filter = [
        'user',
        ('created_at', DateRangeFilter),
    ]
    list_per_page = 25
    ordering = ['id']
    search_fields = ['id', 'name', 'user']


@admin.register(FileModel)
class FileRegister(admin.ModelAdmin):
    autocomplete_fields = ['box']
    list_display = ['id', 'file_name', 'created_at']
    list_display_links = ['id', 'file_name']
    list_filter = [
        'box',
        'box__user',
        ('created_at', DateRangeFilter),
    ]
    list_per_page = 25
    ordering = ['id']
    search_fields = ['id', 'box', 'file__name']

    def file_name(self, obj):
        return obj.file.name
    file_name.short_description = 'File'



@admin.register(NewFileModel)
class NewFileRegister(admin.ModelAdmin):
    list_display = ['id', 'file_name', 'created_at']

    def file_name(self, obj):
        return obj.file.name
    file_name.short_description = 'File'
