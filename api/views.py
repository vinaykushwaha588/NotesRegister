from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import NotesSerializers
from rest_framework import status
from api.models import Notes
from django.http import Http404
# Create your views here.

class CreateNotesView(APIView):

    def post(self, request):
        try:
            serializer = NotesSerializers(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'success':True, 'message':"Notes Created Successfully."}, status=status.HTTP_201_CREATED)
            return Response({'success':False, 'message': serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({'error': error.args[0]})
        

class RetrieveUpdateNotesView(APIView):

    def get_object(self, pk):
        try:
            return Notes.objects.get(id=pk)
        except Notes.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        notes = self.get_object(pk)
        serializer = NotesSerializers(notes)
        return Response({'success': True, 'data':serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        notes = self.get_object(pk)
        serializer = NotesSerializers(notes, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'success': True, 'message':'Notes Updated Successfully.'}, status=status.HTTP_200_OK)
        return Response({'success': False, 'message':serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)


class RetrieveSubstringView(APIView):
    
    def get(self, request):
        substring = request.query_params.get('substring')
        notes = Notes.objects.filter(title__icontains=substring)
        serializer = NotesSerializers(notes, many=True)
        return Response({'success':True, 'data':serializer.data}, status=status.HTTP_200_OK)