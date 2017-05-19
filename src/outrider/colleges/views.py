# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from outrider.outriderClient import OutriderClient

# Create your views here.
def index(request):
	return HttpResponse("Hello, outrider!")

def search(request):
	if request.method == "POST":
		search_key = request.POST
		client = OutriderClient()
		results = client.request("GET", "/states/%s" % search_key)
		return render(request, 'search.html', {'search_results': results})

	return render(request, 'search.html')
