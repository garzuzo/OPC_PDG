from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from django.http import HttpResponse, JsonResponse

from opcapp.models import (RoleUser, Gender, HigherLevelEducation, AchievedLevel, State, Country, City, ComunaCorregimiento, NeightborhoodVereda, Zone, Campaign)
from opcapp.serializers import (RoleUserSerializer, GenderSerializer, HigherLevelEducationSerializer, CountrySerializer, AchievedLevelSerializer, StateSerializer, CitySerializer, ComunaCorregimientoSerializer, NeightborhoodVeredaSerializer, ZoneSerializer, CampaignSerializer)
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


@api_view(['GET'])
def leveleducation_list(request):
    if request.method == "GET":
        name=request.query_params.get('name', None)
        if name is not None:
            levelsEducationList=AchievedLevel.objects.filter(higherLevelEducation__name=name)
            serializer=AchievedLevelSerializer(levelsEducationList, many=True)
            return Response(serializer.data)



      
@api_view(['GET'])
def states_list(request):
    if request.method == "GET":
        country=request.query_params.get('country', None)
        if country is not None:
            #countryAct=Country.objects.filter(name=country).first()
            statesList=State.objects.filter(country__name=country)
            serializer=StateSerializer(statesList, many=True)
            return Response(serializer.data)

@api_view(['GET'])
def cities_list(request):
    if request.method == "GET":
        state=request.query_params.get('state', None)
        if state is not None:
            citiesList=City.objects.filter(state__name=state)
            serializer=CitySerializer(citiesList, many=True)
            return Response(serializer.data)



@api_view(['GET'])
def corregcomunas_list(request):
    if request.method == "GET":
       #if 'city' or 'zone' are not informed, the values ​​are None.
        city=request.query_params.get('city', None)
        zone=request.query_params.get('zone', None)
        if city is not None and zone is not None:
            corregcomunasList=ComunaCorregimiento.objects.filter(city__name=city).filter(zone__zoneType=zone)
            serializer=ComunaCorregimientoSerializer(corregcomunasList, many=True)
            return Response(serializer.data)


@api_view(['GET'])
def zones_list(request):
    if request.method == "GET":
        zoneList=Zone.objects.all()
        serializer=ZoneSerializer(zoneList, many=True)
        return Response(serializer.data)




@api_view(['GET'])
def neigdhborvereda_list(request):
    if request.method == "GET":
       #if 'city' or 'zone'\ are not informed, the values ​​are None.
        city=request.query_params.get('city', None)
        zone=request.query_params.get('zone', None)
        if city is not None and zone is not None:
            cityAct=City.objects.filter(name=city).first()
            nvList=NeightborhoodVereda.objects.filter(zone__zoneType=zone).filter(comunaCorregimiento__city=cityAct.id)
            serializer=NeightborhoodVeredaSerializer(nvList, many=True)
            return Response(serializer.data)


@api_view(['GET'])
def acampaigns_list(request):
    if request.method == "GET":
        campList=Campaign.objects.filter(isActive=True)
        serializer=CampaignSerializer(campList, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def notacampaigns_list(request):
    if request.method == "GET":
        campList=Campaign.objects.filter(isActive=False)
        serializer=CampaignSerializer(campList, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def idk_list(request):
    if request.method == "POST":
        city=request.data.get('city', None)
        zone=request.data.get('zone', None)
        if city is not None and zone is not None:
            cityAct=City.objects.filter(name=city).first()
            corregcomunasList=ComunaCorregimiento.objects.filter(zone__name=zone).filter(comunaCorregimiento__city=city)
            serializer=ComunaCorregimientoSerializer(corregcomunasList, many=True)
            return Response(serializer.data)



class HigherLevelEducationViewSet(viewsets.ModelViewSet):
    queryset = HigherLevelEducation.objects.all()
    serializer_class = HigherLevelEducationSerializer


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





    