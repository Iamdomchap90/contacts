from django.contrib import admin

from contacts.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin class for the Contact model.
    """
    list_display = (
        'first_name', 'last_name', 'email', 'company', 'address', 'phone_number',
    )


