from django.urls import path
from codingsession import views

urlpatterns = [
	path('home/', views.codingsessionpage, name = 'codingsessionspage'),
]