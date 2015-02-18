from django.shortcuts import render_to_response

# Create your views here.
def index(request):
	a=5
	return render_to_response("index.html",{'a':a})