from django.contrib import admin
from .models import Post, Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category', 'created_at')
    list_display = ('title', 'slug', 'category', 'created_at', 'status')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)