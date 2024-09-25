from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contact, base


app_name = CatalogConfig.name
urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contact, name="contact"),
    path("base/", base, name="base"),
]
