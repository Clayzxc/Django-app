from django.contrib import admin
from .models import Member, Profile


class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)

admin.site.register(Member, MemberAdmin)

admin.site.register(Profile)
