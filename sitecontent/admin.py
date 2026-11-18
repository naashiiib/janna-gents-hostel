from django.contrib import admin
from .models import SiteProfile


@admin.register(SiteProfile)
class SiteProfileAdmin(admin.ModelAdmin):
    list_display = ("website_name", "updated_at")
    fieldsets = (
        ("Website identity", {"fields": ("website_name", "subtitle", "about_text", "description_title", "description_text")}),
        ("Contact and location", {"fields": ("phone", "email", "address", "review_url", "map_url")}),
        ("Images", {"fields": ("logo_image", "cover_image", ("gallery_1", "gallery_2", "gallery_3"), ("gallery_4", "gallery_5"))}),
        ("Room names, descriptions, prices and photos", {"fields": (
            ("room_single_name", "room_single_price"), "room_single_description", "room_single_image",
            ("room_2_name", "room_2_price"), "room_2_description", "room_2_image",
            ("room_3_name", "room_3_price"), "room_3_description", "room_3_image",
            ("room_4_name", "room_4_price"), "room_4_description", "room_4_image",
            ("room_6_name", "room_6_price"), "room_6_description", "room_6_image",
        )}),
        ("Payment details", {"fields": ("bank_holder", "bank_account", "bank_ifsc", "bank_name", "bank_branch", "upi_id", "upi_mobile")}),
        ("Social links", {"fields": ("social_facebook", "social_instagram", "social_linkedin", "social_x", "social_telegram")}),
    )

    def has_add_permission(self, request):
        return not SiteProfile.objects.filter(pk=1).exists()

    def has_delete_permission(self, request, obj=None):
        return False
