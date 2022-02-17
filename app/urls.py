from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('<slug:res>/', views.display_snippet, name='display_snippet'),
]

