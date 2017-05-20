# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from outrider.outriderClient import OutriderClient

# Create your views here.
def index(request):
	return HttpResponse("Hello, outrider!")

def search_by_state(request):
	if request.method == "POST":
		search_key = request.POST['search']
		client = OutriderClient()
		results = client.request("GET", "/states/%s" % search_key)
		schools = results['data']
		return render(request, 'search.html', {'search_results': schools})

	return render(request, 'search.html')

def search(request):
	if request.method == "POST":
		search_key = request.POST['search']
		client = OutriderClient()
		results = client.request("GET", "/teams/%s" % search_key)
		schools = results['data']
		return render(request, 'search.html', {'search_results': schools})

	return render(request, 'search.html')
