from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path ('', views.Home.as_view(), name='home'),
    path ('questions/', views.QuestionListView.as_view()),
    path ('questions/create/', views.QuestionCreateView.as_view()),
    path ('questions/update/<int:pk>/', views.QuestionUpdateView.as_view()),
    path ('questions/delete/<int:pk>/', views.QuestionDeleteView.as_view()),
]
