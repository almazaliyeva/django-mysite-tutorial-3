from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),  # polls tətbiqini bura əlavə edirik
    path("admin/", admin.site.urls),
]
