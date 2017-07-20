#!/usr/bin/python
#_*_coding:utf-8_*_
from django.shortcuts import render,HttpResponse,render_to_response

# Create your views here.
def page_404(request):
    return render_to_response('404.html')
def page_403(request):
    return render_to_response('403.html')
def page_500(request):
    return render_to_response('500.html')