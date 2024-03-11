from django.contrib import admin
from .models import BlogPost, Comment, ContactFormMessage
# Register your models here.



@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'image_preview']
    search_fields = ['title', 'content']
    list_filter = ['created_at']


    def image_preview(self, obj):
        return obj.image.url if obj.image else None

    image_preview.short_description = 'Image'



@admin.register(ContactFormMessage)
class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    # Add more options as needed
