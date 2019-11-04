from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from django.http import HttpResponse, JsonResponse

from opcapp.models import (RoleUser, 
Gender, 
HigherLevelEducation, 
AchievedLevel, 
State, 
Country, 
City, 
ComunaCorregimiento, 
NeighborhoodVereda, 
Zone, 
Campaign, 
ActivityNarrative, 
Concept, 
KeyConcept,
RoleCampaign)

from opcapp.serializers import (RoleUserSerializer, 
GenderSerializer, 
HigherLevelEducationSerializer, 
CountrySerializer, 
AchievedLevelSerializer, 
StateSerializer, 
CitySerializer, 
ComunaCorregimientoSerializer, 
NeighborhoodVeredaSerializer, 
ZoneSerializer, CampaignSerializer, 
ActivityNarrativeSerializer, 
ConceptSerializer, 
KeyConceptSerializer,
UserSerializer,
RoleCampaignSerializer)
from rest_framework import viewsets

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

#Auth
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout

#Hash
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User

from datetime import date

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
#@permission_classes([IsAuthenticated])
def zones_list(request):
    if request.method == "GET":
        zoneList=Zone.objects.all()
        serializer=ZoneSerializer(zoneList, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def neighborvereda_list(request):
    if request.method == "GET":
       #if 'city' or 'zone'\ are not informed, the values ​​are None.
        city=request.query_params.get('city', None)
        zone=request.query_params.get('zone', None)
        comunaCorregimiento=request.query_params.get('comuna_corregimiento', None)
        if city is not None and zone is not None and comunaCorregimiento is not None :
            nvList=NeighborhoodVereda.objects.filter(zone__zoneType=zone).filter(comunaCorregimiento__city__name=city,comunaCorregimiento__name=comunaCorregimiento)
            serializer=NeighborhoodVeredaSerializer(nvList, many=True)
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


@api_view(['GET'])
def fivekeywords_list(request):
    if request.method == "GET":
       #if 'city' or 'zone'\ are not informed, the values ​​are None.
        id=request.query_params.get('id', None)

        if id is not None:
            conceptsCampaignList=KeyConcept.objects.filter(activityNarrative__campaign_id=id).order_by('frequency').reverse()[:5]
           
            serializer=KeyConceptSerializer(conceptsCampaignList, many=True)
            return Response(serializer.data)

@api_view(['GET'])
def womenmen_campaign_list(request):
    if request.method == "GET":
       #if 'city' or 'zone'\ are not informed, the values ​​are None.
        id=request.query_params.get('id', None)
        comuna=request.query_params.get('comuna', None)
        if id is not None and comuna is not None:
  
            numMasculino=PersonCampaign.objects.filter(campaign=id, gender__typeGender='Masculino').filter(neighborhoodVeredaActual__comunaCorregimiento__zone__zoneType='Urbana', neighborhoodVeredaActual__comunaCorregimiento__name=comuna).len()
            numFemenino=PersonCampaign.objects.filter(campaign=id, gender__typeGender='Femenino').filter(neighborhoodVeredaActual__comunaCorregimiento__zone__zoneType='Urbana', neighborhoodVeredaActual__comunaCorregimiento__name=comuna).len()
            
            data = {
                "men": numMasculino,
                "women":numFemenino
            }
            
            return JsonResponse(data)


@api_view(['GET'])
def age_range_campaign_list(request):
    if request.method == "GET":
       #if 'city' or 'zone'\ are not informed, the values ​​are None.
        id=request.query_params.get('id', None)
        comuna=request.query_params.get('comuna', None)
        if id is not None and comuna is not None:
            #, calculate_age(birthdate)=0,calculate_age(birthdate)=5
            #, calculate_age(birthdate)=6,calculate_age(birthdate)=11
            #, calculate_age(birthdate)=12,calculate_age(birthdate)=18
            #, calculate_age(birthdate)=19,calculate_age(birthdate)=26
            #, calculate_age(birthdate)=27,calculate_age(birthdate)=59
            #, calculate_age(birthdate)=60

            primeraInfanciaMin=calculate_mindate(0)
            primeraInfanciaMax=calculate_mindate(5)
            infanciaMin=calculate_mindate(6)
            infanciaMax=calculate_mindate(11)
            adolescenciaMin=calculate_mindate(12)
            adolescenciaMax=calculate_mindate(18)
            juventudMin=calculate_mindate(19)
            juventudMax=calculate_mindate(26)
            adultezMin=calculate_mindate(27)
            adultezMax=calculate_mindate(59)
            vejez=calculate_mindate(60)
          

            primeraInfanciaList=PersonCampaign.objects.filter(campaign=id, birthdate__gte=primeraInfanciaMin, birthdate__lte=primeraInfanciaMax).filter(neighborhoodVeredaActual__comunaCorregimiento__zone__zoneType='Urbana', neighborhoodVeredaActual__comunaCorregimiento__name=comuna).len()
            infanciaList=PersonCampaign.objects.filter(campaign=id, birthdate__gte=infanciaMin, birthdate__lte=infanciaMax).filter(neighborhoodVeredaActual__comunaCorregimiento__zone__zoneType='Urbana', neighborhoodVeredaActual__comunaCorregimiento__name=comuna).len()
            adolescenciaList=PersonCampaign.objects.filter(campaign=id, birthdate__gte=adolescenciaMin, birthdate__lte=adolescenciaMax).filter(neighborhoodVeredaActual__comunaCorregimiento__zone__zoneType='Urbana', neighborhoodVeredaActual__comunaCorregimiento__name=comuna).len()
            juventudList=PersonCampaign.objects.filter(campaign=id, birthdate__gte=juventudMin, birthdate__lte=juventudMax).filter(neighborhoodVeredaActual__comunaCorregimiento__zone__zoneType='Urbana', neighborhoodVeredaActual__comunaCorregimiento__name=comuna).len()
            adultezList=PersonCampaign.objects.filter(campaign=id, birthdate__gte=adultezMin, birthdate__lte=adultezMax).filter(neighborhoodVeredaActual__comunaCorregimiento__zone__zoneType='Urbana', neighborhoodVeredaActual__comunaCorregimiento__name=comuna).len()
            vejezList=PersonCampaign.objects.filter(campaign=id, birthdate__gte=vejez).filter(neighborhoodVeredaActual__comunaCorregimiento__zone__zoneType='Urbana', neighborhoodVeredaActual__comunaCorregimiento__name=comuna).len()

            


            data = {


                'primeraInfancia':primeraInfanciaList,
                'infancia':infanciaList,
                'adolescencia':adolescenciaList,
                'juventud':juventudList,
                'adultez':adultezList,
                'vejez':vejezList,

            }
            return JsonResponse(data)


def calculate_mindate(age):
    today = date.today()
    minYear = today.year-age
    minDate = date(minYear, today.month, today.day)
    return minDate



@api_view(['GET'])
def population_comunas_list(request):
    if request.method == "GET":
       #if 'city' or 'zone'\ are not informed, the values ​​are None.
        id=request.query_params.get('id', None)
        comuna=request.query_params.get('comuna', None)
        if id is not None and comuna is not None:
           
            numPeople=PersonCampaign.objects.filter(campaign=id).filter(neighborhoodVeredaActual__comunaCorregimiento__zone__zoneType='Urbana', neighborhoodVeredaActual__comunaCorregimiento__name=comuna).len()
           
            data = {
                "frequency": numPeople
            }
            
            return JsonResponse(data)



@api_view(['GET'])
def narratives_campaign_list(request):
    if request.method == "GET":
        id=request.query_params.get('id', None)
        if id is not None:

            narrativesList=ActivityNarrative.objects.filter(Campaign__id=id)
            serializer=ActivityNarrativeSerializer(narrativesList, many=True)
            return Response(serializer.data)



@api_view(['POST'])
def create_user(request):
    if request.method == "POST":
        username=request.data.get('username', None)
        password=request.data.get('password', None)
        if username is not None and password is not None:
           
            passWithHash=make_password(password)
            print(passWithHash)
            serializer=None#ComunaCorregimientoSerializer(corregcomunasList, many=True)
            return Response(serializer.data)




@api_view(['POST'])
def save_info(request):
    if request.method == "POST":
       # email=request.data.get('email', None)
       # password=request.data.get('password', None)

        campaign =request.data.get('campaign', None)
        age=request.data.get('age', None)
        gender=request.data.get('gender', None)
        name=request.data.get('name', None)
        lastname=request.data.get('lastname', None)
        level=request.data.get('level', None)
        higherEducation=request.data.get('higherEducation', None)
        currentZone=request.data.get('currentZone', None)
        currentState=request.data.get('currentState', None)
        currentCity=request.data.get('currentCity', None)
        currentComuna=request.data.get('currentComuna', None)
        currentNeighborhood=request.data.get('currentNeighborhood', None)
        currentCorregimiento=request.data.get('currentCorregimiento', None)
        currentVereda=request.data.get('currentVereda', None)
        originZone=request.data.get('originZone', None)
        originState=request.data.get('originState', None)
        originCity=request.data.get('originCity', None)
        originComuna=request.data.get('originComuna', None)
        originNeighborhood=request.data.get('originNeighborhood', None)
        originCorregimiento=request.data.get('originCorregimiento', None)
        originVereda=request.data.get('originVereda', None)
        narrative=request.data.get('narrative', None)
        word1=request.data.get('word1', None)
        word2=request.data.get('word2', None)
        word3=request.data.get('word3', None)
        word4=request.data.get('word4', None)
        word5=request.data.get('word5', None)

        email=request.data.get('email', None)


        currentLevel3={}
        originLevel3={}
        if currentNeighborhood is not None and originNeighborhood is not None:
            currentLevel3=NeighborhoodVereda.objects.filter(name=currentNeighborhood, comunaCorregimiento__name=currentComuna)
            originLevel3=NeighborhoodVereda.objects.filter(name=originNeighborhood, comunaCorregimiento__name=currentComuna)
        elif currentVereda is not None and originVereda is not None:
            currentLevel3=NeighborhoodVereda.objects.filter(name=currentVereda, comunaCorregimiento__name=currentCorregimiento)
            originLevel3=NeighborhoodVereda.objects.filter(name=originVereda,comunaCorregimiento__name=originCorregimiento)
        else :
            currentLevel3=NeighborhoodVereda.objects.filter(comunaCorregimiento__city__name=currentCity)
            originLevel3=NeighborhoodVereda.objects.filter(comunaCorregimiento__city__name=originCity)


        if name is not None and lastname is not None:

            

            education=AchievedLevel.objects.filter(higherLevelEducation_name=higherEducation,name=level).id
            genderId=Gender.objects.filter(typeGender=gender).id
            roleUserId=RoleUser.objects.filter(name="Registrado").id

            CityCurrentId=City.objects.filter(name=currentCity, state__name=currentState)#, state__country__name=currentCountry)
            CityOriginId=City.objects.filter(name=originCity, state__name=originState)

           # currentVeredaId=
           # originVeredaId=
            #originNeighborhoodId=
            #currentNeighborhoodId=

           # neighborhoodVeredaSource=NeighborhoodVereda.objects.filter(name=)
            #neighborhoodVeredaActual=
            dataPerson={
                'name':name, 
                'lastname':lastname, 
                'birthdate':age,        
                'achievedLevel':education,
                'gender':genderId,
                'neighborhoodVeredaSource':originLevel3,
                'neighborhoodVeredaActual':currentLevel3,
                'roleUser':roleUserId,
                'user':None

    #achievedLevel=models.ForeignKey(AchievedLevel, on_delete=models.CASCADE)
   # gender=models.ForeignKey(Gender, on_delete=models.CASCADE)
    #neighborhoodVeredaSource=models.ForeignKey(NeighborhoodVereda, on_delete=models.CASCADE,related_name='personterritorysource', blank= True)
   # neighborhoodVeredaActual=models.ForeignKey(NeighborhoodVereda, on_delete=models.CASCADE,related_name='personterritoryactual', blank= True)
   # user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
            }
    
            roleCampaignId=RoleCampaign.objects.filter(name="Registrado").id

            dataPersonCampaign={
            #    person=models.ForeignKey(Person, on_delete=models.CASCADE)
             #   roleCampaign=models.ForeignKey(RoleCampaign, on_delete=models.CASCADE)
                'person':name, 
                'roleCampaign':lastname, 
                'campaign':age,
                'achievedLevel':education,
                'gender':genderId,
                'neighborhoodVeredaSource':originLevel3,
                'neighborhoodVeredaActual':currentLevel3,
            
            }   
            dataKeyConcept1={
                'name':word1
            }
            dataKeyConcept2={
                'name':word2
            }
            dataKeyConcept3={
                'name':word3
            }
            dataKeyConcept4={
                'name':word4
            }

            dataKeyConcept5={
                'name':word5
            }

                
            personCampaign=PersonCampaign.objects.filter()
            activityNarrative=ActivityNarrative.objects.filter()
            keyConcept=KeyConcept.objects.filter()
            keyConcept.activityNarrative.add(activityNarrative)
   #             campaign=models.ForeignKey(Campaign, on_delete=models.CASCADE)
  #  achievedLevel=models.ForeignKey(AchievedLevel, on_delete=models.CASCADE)
   # gender=models.ForeignKey(Gender, on_delete=models.CASCADE)
  #  neighborhoodVeredaSource=models.ForeignKey(NeighborhoodVereda, on_delete=models.CASCADE,related_name='personcampaignterritorysource')
   # neighborhoodVeredaActual=models.ForeignKey(NeighborhoodVereda, on_delete=models.CASCADE,related_name='personcampaignterritoryactual')

            
            serializer=ComunaCorregimientoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_view(request):
    if request.method == "POST":
        username=request.data.get('username', None)
        password=request.data.get('password', None)
        if username is not None and password is not None:
            user = authenticate(username=username, password=password)
            if user is not None:
                #login() saves the user’s ID in the session, using Django’s session framework.
                login(request, user)
                return HttpResponse("You're logged in.")
            else:
                return HttpResponse("Your username and password didn't match.")


@api_view(['POST'])
def register(request):
    if request.method == "POST":
        username=request.data.get('username', None)
        password=request.data.get('password', None)
        if username is not None and password is not None:
            
            user = User.objects.create_user(username=username,
                                 email=username,
                                 password=password)
            
            user.save()
            serializer=UserSerializer(user)
            
            return Response(serializer.data)

  
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def valid_user(request):
    print(request.user.email)
    return HttpResponse("=)")
    

@api_view(['GET'])
def logout_view(request):
    logout(request)
    return HttpResponse("You're logged out.")
    


@api_view(['POST'])
def create_comunacorr(request):
    if request.method == "POST":
        name=request.data.get('name', None)
        city_id=request.data.get('city', None)
        zone_id=request.data.get('zone', None)
        if name is not None and city_id is not None and zone_id is not None:

            #city=City.objects.get(id=city_id)
            #zone=Zone.objects.get(id=zone_id)
            data={
                'name':name, 'city':city_id, 'zone':zone_id

            }
            serializer=ComunaCorregimientoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  
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





    