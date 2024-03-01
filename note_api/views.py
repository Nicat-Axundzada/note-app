from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from note_api.models import Note
from note_api.serializers import NoteSerializer
from rest_framework import status
from django.http import Http404

# Create your views here.


@api_view(['GET',])
def get_routes(request):

    routes = [
        {
            'endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
        },
        {
            'endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
        },
        {
            'endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
        },
        {
            'endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
        },
    ]

    return Response(routes)


class NoteAPI(APIView):
    def get(self, request):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)

        return Response(serializer.data)


class NoteDetailAPI(APIView):
    def get_note(self, id):
        try:
            return Note.objects.get(pk=id)
        except Note.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        note = self.get_note(pk)
        serializer = NoteSerializer(note)
        return Response(serializer.data)
