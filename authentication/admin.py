from django.contrib import admin

from django.contrib import admin
from .models import User, TitleImage, Administrator

# class MessageAdmin(admin.ModelAdmin):
#     print("hi")
#     #     control how out meetups should be presented in the admin area (columns)
#     # list_display = ('first_name', 'email')
#     # list_filter = ('email', 'last_name')
#
# class FriendsAdmin(admin.ModelAdmin):
#     print("hi")
#     #     control how out meetups should be presented in the admin area (columns)
#     # list_display = ('first_name', 'email')
#     # list_filter = ('email', 'last_name')

admin.site.register(User)
admin.site.register(Administrator)

admin.site.register(TitleImage)

