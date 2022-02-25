from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('', views.getRoutes),
    path('playground/', views.getNotes),
    path('playground/create/',views.createNote),
    path('playground/<str:pk>/update/', views.updateNote),
    path('playground/<str:pk>/delete/', views.deleteNote),
    path('playground/<str:pk>/', views.getNote),
    path('hello/',views.say_hello),
    path('sum/',views.index)
]