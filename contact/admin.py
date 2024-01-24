from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [
        "contact_purpose",
        "email",
        "name",
        "phone",
        "message",
        "date_submitted",
    ]
    list_filter = ["name", "date_submitted"]

 