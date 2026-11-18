from django.shortcuts import render
from .models import SiteProfile


def home(request):
    profile, _ = SiteProfile.objects.get_or_create(pk=1)
    site_data = {
        "name": profile.website_name,
        "phone": profile.phone_digits,
        "whatsapp": profile.whatsapp_number,
        "email": profile.email,
        "address": profile.address,
        "about": profile.about_text,
        "map_url": profile.map_url,
        "upi_id": profile.upi_id,
    }
    return render(request, "sitecontent/home.html", {"profile": profile, "site_data": site_data})
