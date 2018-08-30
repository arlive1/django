from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
import time


# Create your views here.
@api_view(["POST"])
def IdealWeight(heightdata):
    try:
        height=json.loads(heightdata.body)
        height=height["h"]
        weight=str(height*10)
        return JsonResponse("Ideal weight should be:"+weight+" kg",safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def ts(request):
    return Response(time.time())

@api_view(["GET"])
def ts2(request):
    stri = request.GET['reverse']
    return Response(stri[::-1])