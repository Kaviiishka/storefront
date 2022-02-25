from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note

# Create your views here.
# request -> response
# request handler
# action

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body' :""},
            'description': 'Creates new note with data sent in post'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': {'body': ""},
            'description': 'Deletes and exiting note'
        },
    ],
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    data = request.data;

    note = Note.objects.create(
        body=data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateNote(request,pk):
    data = request.data;

    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request,pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted!')

def index(request):
    a = 10
    b = 15
    c = my_func(a,b)
    print('Total:',c)
    return HttpResponse(f"Hello, world, Total is {str(c)}")

def my_func(a,b):
    print("Inside Sum function")
    c = a+b
    return c

def say_hello(request): #this func should take a request object and return a response
    #Pull data from db
    #Transform
    #Send email
    #return HttpResponse('Hello World')
    return render(request, 'hello.html',{'name':'Kavishka'})
#we need to map this view to a url, when we get a request at that url this function will be called