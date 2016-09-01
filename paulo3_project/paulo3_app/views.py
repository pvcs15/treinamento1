from django.shortcuts import render

def index(request):
	template_name = 'index.html'
	return render(request, template_name)

def contato(request):
	template_name = 'contato.html'
	return render(request, template_name)

def Cursos(request):
	template_name = 'Cursos.html'
	return render(request, template_name)
