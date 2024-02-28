from django.urls import path
from note_api.views import get_routes, NoteAPI, NoteDetailAPI

urlpatterns = [
    path('', get_routes),
    path('notes/', NoteAPI.as_view()),
    path('notes/<int:pk>/', NoteDetailAPI.as_view()),
]
