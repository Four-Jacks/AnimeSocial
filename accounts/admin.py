from django.contrib import admin
from accounts.models import UserProfile
from accounts.models import UserAnime
from accounts.models import UserFriend

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserAnime)
admin.site.register(UserFriend)