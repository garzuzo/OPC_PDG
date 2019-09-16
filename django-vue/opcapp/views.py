from django.shortcuts import render
from rest_framework.decorators import api_view


# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



def public(request):
    return HttpResponse("You don't need to be authenticated to see this")


@api_view(['GET'])
def private(request):
    return HttpResponse("You should not see this message if not authenticated!")


@api_view(['GET'])
def narratives(request):
    return HttpResponse("You should not see this message if not authenticated!")