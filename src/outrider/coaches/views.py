# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from outrider.outriderClient import OutriderClient

# Create your views here.

def index(request):
	return HttpResponse("Hello, coaches!")

@login_required
def search(request):
	if request.method == "POST":
		search_key = request.POST['search']
		client = OutriderClient()
		results = client.request("GET", "/softball/coaches/%s" % search_key)
		coaches = results['data']
		return render(request, 'search.html', {'search_results': coaches})

	return render(request, 'search.html')
