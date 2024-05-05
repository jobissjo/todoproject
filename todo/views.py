from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import ToDo
from .serializers import ToDoSerializers
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
# Create your views here.

class ToDoListCreateView(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializers
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ToDoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializers
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class UserToDoListView(generics.ListAPIView):
    serializer_class = ToDoSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        todos = ToDo.objects.filter(user_id_id = user_id).all()
        return todos
