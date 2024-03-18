from django.urls import path
from api import views

urlpatterns = [
    path('notes/', views.CreateNotesView.as_view()),
    path('notes/<int:pk>/', views.RetrieveUpdateNotesView.as_view()),
    path('notes-substring/', views.RetrieveSubstringView.as_view()),

]