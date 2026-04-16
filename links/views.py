from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST

from .models import Link, SiteProfile


@ensure_csrf_cookie
def linktree_home(request):
	selected_tab = request.GET.get("tab", "All")
	all_active_links = Link.objects.filter(is_active=True).order_by("sort_order", "id")
	tabs = ["All"]
	tabs.extend(list(all_active_links.values_list("tab", flat=True).distinct().order_by("tab")))

	if selected_tab != "All":
		links = all_active_links.filter(tab=selected_tab)
		if selected_tab not in tabs:
			selected_tab = "All"
			links = all_active_links
	else:
		links = all_active_links

	profile = SiteProfile.objects.first()
	if profile is None:
		profile = SiteProfile.objects.create()

	# Keep hero identity fixed as requested.
	profile_name = "More & More"
	profile_tagline = "what else does not fit in this board?"
	profile_avatar_url = profile.avatar_url
	heart_count = profile.heart_count
	context = {
		"profile_name": profile_name,
		"profile_tagline": profile_tagline,
		"profile_avatar_url": profile_avatar_url,
		"heart_count": heart_count,
		"tabs": tabs,
		"selected_tab": selected_tab,
		"links": links,
	}
	return render(request, "links/linktree_home.html", context)


@require_POST
def add_heart(request):
	profile = SiteProfile.objects.first()
	if profile is None:
		profile = SiteProfile.objects.create()
	SiteProfile.objects.filter(pk=profile.pk).update(heart_count=F("heart_count") + 1)
	profile.refresh_from_db(fields=["heart_count"])
	return JsonResponse({"heart_count": profile.heart_count})
