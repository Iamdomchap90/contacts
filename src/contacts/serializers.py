from rest_framework import serializers

from contacts.models import Contact


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = [
            "first_name",
            "last_name",
            "email",
            "address",
            "phone_number",
            "company",
            "created_at",
            "updated_at",
        ]
