from django.db import models


class SiteProfile(models.Model):
    """Editable content for the public hostel page; one singleton record (pk=1)."""

    id = models.PositiveSmallIntegerField(primary_key=True, default=1, editable=False)
    website_name = models.CharField(max_length=160, default="JANNA GENTS HOSTEL")
    subtitle = models.CharField(max_length=220, default="Single / 2 / 3 / 4 / 6 Sharing Rooms")
    about_text = models.TextField(default="Homely Food | Free Unlimited Wi-Fi | Parking Facilities | 24/7 CCTV Surveillance | Food & Accommodation")
    phone = models.CharField(max_length=40, default="8086311143")
    email = models.EmailField(default="jannahostel@gmail.com")
    address = models.TextField(default="St.Francis church road , kaloor- kathrukadavu, 682017")
    review_url = models.URLField(max_length=500, default="https://search.google.com/local/writereview?placeid=ChIJGyK5Jg0NCDsROxzElXIbqWU")
    map_url = models.URLField(max_length=500, default="https://maps.app.goo.gl/QqN6tyiYzDaZW7Zm8")
    description_title = models.CharField(max_length=220, default="🏠 Comfortable Food & Accommodation")
    description_text = models.TextField(default="JANNA GENTS HOSTEL provides food and accommodation with a comfortable hostel environment for students and working individuals.")

    logo_image = models.FileField(upload_to="site/", blank=True)
    cover_image = models.FileField(upload_to="site/", blank=True)
    gallery_1 = models.FileField(upload_to="site/", blank=True)
    gallery_2 = models.FileField(upload_to="site/", blank=True)
    gallery_3 = models.FileField(upload_to="site/", blank=True)
    gallery_4 = models.FileField(upload_to="site/", blank=True)
    gallery_5 = models.FileField(upload_to="site/", blank=True)

    room_single_name = models.CharField(max_length=100, default="Single Sharing")
    room_single_price = models.CharField(max_length=60, default="₹8,000")
    room_single_description = models.CharField(max_length=220, default="Comfortable private room")
    room_single_image = models.FileField(upload_to="site/", blank=True)
    room_2_name = models.CharField(max_length=100, default="2 Sharing")
    room_2_price = models.CharField(max_length=60, default="₹7,000")
    room_2_description = models.CharField(max_length=220, default="Comfortable shared accommodation")
    room_2_image = models.FileField(upload_to="site/", blank=True)
    room_3_name = models.CharField(max_length=100, default="3 Sharing")
    room_3_price = models.CharField(max_length=60, default="₹6,500")
    room_3_description = models.CharField(max_length=220, default="Spacious shared accommodation")
    room_3_image = models.FileField(upload_to="site/", blank=True)
    room_4_name = models.CharField(max_length=100, default="4 Sharing")
    room_4_price = models.CharField(max_length=60, default="₹6,000")
    room_4_description = models.CharField(max_length=220, default="Spacious shared room")
    room_4_image = models.FileField(upload_to="site/", blank=True)
    room_6_name = models.CharField(max_length=100, default="6 Sharing")
    room_6_price = models.CharField(max_length=60, default="₹5,500")
    room_6_description = models.CharField(max_length=220, default="Budget-friendly shared room")
    room_6_image = models.FileField(upload_to="site/", blank=True)

    bank_holder = models.CharField(max_length=160, default="sainul habeeb")
    bank_account = models.CharField(max_length=80, default="4323002100006883")
    bank_ifsc = models.CharField(max_length=32, default="PUNB0432300")
    bank_name = models.CharField(max_length=160, default="Punjab National Bank")
    bank_branch = models.CharField(max_length=160, default="NILAMBUR")
    upi_id = models.CharField(max_length=160, default="sainul.abid69-19@okhdfcbank")
    upi_mobile = models.CharField(max_length=40, default="9562020100")

    social_facebook = models.URLField(max_length=500, blank=True, default="")
    social_instagram = models.URLField(max_length=500, default="https://www.instagram.com/janna_gents_hostel")
    social_linkedin = models.URLField(max_length=500, blank=True, default="")
    social_x = models.URLField(max_length=500, blank=True, default="")
    social_telegram = models.URLField(max_length=500, blank=True, default="https://t.me/")

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site content"
        verbose_name_plural = "Site content"

    def __str__(self):
        return self.website_name

    @property
    def phone_digits(self):
        return "".join(character for character in self.phone if character.isdigit())

    @property
    def whatsapp_number(self):
        digits = self.phone_digits
        return digits if digits.startswith("91") else f"91{digits}"
