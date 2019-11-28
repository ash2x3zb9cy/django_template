from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import SiteUser

# for now, better to just edit Django user using our inline.
# @admin.register(SiteUser)
class SiteUserAdmin(admin.ModelAdmin):
	search_fields = [
		'equiv_user__username',
		'equiv_user__first_name',
		'equiv_user__last_name',
		'equiv_user__email',
	]

	# TODO: implement get_absolute_url() on SiteUser
	# view_on_site = True

class SiteUserInline(admin.StackedInline):
	model = SiteUser

class UserAdmin(BaseUserAdmin):
	inlines = (SiteUserInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
