from django.http import HttpResponse as http

def index(reauest):
	return http("Hello World")