from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from django.http import HttpResponse, JsonResponse

from .models import (RoleUser, Gender)
from .serializers import (RoleUserSerializer, GenderSerializer)
from rest_framework import viewsets

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET','POST','PUT'])
def roleuser_list(request, pk):


    try:
        roleUser= RoleUser.objects.get(pk=pk)
    except RoleUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        roleuserList=RoleUser.objects.all()
        serializer=RoleUserSerializer(roleuserList, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer=RoleUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PUT":
        serializer=RoleUserSerializer(roleUser,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class RoleUserViewSet(viewsets.ModelViewSet):
    queryset = RoleUser.objects.all()
    serializer_class = RoleUserSerializer


class GenderViewSet(viewsets.ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer

def users(request):

    if request.method=='GET':
        listUsers = RoleUser.objects.all()
        data = {"ListaUsuarios": "listUsers"}
        response = JsonResponse(data)
        return response
    elif request.method=='POST':
        roleAct=RoleUser(name="Proyectista")
        roleAct.save()
        return HttpResponse("Added successfully")




def public(request):
    return HttpResponse("You don't need to be authenticated to see this")


@api_view(['GET'])
def private(request):
    return HttpResponse("You should not see this message if not authenticated!")


@api_view(['GET'])
def narratives(request):
    return HttpResponse("You should not see this message if not authenticated!")





    