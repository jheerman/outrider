# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from outrider.outriderClient import OutriderClient

# Create your views here.
def index(request):
	return HttpResponse("Hello, outrider!")

@login_required
def search_by_state(request):
	if request.method == "POST":
		search_key = request.POST['search']
		client = OutriderClient()
		results = client.request("GET", "/states/%s" % search_key)
		schools = results['data']
		return render(request, 'colleges.html', {'search_results': schools})

	return render(request, 'colleges.html')

@login_required
def college_search(request):
	if request.method == "POST":
		search_key = request.POST['search']
		client = OutriderClient()
		results = client.request("GET", "teams/%s" % search_key)
		schools = results['data']
		return render(request, 'colleges.html', {'search_results': schools})

	return render(request, 'colleges.html')

@login_required
def college_detail(request, school_name):
	client = OutriderClient()
	softball_program = client.request("GET", "%s/softball" % school_name)
	admission_results = client.request("GET", "admissions/%s" % school_name)
	if len(admission_results) > 0:
		admissions = admission_results['data'][0]
	else:
		admissions = None

	if len(softball_program) > 0:
		softball = softball_program['data'][0]
	else:
		None

	return render(request, 'college_detail.html', 
			{'admissions': admissions,
			'softball': softball},)
