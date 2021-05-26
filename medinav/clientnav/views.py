from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from .models import SurveyResponse, TouchGesture, MotionSensor, SurveyCode, TextSurveyResponse, SwipeSurveyResponse
from django.views.decorators.csrf import csrf_exempt
import logging


logger = logging.getLogger(__name__)
# Create your views here.

def index(request):
    return render(request, 'clientnav/index.html')

def get_index(request):
    return render(request, 'clientnav/index.html')

def get_help(request):
    return render(request, 'clientnav/help.html')

def get_selectmix(request):
    return render(request, 'clientnav/selectmix.html')

def get_showmix(request):
    return render(request, 'clientnav/showmix.html')
