from django.contrib import admin
from django.conf.locale.pt_BR import formats as portuguese
from django.conf.locale.en import formats as english
from rangefilter.filters import DateRangeFilter
from .models import FileModel

portuguese.DATE_FORMAT = 'd/m/Y'
english.DATE_FORMAT = 'd/m/Y'


@admin.register(FileModel)
class FileRegister(admin.ModelAdmin):
    autocomplete_fields = ['user']
    list_display = ['id', 'file_name', 'created_at']
    list_display_links = ['id', 'file_name']
    list_filter = [
        'user',
        ('created_at', DateRangeFilter),
    ]
    list_per_page = 25
    ordering = ['id']
    search_fields = ['id', 'file__name']

    def file_name(self, obj):
        return obj.file.name
    file_name.short_description = 'File'
