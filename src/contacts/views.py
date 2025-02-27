from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.generic.edit import FormView
from loguru import logger
from rest_framework import viewsets

from contacts.forms import ContactForm
from contacts.models import Contact
from contacts.serializers import ContactSerializer


class ContactListView(ListView):
    model = Contact
    template_name = "list.html"
    context_object_name = "contacts"
    paginate_by = 20

    def get_queryset(self):
        return Contact.objects.all()


class ContactUpdateView(FormView):
    template_name = "add_or_update.html"  # Reusing the same template as add
    form_class = ContactForm
    success_url = reverse_lazy("contacts:list")

    def get_object(self, queryset=None):
        contact_id = self.kwargs.get("pk")
        return Contact.objects.get(id=contact_id)

    def get_initial(self):
        contact = self.get_object()  # Get the contact object
        return {
            "first_name": contact.first_name,
            "last_name": contact.last_name,
            "email": contact.email,
            "phone_number": contact.phone_number,
            "company": contact.company,
            "address": contact.address,
        }

    def form_valid(self, form):
        contact = self.get_object()
        form = ContactForm(form.data, instance=contact)

        if form.is_valid():
            contact = form.save()
            messages.success(
                self.request,
                f"Contact {contact} has been successfully updated.",
            )
            logger.info(f"Contact {contact} updated.")
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class ContactFormView(CreateView):
    template_name = "add_or_update.html"
    form_class = ContactForm
    success_url = reverse_lazy("contacts:list")

    def form_valid(self, form):
        contact = form.save()
        logger.info(f"Contact {contact} created at")
        messages.success(
            self.request, "Your contact has been successfully created."
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"add": True})
        return context


class HTTPResponseHXRedirect(HttpResponseRedirect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self["HX-Redirect"] = self["Location"]

    status_code = 200


def delete_contact(request, pk):
    if request.method == "POST":
        contact = get_object_or_404(Contact, pk=pk)
        contact.delete()
        messages.success(
            request,
            f"Contact {contact.first_name} has been successfully deleted.",
        )

    return HTTPResponseHXRedirect(redirect_to=reverse_lazy("contacts:list"))


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
