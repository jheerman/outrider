# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Hello, outrider!")

def search(request):
	if request.method == "POST":
		search_key = request.POST
		client = OutriderClient()
		response = client.request("GET", "/stats/%s" % search_key)
		render(request, 'colleges.html', {'search_results': response})
