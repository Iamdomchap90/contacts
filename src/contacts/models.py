from django.db import models


class Contact(models.Model):
    """
    Represents an individual contact.
    """

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField(blank=True, default="")
    phone_number = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def truncated_address(self):
        if self.address:
            if len(self.address) > 40:
                return f"{self.address[:40]}..."
            return self.address
        return "No address given"
