from django.contrib import admin

from .models import Link, SiteProfile


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
	list_display = ("title", "tab", "url", "sort_order", "is_active", "updated_at")
	list_filter = ("tab", "is_active")
	search_fields = ("title", "tab", "url", "description")
	list_editable = ("tab", "sort_order", "is_active")
	ordering = ("sort_order", "id")
	fields = ("title", "url", "description", "tab", "sort_order", "is_active")


@admin.register(SiteProfile)
class SiteProfileAdmin(admin.ModelAdmin):
	list_display = ("name", "tagline", "heart_count", "updated_at")
	fields = ("name", "tagline", "avatar_url", "heart_count")

	def has_add_permission(self, request):
		return not SiteProfile.objects.exists()

	def has_delete_permission(self, request, obj=None):
		return False
