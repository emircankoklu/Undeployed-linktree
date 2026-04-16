from django.db import models


class Link(models.Model):
	title = models.CharField(max_length=120)
	url = models.URLField(max_length=500)
	description = models.CharField(max_length=180, blank=True)
	image_url = models.URLField(max_length=500, blank=True)
	tab = models.CharField(max_length=60, default="Main")
	sort_order = models.PositiveIntegerField(default=0)
	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["sort_order", "id"]

	def __str__(self):
		return self.title


class SiteProfile(models.Model):
	name = models.CharField(max_length=120, blank=True, default="")
	tagline = models.CharField(max_length=180, blank=True, default="")
	avatar_url = models.URLField(max_length=500, blank=True)
	heart_count = models.PositiveIntegerField(default=0)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Site profile"
		verbose_name_plural = "Site profile"

	def __str__(self):
		return self.name or "Site profile"
