from django.contrib import admin
from .models import BlogPost, Comment, ContactFormMessage
# Register your models here.



@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    # Add more options as needed

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'content', 'created_at')
    # Add more options as needed

@admin.register(ContactFormMessage)
class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    # Add more options as needed
