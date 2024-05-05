from django.urls import path
from .views import ToDoListCreateView, ToDoRetrieveUpdateDestroyView, UserToDoListView

urlpatterns = [
    path('', ToDoListCreateView.as_view(),name='todo-list-create'),
    path('<uuid:pk>/', ToDoRetrieveUpdateDestroyView.as_view(), name='todo-retrieve-update-destroy'),
    path('users/<int:user_id>/', UserToDoListView.as_view(), name='user-todo-list')
]