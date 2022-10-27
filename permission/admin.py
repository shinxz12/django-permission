from django.contrib import admin
from .models import *
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass

class BloggerAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class PostManagerAdmin(admin.ModelAdmin):
    pass

class ContentTypeAdmin(admin.ModelAdmin):
    pass

class PermissionAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(Blogger, BloggerAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Permission, PermissionAdmin)
admin.site.register(PostManager, PostManagerAdmin)
admin.site.register(ContentType, ContentTypeAdmin)
