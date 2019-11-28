from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from django.http import HttpResponse, JsonResponse
import json
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
TopicSerializer, 
KeyConceptSerializer,
UserSerializer,
#RoleCampaignSerializer,
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

from datetime import date,datetime




          


#Analitica

#Tener en cuenta rutas:
#os.getcwd()+'/../modelo_entrenado.pkl'
#os.getcwd()+'/../data/df_limpieza.xlsx'
from opcapp.analitica import clean_text,obtain_topics


@api_view(['GET'])
def predictTopic(request):
 
    text=request.query_params.get("text",None)

    topics_list=predict(text)

    
    data={
        "topics":topics_list
    }
    return JsonResponse(data)

def predict(text):
    data_list=clean_text(text)
    topics_list=obtain_topics(data_list)
    return topics_list



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
def gender(request):
    if request.method == "GET":
        genderList=Gender.objects.all()
        serializer=GenderSerializer(genderList, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def levelseducation(request):
    if request.method == "GET":
        hlEducationList=HigherLevelEducation.objects.filter()
        serializer=HigherLevelEducationSerializer(hlEducationList, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def leveleducation_list(request):
    if request.method == "GET":
        name=request.query_params.get('name', None)
        if name is not None:
            levelsEducationList=AchievedLevel.objects.filter(higherLevelEducation__name=name)
            serializer=AchievedLevelSerializer(levelsEducationList, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



      
@api_view(['GET'])
def states_list(request):
    if request.method == "GET":
        country=request.query_params.get('country', None)
        if country is not None:
            #countryAct=Country.objects.filter(name=country).first()
            statesList=State.objects.filter(country__name=country)
            serializer=StateSerializer(statesList, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



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

        campList=Campaign.objects.filter(startDate__lte=date.today(),endDate__gte=date.today(),isActive=True)
        serializer=CampaignSerializer(campList, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def notacampaigns_list(request):
    if request.method == "GET":
        campList=Campaign.objects.filter(isActive=False)
        serializer=CampaignSerializer(campList, many=True)
        return Response(serializer.data)



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
        corregimiento=request.query_params.get('corregimiento', None)
        state=request.query_params.get('state', None)
        if id is not None:

            numPeople=None
            flag=False
            if comuna is not None:
                flag=True
                numPeople=PersonCampaign.objects.filter(campaign__id=id).filter(neighborhoodVeredaActual__comunaCorregimiento__zone__zoneType='Urbana', neighborhoodVeredaActual__comunaCorregimiento__id=comuna).count()
           
            elif corregimiento is not None:
                flag=True
                numPeople=PersonCampaign.objects.filter(campaign__id=id, neighborhoodVeredaActual__comunaCorregimiento__id=corregimiento).count()
           
            elif state is not None:
                flag=True
                numPeople=PersonCampaign.objects.filter(campaign__id=id, neighborhoodVeredaActual__comunaCorregimiento__city__state__id=city).count()
           


            if flag :
                data = {
                "frequency": numPeople
                }
            
                return JsonResponse(data)
            else :
                return Response( status=status.HTTP_404_NOT_FOUND)
        else :
            return Response( status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def narratives_list(request):
    if request.method == "GET":

        narrativesList=ActivityNarrative.objects.all()
        serializer=ActivityNarrativeSerializer(narrativesList, many=True)
        return Response(serializer.data)
    else :
        return Response( status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def narratives_campaign_list(request):
    if request.method == "GET":
        id=request.query_params.get('id', None)
        if id is not None:

            narrativesList=ActivityNarrative.objects.filter(campaign__id=id)
            serializer=ActivityNarrativeSerializer(narrativesList, many=True)
            return Response(serializer.data)
        else :
            return Response( status=status.HTTP_404_NOT_FOUND)

#--------------------------------------------REMOVE-----------------------------
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


#--------------------------------------------REMOVE-----------------------------
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


@api_view(['POST','PUT'])
@permission_classes([IsAuthenticated])
def save_campaign(request):
    startDate=request.data.get('start_date',None)
    endDate=request.data.get('end_date',None)
    description=request.data.get('description',None)
    title=request.data.get('title',None)
    narrativesGoal=request.data.get('narratives_goal',None)
    accumulatedNarratives=request.data.get('accumulated_narratives',None)
    isActive=request.data.get('is_active',None)

    #Tengo que formatearlo para comparar las fechas
    endDateFormatted=datetime.strptime(endDate, '%Y-%m-%d').date()

    validDate=True if endDateFormatted>date.today() else False

    #id de la campaign para el put
    id=request.data.get('id',None)

    if validDate and startDate is not None and endDate is not None and description is not None and title is not None and narrativesGoal is not None and isActive is not None:
        
        if request.method == "POST"  and accumulatedNarratives is not None:
            
            person=Person.objects.get(user=request.user.id)
            print(person.id)
            data={
                "person":person.id,
                "startDate":startDate,
                "endDate":endDate,
                "description":description,
                "title":title,
                "narrativesGoal":narrativesGoal,
                "accumulatedNarratives":accumulatedNarratives,
                "isActive":isActive,
                
            }
            
            campaignSerializer=CampaignSerializer(data=data)

            if campaignSerializer.is_valid():
                campaignSerializer.save()
                return Response(campaignSerializer.data, status=status.HTTP_200_OK)
            else:
                return Response( status=status.HTTP_400_BAD_REQUEST)

        elif request.method =="PUT" and id is not None:

            person=Person.objects.get(user=request.user.id)
            campaign=Campaign.objects.filter(id=id, person=person.id)
            if campaign:
                campaign.update(startDate=startDate,endDate=endDate, description=description, title=title,narrativesGoal=narrativesGoal,isActive=isActive)
                serializer=CampaignSerializer(campaign.first())
                return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response( status=status.HTTP_404_NOT_FOUND)
        else:
            return Response( status=status.HTTP_404_NOT_FOUND)
    else:
        return Response( status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def city_person(request):
    if request.method == "GET":

        person=Person.objects.get(user=request.user.id)
        neighVer=NeighborhoodVereda.objects.get(id=person.neighborhoodVeredaActual.id)
        comunaCorr=ComunaCorregimiento.objects.get(id=neighVer.comunaCorregimiento.id)
        city=City.objects.get(id=comunaCorr.city.id)

        data = {
                "city_name": city.name
            }
            
        return JsonResponse(data)
    else:
        return Response( status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def campaigns_person(request):
    if request.method == "GET":

        person=Person.objects.get(user=request.user.id)

        personCampaignList=PersonCampaign.objects.values_list('campaign', flat=True).filter(person__id=person.id)
        print(personCampaignList)
        campaignList=None
        for i in personCampaignList:
            if campaignList is None:
                campaignList=Campaign.objects.filter(id=i)
            else:
                campaignList=campaignList.union(Campaign.objects.filter(id=i))

        #campaignList=Campaign.objects.filter(person=person.id)
        serializer=CampaignSerializer(campaignList, many=True)
       
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response( status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def campaigns_created_person(request):
    if request.method == "GET":

        person=Person.objects.get(user=request.user.id)
        campaignList=Campaign.objects.filter(person=person.id)
        serializer=CampaignSerializer(campaignList, many=True)

       
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response( status=status.HTTP_400_BAD_REQUEST)


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
        achievedLevel=str(person.achievedLevel.id)+"/"+person.achievedLevel.name 
        higherEd=str(person.achievedLevel.higherLevelEducation.id)+"/"+ person.achievedLevel.higherLevelEducation.name
        neighborhoodVereda=str(person.neighborhoodVeredaActual.id)+"/"+person.neighborhoodVeredaActual.name
        comunaCorregimiento=str(person.neighborhoodVeredaActual.comunaCorregimiento.id)+"/"+person.neighborhoodVeredaActual.comunaCorregimiento.name
        city=str(person.neighborhoodVeredaActual.comunaCorregimiento.city.id)+"/"+person.neighborhoodVeredaActual.comunaCorregimiento.city.name
        state=str(person.neighborhoodVeredaActual.comunaCorregimiento.city.state.id)+"/"+person.neighborhoodVeredaActual.comunaCorregimiento.city.state.name
        #neighborhoodVeredaSource=person.neighborhoodVeredaSource.name+"/"+person.neighborhoodVeredaSource.comunaCorregimiento.name+"/"+person.neighborhoodVeredaSource.comunaCorregimiento.city.name+"/"+person.neighborhoodVeredaSource.comunaCorregimiento.city.state.name
        zoneActual=str(person.neighborhoodVeredaActual.zone.id)+"/"+person.neighborhoodVeredaActual.zone.zoneType
        data = {
            #'phoneNumber':person.phoneNumber,
            'achievedLevel':achievedLevel,
            'higherEd':higherEd,
            'zoneActual':zoneActual,
            'neighborhoodVeredaActual':neighborhoodVereda,
            'comunaCorregimiento':comunaCorregimiento,
            'city':city,
            'state':state
            }
            
        return JsonResponse(data,status=status.HTTP_200_OK)

    elif request.method =="PUT":
       # phoneNumber=request.data.get('phoneNumber')
        achievedLevel=request.data.get('achievedLevel', None)
        #birthdate=request.data.get('birthdate')
        neighborhoodVeredaActual=request.data.get('neighborhoodVeredaActual', None)
        cityActual=request.data.get('cityActual',None)
       # neighborhoodVeredaSource=request.data.get('neighborhoodVeredaSource')

        person=Person.objects.filter(user__id=request.user.id)
        #person.phoneNumber=phoneNumber

        al=AchievedLevel.objects.get(id=achievedLevel)

        person.update(achievedLevel=al)

        if neighborhoodVeredaActual!=0:
            nvActual=NeighborhoodVereda.objects.get(id=neighborhoodVeredaActual)
            person.update(neighborhoodVeredaActual=nvActual)
        elif cityActual !=0 :

            nvActualOutsideCali=NeighborhoodVereda.objects.filter(comunaCorregimiento__city__id=cityActual).first()
            person.update(neighborhoodVeredaActual=nvActualOutsideCali)


        serializer=PersonSerializer(person.first())
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    else:
        return Response( status=status.HTTP_400_BAD_REQUEST)


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


        if narrative is not None and word1 is not None and word2 is not None and word3 is not None and word4 is not None and word5 is not None and campaign is not None: 
            idUser=request.user.id
            person=Person.objects.get(user=idUser)
            #roleUserId=RoleCampaign.objects.get(name="Invitado").id
            #si el usuario ya ha participado en esta campaña
            isAlreadyCreated=PersonCampaign.objects.filter(person=person.id,campaign=campaign)
            if isAlreadyCreated:
                return Response({"status_code": 409, "detail": "User already exists"},status=409)

            dataPersonCampaign={
                #    person=models.ForeignKey(Person, on_delete=models.CASCADE)
                #   roleCampaign=models.ForeignKey(RoleCampaign, on_delete=models.CASCADE)
                    'person':person.id, 
                    #'roleCampaign':roleUserId, 
                    'campaign':campaign,
                    'achievedLevel':person.achievedLevel.id,
                    'gender':person.gender.id,
                    'neighborhoodVeredaSource':person.neighborhoodVeredaSource.id,
                    'neighborhoodVeredaActual':person.neighborhoodVeredaActual.id,
                
            }



            serializerPersonCampaign=PersonCampaignSerializer(data=dataPersonCampaign)
            if serializerPersonCampaign.is_valid():
                personCampaignAct= serializerPersonCampaign.save()

                idPersonCampaign=personCampaignAct.id

                #Predict
                topics_list=predict(narrative)
                topicPrimary=topics_list[0]
                topicSecondary=topics_list[1]
                idTPrimary=Topic.objects.filter(concepts=topicPrimary).first().id
                idTSecondary=Topic.objects.filter(concepts=topicSecondary).first().id

                dataActivityNarrative={
                    "text":narrative,
                    "campaign":campaign,
                    "personCampaign":idPersonCampaign,
                    "topicPrimary":idTPrimary,
                    "topicSecondary":idTSecondary
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
            else:
                return Response( status=status.HTTP_400_BAD_REQUEST)
        else:
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

        if age is not None and campaign is not None and gender is not None and level is not None and higherEducation is not None and currentZone is not None and currentState is not None and currentCity is not None and currentComuna is not None and currentNeighborhood is not None and currentCorregimiento is not None and currentVereda is not None and originZone is not None and originState is not None and originCity is not None and originComuna is not None and originNeighborhood is not None and originCorregimiento is not None and originVereda is not None and narrative is not None and word1 is not None and word2 is not None and word3 is not None and word4 is not None and word5 is not None :
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
                currentLevel3=NeighborhoodVereda.objects.filter(comunaCorregimiento__city__id=currentCity ).first().id


            if originNeighborhood == 0 and originVereda == 0 :
                originLevel3=NeighborhoodVereda.objects.filter(comunaCorregimiento__city__id=originCity).first().id


        # print(currentLevel3)
        # print(originLevel3)

            idUser=None

            if email is not None and password is not None:

                if User.objects.filter(username=email).exists() :

                    return Response({"status_code": 409, "detail": "User already exists"},status=409)

                else:
                    userAct = User.objects.create_user(username=email,
                                        email=email,
                                        password=password)

                    userAct.save()

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
             #   roleCampaignId=RoleCampaign.objects.filter(name="Invitado").first().id

            # print(serializerPerson.data)

                idPerson=personAct.id

                dataPersonCampaign={
                #    person=models.ForeignKey(Person, on_delete=models.CASCADE)
                #   roleCampaign=models.ForeignKey(RoleCampaign, on_delete=models.CASCADE)
                    'person':idPerson, 
                  #  'roleCampaign':roleCampaignId, 
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

                #Predict
                topics_list=predict(narrative)
                topicPrimary=topics_list[0]
                topicSecondary=topics_list[1]
                idTPrimary=Topic.objects.filter(concepts=topicPrimary).first().id
                idTSecondary=Topic.objects.filter(concepts=topicSecondary).first().id

                dataActivityNarrative={
                    "text":narrative,
                    "campaign":campaign,
                    "personCampaign":idPersonCampaign,
                    "topicPrimary":idTPrimary,
                    "topicSecondary":idTSecondary
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
        else:
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

  
@api_view(['GET'])
def topic_person_campaign(request):

    if request.method=="GET":
        id=request.query_params.get('id', None)
        if id is not None:
            

            aNarrative=ActivityNarrative.objects.get(personCampaign=id)
            topicPrimaryId=aNarrative.topicPrimary.id
            topicSecondaryId=aNarrative.topicSecondary.id
            topicPrimary=Topic.objects.get(id=topicPrimaryId).concepts
            topicSecondary=Topic.objects.get(id=topicSecondaryId).concepts

            data={
                "id_primary":topicPrimaryId,
                "id_secondary":topicSecondaryId,
                "topic_primary":topicPrimary,
                "topic_secondary":topicSecondary
            }
            return Response(data=data, status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def obtain_campaign(request):

    if request.method=="GET":
        id=request.query_params.get('id', None)
        if id is not None:
            

            campaign=Campaign.objects.get(id=id)

            serializer=CampaignSerializer(campaign)
         
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def topic_list(request):

    if request.method=="GET":
        topics=Topic.objects.all()

        serializer=TopicSerializer(topics, many=True)
         
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def role_user(request):

    if request.method=="GET":
        person=Person.objects.filter(id=request.user.id).first()

        data={
            "role_user":person.roleUser.id
        }

        return JsonResponse(data)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def acampaigns_person_list(request):
    if request.method == "GET":
        person=Person.objects.filter(id=request.user.id).first()
        campList=Campaign.objects.filter(startDate__lte=date.today(),endDate__gte=date.today(),isActive=True)

        person=Person.objects.get(user=request.user.id)

        personCampaignList=PersonCampaign.objects.values_list('campaign', flat=True).filter(person__id=person.id)
        print(personCampaignList)
 
        for i in personCampaignList:
            campList=campList.exclude(id=i)

        serializer=CampaignSerializer(campList, many=True)

        return Response(serializer.data)

        
@api_view(['GET'])
def obtain_percentage(request):
    if request.method=="GET":
        
        gender=request.query_params.get('gender', None)
        age=request.query_params.get('age', None)
        education=request.query_params.get('education', None)
        idCampaign=request.query_params.get('id_campaign', None)
        topicPrimary=request.query_params.get('topic_primary', None)
        topicSecondary=request.query_params.get('topic_secondary', None)
        typeFilter=request.query_params.get('type_filter',None)
        
        #por tiempo
        minDate=request.query_params.get('min_date',None)
        maxDate=request.query_params.get('max_date',None)
        if age is not None and age!=0:

            if age == "primera infancia":
                primeraInfanciaMin=calculate_mindate(0)
                primeraInfanciaMax=calculate_mindate(5)
            elif age == "infancia":
                infanciaMin=calculate_mindate(6)
                infanciaMax=calculate_mindate(11)
            elif age == "adolescencia":
                adolescenciaMin=calculate_mindate(12)
                adolescenciaMax=calculate_mindate(18)
            elif age == "juventud":
                juventudMin=calculate_mindate(19)
                juventudMax=calculate_mindate(26)
            elif age == "adultez":
                adultezMin=calculate_mindate(27)
                adultezMax=calculate_mindate(59)
            elif age == "vejez":
                vejez=calculate_mindate(60)


        idList=[]
        print(typeFilter)
        if typeFilter == 'comuna':
            idList=list(range(1,23))
        elif typeFilter == 'corregimiento':
            idList=list(range(23,38))

        elif typeFilter == 'state':
            idList=State.objects.values_list('id', flat=True)
            print("entr")

        print(idList)
        dictWithFilters={}
        for i in idList:
            if (typeFilter == 'comuna') or (typeFilter == 'corregimiento'):
                personCampaignAct=PersonCampaign.objects.filter(neighborhoodVeredaActual__comunaCorregimiento=i)
            elif typeFilter == 'state':
                personCampaignAct=PersonCampaign.objects.filter(neighborhoodVeredaActual__comunaCorregimiento__city__state=i)
                
            
            
            #Por si es un filtro en una campaña
            if idCampaign is not None and idCampaign!=0:
                personCampaignAct=personCampaignAct.filter(campaign__id=idCampaign)

            #Las 3 posibles de siempre
            if gender is not None and gender!=0:
                personCampaignAct=personCampaignAct.filter(gender__name=gender)

            #por tiempo
            if minDate is not None:
                personCampaignAct=personCampaignAct.filter(campaign__startDate__gte=minDate)

            if maxDate is not None:
                personCampaignAct=personCampaignAct.filter(campaign__endDate__lte=maxDate)


            if age is not None and age!=0:



                if age == "primera Infancia":

                    personCampaignAct=personCampaignAct.filter( person__birthdate__lte=primeraInfanciaMin, person__birthdate__gte=primeraInfanciaMax)
                elif age == "infancia":

                    personCampaignAct=personCampaignAct.filter( person__birthdate__lte=infanciaMin, person__birthdate__gte=infanciaMax)
                elif age == "adolescencia":

                    personCampaignAct=personCampaignAct.filter( person__birthdate__lte=adolescenciaMin, person__birthdate__gte=adolescenciaMax)
                elif age == "juventud":

                    personCampaignAct=personCampaignAct.filter( person__birthdate__lte=juventudMin, person__birthdate__gte=juventudMax)
                elif age == "adultez":

                    personCampaignAct=personCampaignAct.filter( person__birthdate__lte=adultezMin, person__birthdate__gte=adultezMax)
                elif age == "vejez":

                    personCampaignAct=personCampaignAct.filter( person__birthdate__lte=vejez)





            if education is not None and education!=0:
                personCampaignAct=personCampaignAct.filter(achievedLevel__higherLevelEducation__name=education)

            #Por si es un filtro en la visualiza general
            if topicPrimary is not None and topicPrimary!=0:
                personCampaignAct=personCampaignAct.filter(activitynarrative__topicPrimary__id=topicPrimary)
            if topicSecondary is not None and topicSecondary!=0:
                personCampaignAct=personCampaignAct.filter(activitynarrative__topicSecondary__id=topicSecondary)

            dictWithFilters[i]=personCampaignAct.count()

        if dictWithFilters:
            dictWithFilters=create_percentages(dictWithFilters)

            return JsonResponse(dictWithFilters, safe=False)
        else:
           return Response(status=status.HTTP_404_NOT_FOUND) 
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


def create_percentages(dictWithFilters):

    maxIndex=max(dictWithFilters, key=dictWithFilters.get)
    maxValue=dictWithFilters[maxIndex]
    
    if maxValue!=0:
        for key, value in dictWithFilters.items():
            dictWithFilters[key]=float("{0:.2f}".format((value)/maxValue))
    else:
        for key, value in dictWithFilters.items():
            dictWithFilters[key]=float("{0:.2f}".format(0))
    return dictWithFilters



    

@api_view(['GET'])
def obtain_opendata(request):
    if request.method=="GET":

        #edad
        #genero
        #level
        #
        #
        #

        person_campaign_list=PersonCampaign.objects.all()
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



#visualizacion

@api_view(['GET'])
def fivekeywords_list(request):
    if request.method == "GET":
       #if 'city' or 'zone'\ are not informed, the values ​​are None.
        id=request.query_params.get('id', None)

        if id is not None:
            conceptsCampaignList=KeyConcept.objects.filter(activityNarrative__campaign__id=id).distinct().order_by('frequency').reverse()[:5]
           
            serializer=KeyConceptSerializer(conceptsCampaignList, many=True)
            return Response(serializer.data)
        else:
            return Response( status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def education_visualization_list(request):
    if request.method == "GET":
       #if 'city' or 'zone'\ are not informed, the values ​​are None.
        
        comuna=request.query_params.get('comuna', None)
        corregimiento=request.query_params.get('corregimiento', None)
        state=request.query_params.get('state', None)
        
        id=request.query_params.get('id', None)
        topic=request.query_params.get('topic',None)
        topicType=request.query_params.get('topic_type',None)


        primaria=PersonCampaign.objects.filter(achievedLevel__higherLevelEducation__id=1 )
        secundaria=PersonCampaign.objects.filter( achievedLevel__higherLevelEducation__id=2)
        tyt=PersonCampaign.objects.filter( achievedLevel__higherLevelEducation__id=3)
        universitaria=PersonCampaign.objects.filter( achievedLevel__higherLevelEducation__id=4)
        postgrado=PersonCampaign.objects.filter( achievedLevel__higherLevelEducation__id=5)

        if id is not None:
            primaria=primaria.filter(campaign__id=id)
            secundaria=secundaria.filter(campaign__id=id)
            tyt=tyt.filter(campaign__id=id)
            universitaria=universitaria.filter(campaign__id=id)
            postgrado=postgrado.filter(campaign__id=id)
                

           

        if topic is not None:
            if topicType is not None and topicType=="Primario":
                primaria=primaria.filter(activitynarrative__topicPrimary=topic)
                secundaria=secundaria.filter(activitynarrative__topicPrimary=topic)
                tyt=tyt.filter(activitynarrative__topicPrimary=topic)
                universitaria=universitaria.filter(activitynarrative__topicPrimary=topic)
                postgrado=postgrado.filter(activitynarrative__topicPrimary=topic)
            
            elif topicType is not None and topicType=="Secundario":
                primaria=primaria.filter(activitynarrative__topicSecondary=topic)
                secundaria=secundaria.filter(activitynarrative__topicSecondary=topic)
                tyt=tyt.filter(activitynarrative__topicSecondary=topic)
                universitaria=universitaria.filter(activitynarrative__topicSecondary=topic)
                postgrado=postgrado.filter(activitynarrative__topicSecondary=topic)


        if comuna is not None:
            
            primaria=primaria.filter( neighborhoodVeredaActual__comunaCorregimiento__id=comuna)
            secundaria=secundaria.filter( neighborhoodVeredaActual__comunaCorregimiento__id=comuna)
            tyt=tyt.filter( neighborhoodVeredaActual__comunaCorregimiento__id=comuna)
            universitaria=universitaria.filter( neighborhoodVeredaActual__comunaCorregimiento__id=comuna)
            postgrado=postgrado.filter( neighborhoodVeredaActual__comunaCorregimiento__id=comuna)
            
        elif corregimiento is not None:
            
            primaria=primaria.filter( neighborhoodVeredaActual__comunaCorregimiento__id=corregimiento)
            secundaria=secundaria.filter(neighborhoodVeredaActual__comunaCorregimiento__id=corregimiento)
            tyt=tyt.filter(neighborhoodVeredaActual__comunaCorregimiento__id=corregimiento)
            universitaria=universitaria.filter( neighborhoodVeredaActual__comunaCorregimiento__id=corregimiento)
            postgrado=postgrado.filter( neighborhoodVeredaActual__comunaCorregimiento__id=corregimiento)
            
        elif state is not None:
            
            primaria=primaria.filter(neighborhoodVeredaActual__comunaCorregimiento__city__state__id=state)
            secundaria=secundaria.filter(neighborhoodVeredaActual__comunaCorregimiento__city__state__id=state)
            tyt=tyt.filter(neighborhoodVeredaActual__comunaCorregimiento__city__state__id=state)
            universitaria=universitaria.filter(neighborhoodVeredaActual__comunaCorregimiento__city__state__id=state)
            postgrado=postgrado.filter(neighborhoodVeredaActual__comunaCorregimiento__city__state__id=state)

           
        data = {
        "primaria": primaria.count(),
        "secundaria":secundaria.count(),
        "tyt":tyt.count(),
        "universitaria":universitaria.count(),
        "postgrado":postgrado.count(),
        }
    
        return JsonResponse(data)
    else :
        return Response( status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def gender_list(request):
    if request.method == "GET":
       #if 'city' or 'zone'\ are not informed, the values ​​are None.

        comuna=request.query_params.get('comuna', None)
        corregimiento=request.query_params.get('corregimiento', None)
        state=request.query_params.get('state', None)

        id=request.query_params.get('id', None)
        topic=request.query_params.get('topic',None)
        topicType=request.query_params.get('topic_type',None)



        numMasculino=PersonCampaign.objects.filter(gender__typeGender='Masculino')
        numFemenino=PersonCampaign.objects.filter(gender__typeGender='Femenino')
        numIntersexual=PersonCampaign.objects.filter(gender__typeGender='Intersexual')


        if id is not None:
            numMasculino=numMasculino.filter(campaign__id=id)
            numFemenino=numFemenino.filter(campaign__id=id)
            numIntersexual=numIntersexual.filter(campaign__id=id)
                

        if topic is not None:
            if topicType is not None and topicType=="Primario":
                numMasculino=numMasculino.filter(activitynarrative__topicPrimary=topic)
                numFemenino=numFemenino.filter(activitynarrative__topicPrimary=topic)
                numIntersexual=numIntersexual.filter(activitynarrative__topicPrimary=topic)

            
            elif topicType is not None and topicType=="Secundario":
                numMasculino=numMasculino.filter(activitynarrative__topicSecondary=topic)
                numFemenino=numFemenino.filter(activitynarrative__topicSecondary=topic)
                numIntersexual=numIntersexual.filter(activitynarrative__topicSecondary=topic)





        if comuna is not None:

            numMasculino=numMasculino.filter( neighborhoodVeredaActual__comunaCorregimiento__zone__zoneType='Urbana', neighborhoodVeredaActual__comunaCorregimiento__id=comuna)
            numFemenino=numFemenino.filter( neighborhoodVeredaActual__comunaCorregimiento__zone__zoneType='Urbana', neighborhoodVeredaActual__comunaCorregimiento__id=comuna)
            numIntersexual=numIntersexual.filter( neighborhoodVeredaActual__comunaCorregimiento__zone__zoneType='Urbana', neighborhoodVeredaActual__comunaCorregimiento__id=comuna)
        
        elif corregimiento is not None:

            numMasculino=PersonCampaign.objects.filter(  neighborhoodVeredaActual__comunaCorregimiento__id=corregimiento)
            numFemenino=PersonCampaign.objects.filter(  neighborhoodVeredaActual__comunaCorregimiento__id=corregimiento)
            numIntersexual=numIntersexual.filter( neighborhoodVeredaActual__comunaCorregimiento__id=corregimiento)

        elif state is not None:

            numMasculino=numMasculino.filter( neighborhoodVeredaActual__comunaCorregimiento__city__state__id=state)
            numFemenino=numFemenino.filter( neighborhoodVeredaActual__comunaCorregimiento__city__state__id=state)
            numIntersexual=numIntersexual.filter(  neighborhoodVeredaActual__comunaCorregimiento__id=corregimiento)

        data = {
        "men": numMasculino.count(),
        "women":numFemenino.count(),
        "intersexual":numIntersexual.count()
        }
            
        return JsonResponse(data)

    else :
        return Response( status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def age_range_list(request):
    if request.method == "GET":
       #if 'city' or 'zone'\ are not informed, the values ​​are None.

        comuna=request.query_params.get('comuna', None)
        corregimiento=request.query_params.get('corregimiento', None)
        state=request.query_params.get('state', None)

        id=request.query_params.get('id', None)
        topic=request.query_params.get('topic',None)
        topicType=request.query_params.get('topic_type',None)



        #Ages
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



        primeraInfanciaList=PersonCampaign.objects.filter(person__birthdate__lte=primeraInfanciaMin, person__birthdate__gte=primeraInfanciaMax)
        infanciaList=PersonCampaign.objects.filter(person__birthdate__lte=infanciaMin, person__birthdate__gte=infanciaMax )
        adolescenciaList=PersonCampaign.objects.filter(person__birthdate__lte=adolescenciaMin, person__birthdate__gte=adolescenciaMax)
        juventudList=PersonCampaign.objects.filter(person__birthdate__lte=juventudMin, person__birthdate__gte=juventudMax)
        adultezList=PersonCampaign.objects.filter(person__birthdate__lte=adultezMin, person__birthdate__gte=adultezMax)
        vejezList=PersonCampaign.objects.filter(person__birthdate__lte=vejez)

        if id is not None:
            primeraInfanciaList=primeraInfanciaList.filter(campaign__id=id)
            infanciaList=infanciaList.filter(campaign__id=id)
            adolescenciaList=adolescenciaList.filter(campaign__id=id)
            juventudList=juventudList.filter(campaign__id=id)
            adultezList=adultezList.filter(campaign__id=id)
            vejezList=vejezList.filter(campaign__id=id)


        
        if topic is not None:
            if topicType is not None and topicType=="Primario":

                primeraInfanciaList=primeraInfanciaList.filter(activitynarrative__topicPrimary=topic)
                infanciaList=infanciaList.filter(activitynarrative__topicPrimary=topic)
                adolescenciaList=adolescenciaList.filter(activitynarrative__topicPrimary=topic)
                juventudList=juventudList.filter(activitynarrative__topicPrimary=topic)
                adultezList=adultezList.filter(activitynarrative__topicPrimary=topic)
                vejezList=vejezList.filter(activitynarrative__topicPrimary=topic)


            elif topicType is not None and topicType=="Secundario":

                primeraInfanciaList=primeraInfanciaList.filter(activitynarrative__topicSecondary=topic)
                infanciaList=infanciaList.filter(activitynarrative__topicSecondary=topic)
                adolescenciaList=adolescenciaList.filter(activitynarrative__topicSecondary=topic)
                juventudList=juventudList.filter(activitynarrative__topicSecondary=topic)
                adultezList=adultezList.filter(activitynarrative__topicSecondary=topic)
                vejezList=vejezList.filter(activitynarrative__topicSecondary=topic)








        if comuna is not None:
    
            primeraInfanciaList=primeraInfanciaList.filter( neighborhoodVeredaActual__comunaCorregimiento__id=comuna)
            infanciaList=infanciaList.filter(neighborhoodVeredaActual__comunaCorregimiento__id=comuna)
            adolescenciaList=adolescenciaList.filter(neighborhoodVeredaActual__comunaCorregimiento__id=comuna)
            juventudList=juventudList.filter(neighborhoodVeredaActual__comunaCorregimiento__id=comuna)
            adultezList=adultezList.filter( neighborhoodVeredaActual__comunaCorregimiento__id=comuna)
            vejezList=vejezList.filter( neighborhoodVeredaActual__comunaCorregimiento__id=comuna)

        
        elif corregimiento is not None:
            
            primeraInfanciaList=primeraInfanciaList.filter(neighborhoodVeredaActual__comunaCorregimiento__id=corregimiento)
            infanciaList=infanciaList.filter(neighborhoodVeredaActual__comunaCorregimiento__id=corregimiento)
            adolescenciaList=adolescenciaList.filter(neighborhoodVeredaActual__comunaCorregimiento__id=corregimiento)
            juventudList=juventudList.filter( neighborhoodVeredaActual__comunaCorregimiento__id=corregimiento)
            adultezList=adultezListfilter(neighborhoodVeredaActual__comunaCorregimiento__id=corregimiento)
            vejezList=vejezList.filter(neighborhoodVeredaActual__comunaCorregimiento__id=corregimiento)
        elif state is not None:
        
            primeraInfanciaList=primeraInfanciaList.filter( neighborhoodVeredaActual__comunaCorregimiento__city__state__id=state)
            infanciaList=infanciaList.filter(neighborhoodVeredaActual__comunaCorregimiento__city__state__id=state)
            adolescenciaList=adolescenciaList.filter( neighborhoodVeredaActual__comunaCorregimiento__city__state__id=state)
            juventudList=juventudList.filter(neighborhoodVeredaActual__comunaCorregimiento__city__state__id=state)
            adultezList=adultezList.filter( neighborhoodVeredaActual__comunaCorregimiento__city__state__id=state)
            vejezList=vejezList.filter(neighborhoodVeredaActual__comunaCorregimiento__city__state__id=state)



        data = {
            'primeraInfancia':primeraInfanciaList.count(),
            'infancia':infanciaList.count(),
            'adolescencia':adolescenciaList.count(),
            'juventud':juventudList.count(),
            'adultez':adultezList.count(),
            'vejez':vejezList.count(),

        }
        return JsonResponse(data)

    else :
        return Response( status=status.HTTP_404_NOT_FOUND)
