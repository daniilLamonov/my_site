from django.contrib import admin

from works.models import Work


# Register your models here.
@admin.register(Work)
class WorksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish')
    list_filter = ('title', 'author', 'publish')
    search_fields = ('title', 'author', 'publish')
    prepopulated_fields = {'slug': ('title',)}