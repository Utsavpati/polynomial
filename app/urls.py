from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('renew/<int:id>',views.renew,name='renew'),
    path('<slug:res>/', views.display_snippet, name='display_snippet'),
]

