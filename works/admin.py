from django.contrib import admin
from works.models import Work, WorkImage

# Inline-модель для загрузки нескольких изображений
class WorkImageInline(admin.TabularInline):
    model = WorkImage
    extra = 5  # Можно загружать до 3 изображений за раз

@admin.register(Work)
class WorksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish')
    list_filter = ('title', 'author', 'publish')
    search_fields = ('title', 'author__username', 'publish')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [WorkImageInline]  # Добавляем изображения внутрь Work
