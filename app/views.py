# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app/index.html')
#    return HttpResponse("Hola, Mundo. Esta es de app index.")
