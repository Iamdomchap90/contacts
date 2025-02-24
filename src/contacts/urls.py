from django.urls import path
from contacts.views import (
    ContactFormView,
    ContactListView,
    ContactUpdateView,
    delete_contact,
)


app_name = "contacts"


urlpatterns = [
    path("", ContactListView.as_view(), name="list"),
    path("add/", ContactFormView.as_view(), name="add"),
    path("update/<int:pk>/", ContactUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", delete_contact, name="delete"),
]
