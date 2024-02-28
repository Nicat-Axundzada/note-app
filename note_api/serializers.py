from rest_framework.serializers import ModelSerializer
from note_api.models import Note


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created', 'updated']
