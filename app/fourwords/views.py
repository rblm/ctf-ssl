from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import random
with open('/opt/app/fourwords/rockyou-50.txt') as f:
    lines = f.read().splitlines()


def index(request):
    flag='FLAG{'+'-'.join([ lines[random.randint(0,len(lines))] for i in range(4)])+'}'
    return HttpResponse(flag)
