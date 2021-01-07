from django.urls import path, include

from . import views

app_name = "website"

urlpatterns = [
    path("", views.landing_view, name="landing"),
    path("info/", views.info_view, name="info"),
    path("edit/", views.info_create, name="edit"),
    path("delete/<int:my_id>", views.delete_picture, name="pic_view"),
    path("upload/", views.upload, name="upload")
]
