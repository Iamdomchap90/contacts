from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Contact

@receiver(post_save, sender=Contact)
def contact_saved(sender, instance, created, **kwargs):
    if created:
        print(f"Contact {instance.name} has been saved.")  # You can remove this line later
