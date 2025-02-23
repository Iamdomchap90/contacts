from django import forms

from contacts.models import Contact


class ContactForm(forms.ModelForm):
    """
    Represents contact form instance that produces an instance of a
    Contact model.
    """

    class Meta:
        model = Contact
        fields = [
            "first_name",
            "last_name",
            "address",
            "phone_number",
            "email",
            "company",
        ]

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
