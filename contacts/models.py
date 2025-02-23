from django.db import models


class Contact(models.Model):
    """
    Represents an individual contact.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
