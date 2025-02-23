from contacts.forms import ContactForm
from django.views.generic.edit import FormView
from loguru import logger


class ContactFormView(FormView):
    template_name = "add.html"
    form_class = ContactForm
    success_url = "/thanks/"

    def form_valid(self, form):
        contact = form.save()
        logger.info(f"Contact {contact} created at")
        return super().form_valid(form)