from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views


urlpatterns = (
    path("sd-accesss/", views.SDAccessListView.as_view(), name="sdaccess_list"),
    path("sd-accesss/add/", views.SDAccessEditView.as_view(), name="sdaccess_add"),
    path("sd-accesss/<int:pk>/", views.SDAccessView.as_view(), name="sdaccess"),
    path("sd-accesss/<int:pk>/edit/", views.SDAccessEditView.as_view(), name="sdaccess_edit"),
    path("sd-accesss/<int:pk>/delete/", views.SDAccessDeleteView.as_view(), name="sdaccess_delete"),
    path(
        "sd-accesss/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="sdaccess_changelog",
        kwargs={"model": models.SDAccess},
    ),
)
