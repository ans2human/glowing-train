from django.contrib import admin

from .models import Profile, FamilyMember, Timeline

admin.site.register(Profile)
admin.site.register(FamilyMember)
admin.site.register(Timeline)