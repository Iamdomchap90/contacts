from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from contacts.views import ContactViewSet

router = DefaultRouter()
router.register(r"contacts", ContactViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("src.contacts.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
]
