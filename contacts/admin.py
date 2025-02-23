from django.contrib import admin


class ContactAdmin(admin.ModelAdmin):
    """
    Admin class for the Contact model.
    """
    list_display = ('first_name', 'last_name', 'email', 'company')


