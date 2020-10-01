from django.contrib import admin
from userAccount.models import Post,Profile,Like,Following
# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Like)
admin.site.register(Following)
