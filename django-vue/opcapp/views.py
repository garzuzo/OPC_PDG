from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from django.http import HttpResponse, JsonResponse

from opcapp.models import *

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
RoleCampaignSerializer,
PersonSerializer,
PersonCampaignSerializer)


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



#Analitica

#Tener en cuenta rutas:
#os.getcwd()+'/../modelo_entrenado.pkl'
#os.getcwd()+'/../data/df_limpieza.xlsx'
from opcapp.analitica import clean_text,obtain_topics


@api_view(['GET'])
def predictTopic(request):
 
    text=request.query_params.get("text",None)

    data_list=clean_text(text)
    topics_list=obtain_topics(data_list)

    
    data={
        "topics":topics_list
    }
    return JsonResponse(data)

    



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

        campList=Campaign.objects.filter(startDate__lte=date.today(),endDate__gte=date.today())
        serializer=CampaignSerializer(campList, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def notacampaigns_list(request):
    if request.method == "GET":
        campList=Campaign.objects.filter(endDate__lt=date.today())
        serializer=CampaignSerializer(campList, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def fivekeywords_list(request):
    if request.method == "GET":
       #if 'city' or 'zone'\ are not informed, the values ​​are None.
        id=request.query_params.get('id', None)

        if id is not None:
            conceptsCampaignList=KeyConcept.objects.filter(activityNarrative__campaign__id=id).order_by('frequency').reverse()[:5]
           
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

            narrativesList=ActivityNarrative.objects.filter(campaign__id=id)
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
def save_info_zone(request):
    name=request.data.get('name', None)
    data={"id":100,"name":None}
    serializer=CountrySerializer(data=data)
   
    data.update({'name':name})

    if serializer.is_valid():
        serializer.save()
        idCountry=serializer.data
        

        print(idCountry)


    return Response(serializer.data)


@api_view(['POST'])
def save_campaign(request):
    startDate=request.data.get('start_date',None)
    endDate=request.data.get('end_date',None)
    description=request.data.get('description',None)
    title=request.data.get('title',None)
    narrativesGoal=request.data.get('narratives_goal',None)
    accumulatedNarratives=request.data.get('accumulated_narratives',None)
    isActive=request.data.get('is_active',None)

    validDate=True if endDate>date.today() else False

    if validDate and startDate is not None and endDate is not None and description is not None and title is not None and narrativesGoal is not None and accumulatedNarratives is not None and isActive is not None:
        
        data={
            "startDate":startDate,
            "endDate":endDate,
            "description":description,
            "title":title,
            "narrativesGoal":narrativesGoal,
            "accumulatedNarratives":accumulatedNarratives,
            "isActive":isActive
        }
        
        campaignSerializer=CampaignSerializer(data=data)

        if campaignSerializer.is_valid():
            campaignSerializer.save()



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def city_person(request):
    if request.method == "GET":

        person=Person.objects.get(user=request.user.id)
        neighVer=NeighborhoodVereda.objects.get(id=person.neighborhoodVeredaActual)
        comunaCorr=ComunaCorregimiento.objects.get(id=neighVer.comunaCorregimiento)
        city=City.objects.get(id=comunaCorr.city)

        data = {
                "city_name": city.name
            }
            
        return JsonResponse(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def campaigns_person(request):
    if request.method == "GET":

        person=Person.objects.get(user=request.user.id)
        numPersonCampaign=PersonCampaign.objects.filter(person=person.id).len()

        data = {
                "campaings_person": numPersonCampaign
            }
            
        return JsonResponse(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def campaigns_created_person(request):
    if request.method == "GET":

        person=Person.objects.get(user=request.user.id)
        numPersonCampaignCreated=PersonCampaign.objects.filter(person=person.id,roleCampaign="Proyectista").len()

        data = {
                "campaings_created_person": numPersonCampaignCreated
            }
            
        return JsonResponse(data)

#test PUT
@api_view(['PUT'])
#@permission_classes([IsAuthenticated])
def t_change_zone(request):
    id=request.data.get('id')
    name=request.data.get('name')
    zone=Zone.objects.get(id=id)
    zone.zoneType=name
    zone.save()
    serializer=ZoneSerializer(zone)
    return Response(serializer.data)


@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def person_data(request):
    if request.method == "GET":

        person=Person.objects.get(user=request.user.id)

        data = {
            #'phoneNumber':person.phoneNumber,
            'achievedLevel':person.achievedLevel,
            'birthdate':person.birthdate,
            'neighborhoodVeredaActual':person.neighborhoodVeredaActual,
            'neighborhoodVeredaSource':person.neighborhoodVeredaSource,
            }
            
        return JsonResponse(data)

    elif request.method =="PUT":
       # phoneNumber=request.data.get('phoneNumber')
        achievedLevel=request.data.get('achievedLevel')
        birthdate=request.data.get('birthdate')
        neighborhoodVeredaActual=request.data.get('neighborhoodVeredaActual')
        neighborhoodVeredaSource=request.data.get('neighborhoodVeredaSource')
           
        person=Person.objects.get(user=request.user.id)
        #person.phoneNumber=phoneNumber
        person.achievedLevel=achievedLevel
        person.birthdate=birthdate
        person.neighborhoodVeredaActual=neighborhoodVeredaActual
        person.neighborhoodVeredaSource=neighborhoodVeredaSource
        person.save()
        serializer=PersonSerializer(person)
        return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_info_registered_user(request):
    if request.method == "POST":
        narrative=request.data.get('narrative', None)
        word1=request.data.get('word1', None)
        word2=request.data.get('word2', None)
        word3=request.data.get('word3', None)
        word4=request.data.get('word4', None)
        word5=request.data.get('word5', None)
        campaign =request.data.get('campaign', None)

        idUser=request.user.id
        person=Person.objects.get(user=idUser)
        roleUserId=RoleCampaign.objects.get(name="Invitado").id

        dataPersonCampaign={
            'person':person.id, 
            'roleCampaign':roleUserId, 
            'campaign':campaign,
            'achievedLevel':person.achievedLevel.id,
            'gender':person.gender,
            'neighborhoodVeredaSource':person.neighborhoodVeredaSource.id,
            'neighborhoodVeredaActual':person.neighborhoodVeredaActual.id,
            
        }

   

        serializerPersonCampaign=PersonCampaignSerializer(data=dataPersonCampaign)
        if serializerPersonCampaign.is_valid():
            personCampaignAct=serializerPersonCampaign.save()

        idPersonCampaign=personCampaignAct.id

        dataActivityNarrative={
            "text":narrative,
            "campaign":campaign,
            "personCampaign":idPersonCampaign
        }

        serializerActivityNarrative = ActivityNarrativeSerializer(data=dataActivityNarrative)
        if serializerActivityNarrative.is_valid():
            activityNarrativeAct=serializerActivityNarrative.save()

            actualCampaign=Campaign.objects.filter(id=campaign)
            accNarratives=actualCampaign.accumulatedNarratives+1
            actualCampaign.uaccumulatedNarratives=accNarratives
            actualCampaign.save()

        idActivityNarrative=activityNarrativeAct

           
        kcw1=KeyConcept.objects.filter(name=word1).first()

        if kcw1 is not None:
            totalFreq=kcw1.frequency+1
            kcw1.frequency=totalFreq
            kcw1.activityNarrative.add(idActivityNarrative)
            kcw1.save()
            idKeyConcept1=kcw1.id
        else:

            keyConcept1Act=KeyConcept.objects.create(name=word1,frequency=1)
            keyConcept1Act.activityNarrative.add(idActivityNarrative)
            keyConcept1Act.save()



        kcw2=KeyConcept.objects.filter(name=word2).first()

        if kcw2 is not None:
            totalFreq=kcw2.frequency+1
            kcw2.frequency=totalFreq
            kcw2.activityNarrative.add(idActivityNarrative)               
            kcw2.save()
            idKeyConcept2=kcw2.id
        else:
            keyConcept2Act=KeyConcept.objects.create(name=word2,frequency=1)
            keyConcept2Act.activityNarrative.add(idActivityNarrative)
            keyConcept2Act.save()



        kcw3=KeyConcept.objects.filter(name=word3).first()

        if kcw3 is not None:
            totalFreq=kcw3.frequency+1
            kcw3.frequency=totalFreq
            kcw3.activityNarrative.add(idActivityNarrative)  
            kcw3.save()
            idKeyConcept3=kcw3.id
        else:
            keyConcept3Act=KeyConcept.objects.create(name=word3,frequency=1)
            keyConcept3Act.activityNarrative.add(idActivityNarrative)
            keyConcept3Act.save()


        kcw4=KeyConcept.objects.filter(name=word4).first()

        if kcw4 is not None:
            totalFreq=kcw4.frequency+1
            kcw4.frequency=totalFreq
            kcw4.activityNarrative.add(idActivityNarrative)  
            kcw4.save()
            idKeyConcept4=kcw4.id
        else:
            keyConcept4Act=KeyConcept.objects.create(name=word4,frequency=1)
            keyConcept4Act.activityNarrative.add(idActivityNarrative)
            keyConcept4Act.save()


        kcw5=KeyConcept.objects.filter(name=word5).first()

        if kcw5 is not None:
            totalFreq=kcw5.frequency+1
            kcw5.frequency=totalFreq
            kcw5.activityNarrative.add(idActivityNarrative)  
            kcw5.save()
            idKeyConcept5=kcw5.id
        else:
            keyConcept5Act=KeyConcept.objects.create(name=word5,frequency=1)
            keyConcept5Act.activityNarrative.add(idActivityNarrative)
            keyConcept5Act.save()


        if serializerPersonCampaign.is_valid():
            return Response(serializerPersonCampaign.data, status=status.HTTP_201_CREATED)
        return Response( status=status.HTTP_400_BAD_REQUEST)








@api_view(['POST'])
def save_info(request):
    if request.method == "POST":
       # email=request.data.get('email', None)
       # password=request.data.get('password', None)
        age=request.data.get('age', None)
        campaign =request.data.get('campaign', None)
        gender=request.data.get('gender', None)
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
        password=request.data.get('password', None)

        currentLevel3=0
        originLevel3=0
        if currentNeighborhood != 0 and currentVereda  == 0:
            currentLevel3=currentNeighborhood
            

        elif currentNeighborhood == 0 and currentVereda  != 0:
            currentLevel3=currentVereda

        if originNeighborhood != 0 and originVereda == 0:
            originLevel3=originNeighborhood

        elif originNeighborhood == 0 and originVereda != 0:
            originLevel3=originVereda


        if currentNeighborhood == 0 and currentVereda == 0 :
            currentLevel3=NeighborhoodVereda.objects.filter(comunaCorregimiento__city__id=currentCity ).first()


        if currentNeighborhood == 0 and currentVereda == 0 :
            originLevel3=NeighborhoodVereda.objects.filter(comunaCorregimiento__city__id=originCity).first()


       # print(currentLevel3)
       # print(originLevel3)

        idUser=None

        if email is not None and password is not None: #and so on...
            dataUser={
                'username':email,
                'email':email,
                'password':password,
                'isActive': False
            }
            userSerializer=UserSerializer(data=dataUser)
            if userSerializer.is_valid():
                userAct=userSerializer.save()
                idUser=userAct.id


        if level is not None and originLevel3 is not None:

            #debe existir registrado en la db
            roleUserId=RoleUser.objects.filter(name="Registrado").first().id
            #print(roleUserId)
            dataPerson={
                'birthdate':age,        
                'achievedLevel':level,
                'gender':gender,
                'neighborhoodVeredaSource':originLevel3,
                'neighborhoodVeredaActual':currentLevel3,
                'roleUser':roleUserId,
                'user':None

            }

            
            #Si se va a crear una cuenta actualizo el dict para luego guardar el objeto
            if idUser is not None:
                dataPerson.update({'user':idUser})

            personAct=None
            serializerPerson=PersonSerializer(data=dataPerson)

            if serializerPerson.is_valid():
               personAct= serializerPerson.save()
                
           #debe existir Invitado en la db
            roleCampaignId=RoleCampaign.objects.filter(name="Invitado").first().id

           # print(serializerPerson.data)

            idPerson=personAct.id

            dataPersonCampaign={
            #    person=models.ForeignKey(Person, on_delete=models.CASCADE)
             #   roleCampaign=models.ForeignKey(RoleCampaign, on_delete=models.CASCADE)
                'person':idPerson, 
                'roleCampaign':roleCampaignId, 
                'campaign':campaign,
                'achievedLevel':level,
                'gender':gender,
                'neighborhoodVeredaSource':originLevel3,
                'neighborhoodVeredaActual':currentLevel3,
            
            }



            serializerPersonCampaign=PersonCampaignSerializer(data=dataPersonCampaign)
            if serializerPersonCampaign.is_valid():
               personCampaignAct= serializerPersonCampaign.save()

            idPersonCampaign=personCampaignAct.id

            dataActivityNarrative={
                "text":narrative,
                "campaign":campaign,
                "personCampaign":idPersonCampaign
            }

            serializerActivityNarrative = ActivityNarrativeSerializer(data=dataActivityNarrative)
            if serializerActivityNarrative.is_valid():
                activityNarrativeAct= serializerActivityNarrative.save()

                actualCampaign=Campaign.objects.filter(id=campaign).first()
                accNarratives=actualCampaign.accumulatedNarratives+1
                actualCampaign.accumulatedNarratives=accNarratives
                actualCampaign.save()

            idActivityNarrative=activityNarrativeAct

           
            kcw1=KeyConcept.objects.filter(name=word1).first()

            if kcw1 is not None:
                totalFreq=kcw1.frequency+1
                kcw1.frequency=totalFreq
                kcw1.activityNarrative.add(idActivityNarrative)
                kcw1.save()
                idKeyConcept1=kcw1.id
            else:

                keyConcept1Act=KeyConcept.objects.create(name=word1,frequency=1)
                keyConcept1Act.activityNarrative.add(idActivityNarrative)
                keyConcept1Act.save()



            kcw2=KeyConcept.objects.filter(name=word2).first()

            if kcw2 is not None:
                totalFreq=kcw2.frequency+1
                kcw2.frequency=totalFreq
                kcw2.activityNarrative.add(idActivityNarrative)               
                kcw2.save()
                idKeyConcept2=kcw2.id
            else:
                keyConcept2Act=KeyConcept.objects.create(name=word2,frequency=1)
                keyConcept2Act.activityNarrative.add(idActivityNarrative)
                keyConcept2Act.save()



            kcw3=KeyConcept.objects.filter(name=word3).first()

            if kcw3 is not None:
                totalFreq=kcw3.frequency+1
                kcw3.frequency=totalFreq
                kcw3.activityNarrative.add(idActivityNarrative)  
                kcw3.save()
                idKeyConcept3=kcw3.id
            else:
                keyConcept3Act=KeyConcept.objects.create(name=word3,frequency=1)
                keyConcept3Act.activityNarrative.add(idActivityNarrative)
                keyConcept3Act.save()


            kcw4=KeyConcept.objects.filter(name=word4).first()

            if kcw4 is not None:
                totalFreq=kcw4.frequency+1
                kcw4.frequency=totalFreq
                kcw4.activityNarrative.add(idActivityNarrative)  
                kcw4.save()
                idKeyConcept4=kcw4.id
            else:
                keyConcept4Act=KeyConcept.objects.create(name=word4,frequency=1)
                keyConcept4Act.activityNarrative.add(idActivityNarrative)
                keyConcept4Act.save()


            kcw5=KeyConcept.objects.filter(name=word5).first()

            if kcw5 is not None:
                totalFreq=kcw5.frequency+1
                kcw5.frequency=totalFreq
                kcw5.activityNarrative.add(idActivityNarrative)  
                kcw5.save()
                idKeyConcept5=kcw5.id
            else:
                keyConcept5Act=KeyConcept.objects.create(name=word5,frequency=1)
                keyConcept5Act.activityNarrative.add(idActivityNarrative)
                keyConcept5Act.save()


            if serializerPersonCampaign.is_valid():
                return Response(serializerPersonCampaign.data, status=status.HTTP_201_CREATED)
            return Response( status=status.HTTP_400_BAD_REQUEST)


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





    