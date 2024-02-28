from django.urls import path
from note_api.views import get_routes

urlpatterns = [
    path('', get_routes),
]
