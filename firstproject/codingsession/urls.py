from django.urls import path
from codingsession import views

urlpatterns = [
	path('', views.codingsessionpage, name = 'codingsessionspage'),
	path('home/', views.codingsessionpage, name = 'codingsessionspage'),
]