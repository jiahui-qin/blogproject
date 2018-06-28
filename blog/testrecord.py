from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect  
from django.http import HttpResponse
from django.shortcuts import render
from .models import testrecord, crudeex, bact,cpd
from django.db.models import Q
from django.utils import timezone
from django.http import JsonResponse
import json
from django.core import serializers


def recordindex(request, msg = -1):
    lists = testrecord.objects.all()
    num = len(lists) 
    return render(request, 'blog/record.html', {'tests' : lists, 'msg' : msg, 'num' : num} )

def upload(request):
    if request.method == "GET":
        try:
            testtype = request.GET.get('testtype') #或者改成两个可选项？粗提物或者化合物
            samst = request.GET.get('samst') #盒序号
            samend = request.GET.get('samend') #样品起序号
            solvent = request.GET.get('solvent') #样品终序号
            mass = request.GET.get('mass') #样品名
            volume = request.GET.get('volume') #溶剂
            conc = request.GET.get('conc')#重量，单位miug
            testconc = request.GET.get('testconc') #体积单位niuL
            department = request.GET.get('department') #浓度 单位(mg/mL)
            comment = request.GET.get('comment') #测试浓度 单位(miug/mL)
            if request.GET.get('fromcru'):
                id = request.GET.get('fromcru')
                fromcru = crudeex.objects.get(id=fromcru)
            else:
                id = request.GET.get('frombact')
                frombact = bact.objects.get(id=frombact)
            info = {
                'testtype' : testtype, 
                'samst' : samst, 
                'samend' : samend, 
                'solvent' : solvent, 
                'mass' : mass,
                'volume' : volume, 
                'conc' : conc, 
                'testconc' : testconc, 
                'department' : department,
                'comment' : comment,
                'provider': request.user
                'fromcru' : fromcru
                'frombact' : frombact
            }        
            testrecord.objects.create(**info)
            return recordindex(request, msg = 0) #msg = 0代表正常插入
        except:
            return recordindex(request, msg = 1) #msg = 1 代表插入失败

def recdel(request):
    if request.method == "GET":
        try:
            id = request.GET.get('id')
            testrecord.objects.get(id = id).delete()
            return recordindex(request, msg = 0)
        except:
            return recordindex(request, msg = 1)


def recalter(request):
    if request.method == 'GET':
        try:
            id = request.GET.get('id')
            testtype = request.GET.get('testtype') #或者改成两个可选项？粗提物或者化合物
            samst = request.GET.get('samst') #盒序号
            samend = request.GET.get('samend') #样品起序号
            solvent = request.GET.get('solvent') #样品终序号
            mass = request.GET.get('mass') #样品名
            volume = request.GET.get('volume') #溶剂
            conc = request.GET.get('conc')#重量，单位miug
            testconc = request.GET.get('testconc') #体积单位niuL
            department = request.GET.get('department') #浓度 单位(mg/mL)
            comment = request.GET.get('comment') #测试浓度 单位(miug/mL)
            if request.GET.get('fromcru'):
                id = request.GET.get('fromcru')
                fromcru = crudeex.objects.get(id=fromcru)
            else:
                id = request.GET.get('frombact')
                frombact = bact.objects.get(id=frombact)
            infos = {
                'testtype' : testtype, 
                'samst' : samst, 
                'samend' : samend, 
                'solvent' : solvent, 
                'mass' : mass,
                'volume' : volume, 
                'conc' : conc, 
                'testconc' : testconc, 
                'department' : department,
                'comment' : comment,
                'provider': request.user
                'fromcru' : fromcru
                'frombact' : frombact
            }
            testrecord.objects.select_for_update().filter(id = id).update(**infos)
            return recordindex(request, msg = 0)
        except:
            return recordindex(request, msg = 1)