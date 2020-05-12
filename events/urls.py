from django.urls import path
from . import views

urlpatterns = [
    path('api/event/', views.EventListCreate.as_view() ),
    path('api/event/<pk>/', views.EventRetrieveDestroy.as_view()),
]
