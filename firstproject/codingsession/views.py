from django.shortcuts import render, HttpResponse

# Create your views here.

def codingsessionpage(request):
	return HttpResponse('<h1>Hello World</h1>')
