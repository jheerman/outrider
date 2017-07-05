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
		results = client.request("GET", "search/%s" % search_key)
		schools = results['data']
		return render(request, 'colleges.html', {'search_results': schools})

	return render(request, 'colleges.html')

@login_required
def college_detail(request, slug):
	client = OutriderClient()

	college_results = client.request("GET", "%s" % slug)
	softball_program = client.request("GET", "softball/%s" % slug)
	admission_results = client.request("GET", "admissions/%s" % slug)
	demographics_results = client.request("GET", "demographics/%s" % slug)
	coach_results = client.request("GET", "softball/coaches/%s" % slug)

	if coach_results['data']:
		coaches = coach_results['data'][0]
	else:
		coaches = None	

	if admission_results['data']:
		admissions = admission_results['data'][0]
	else:
		admissions = None

	if softball_program['data']:
		softball = softball_program['data'][0]
	else:
		softball = None

	if college_results['data']:
		college = college_results['data'][0]
	else:
		college = None

	if demographics_results['data']:
		demographics = demographics_results['data'][0]
	else:
		demographics = None

	return render(request, 'college_detail.html', 
			{'admissions': admissions,
			 'coach': coaches,
			 'college': college,
		     'demographics': demographics,
			 'softball': softball},)
