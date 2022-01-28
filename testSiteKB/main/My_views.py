from django.shortcuts import render
import requests
from main.models import Person
import datetime


dbarray = []


def about(request):
    today = datetime.date.today()

    if request.user.username:
        usrname = request.user.username
        orgname = Person.objects.get(operator=usrname).organisation
        site_org = Person.objects.get(operator=usrname).site_organis
    else:
        orgname = ''
        site_org = ''

    return render(
        request,
        'about.html',
        context={
            'organisation': orgname,
            'site_org': site_org,
            'today': today,
        }
    )


def index(request):
    today = datetime.date.today()

    if request.user.username:
        usrname = request.user.username
        orgname = Person.objects.get(operator=usrname).organisation
        site_org = Person.objects.get(operator=usrname).site_organis
    else:
        orgname = ''
        site_org = ''

    return render(
        request,
        'index.html',
        context={
            'organisation': orgname,
            'site_org': site_org,
            'today': today,
        }
    )


def blank_1(request):

    today = str(datetime.date.today())

    global dbarray
    poleName = ""
    polePlo = 0
    poleUdb = 0

    if request.user.username:
        usrname = request.user.username
        orgname = Person.objects.get(operator=usrname).organisation
        site_org = Person.objects.get(operator=usrname).site_organis
    else:
        orgname = ''
        site_org = ''

    if 'SaveButton' in request.POST:
        if 'poleName' in request.POST:
            poleName = request.POST['poleName']
        if 'polePlo' in request.POST:
            polePlo = request.POST['polePlo']
            if polePlo is None:
                polePlo = 0
            else:
                polePlo = int(polePlo, base=10)
        if 'poleUdb' in request.POST:
            poleUdb = request.POST['poleUdb']
            if poleUdb is None:
                poleUdb = 0
            else:
                poleUdb = int(poleUdb, base=10)

    if 'EraseButton' in request.POST:
        dbarray = []

    if poleName != '' and polePlo > 0:
        dbarray.append((poleName, polePlo, poleUdb))
        # print("Имя поля:" + poleName)
        # print("Площадь поля:" + str(polePlo))
        # print("Удобрений на поле:" + str(poleUdb))

    return render(
        request,
        'blank_1.html',
        context={
            'organisation': orgname,
            'site_org': site_org,
            'dbarray': dbarray,
            'today': today,
        }
    )

