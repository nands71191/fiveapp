from django.shortcuts import render
from codingsession.models import codingsession
# Create your views here.

def codingsessionpage(request):
	coding_session = codingsession.objects.all()
	print(coding_session)
	return render(request, template_name="codingsession/all.html", context={'coding_sessions' : coding_sessions})
