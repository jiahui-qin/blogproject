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
import os
import csv
from django.core.urlresolvers import reverse  
from django.shortcuts import redirect  

@login_required
def recordindex(request, msg = -1,err = []):
    lists = testrecord.objects.all()
    num = len(lists) 
    return render(request, 'blog/record.html', {'tests' : lists, 'msg' : msg, 'num' : num, 'err' : err} )

def upload(request):
    if request.method == "GET":
        try:
            cpdid = request.GET.get('fromcpd')
            cruid = request.GET.get('fromcru')
            testtype = request.GET.get('testtype') #或者改成两个可选项？粗提物或者化合物
            solvent = request.GET.get('solvent') 
            mass = request.GET.get('mass') 
            volume = request.GET.get('volume') 
            conc = request.GET.get('conc')
            testconc = request.GET.get('testconc') #
            department = request.GET.get('department') #
            batch = request.GET.get('batch')#送测批次
            comment = request.GET.get('comment') #
            info = {
                'testtype' : testtype, 
                'solvent' : solvent, 
                'mass' : mass,
                'volume' : volume, 
                'conc' : conc, 
                'testconc' : testconc, 
                'department' : department,
                'comment' : comment,
                'batch' : batch,
                'provider': request.user,
                }
            if cruid:
                id = request.GET.get('fromcru')
                fromcru = crudeex.objects.get(id=cruid)
                info['fromcru'] = fromcru
            else:
                id = request.GET.get('fromcpd')
                fromcpd = cpd.objects.get(id=cpdid)
                info['fromcpd'] = fromcpd
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
            #testtype = request.GET.get('testtype') #或者改成两个可选项？粗提物或者化合物
            solvent = request.GET.get('solvent') #样品终序号
            mass = request.GET.get('mass') #样品名
            volume = request.GET.get('volume') #溶剂
            conc = request.GET.get('conc')#重量，单位miug
            testconc = request.GET.get('testconc') #体积单位niuL
            batch = request.GET.get('batch')#送测批次
            department = request.GET.get('department') #浓度 单位(mg/mL)
            comment = request.GET.get('comment') #测试浓度 单位(miug/mL)
            info = {
                'solvent' : solvent, 
                'mass' : mass,
                'volume' : volume, 
                'conc' : conc, 
                'testconc' : testconc, 
                'department' : department,
                'comment' : comment,
                'batch' : batch,
                'provider': request.user,
                }

            ##if testtype == "粗提物" :
            ##    id = request.GET.get('fromcru')
            ##    fromcru = crudeex.objects.get(id=cruid)
            ##    info['fromcru'] = fromcru
            ##else:
            ##    id = request.GET.get('fromcpd')
            ##    fromcpd = cpd.objects.get(id=cpdid)
            ##    info['fromcpd'] = fromcpd
            testrecord.objects.select_for_update().filter(id = id).update(**info)
            return recordindex(request, msg = 0)
        except:
            return recordindex(request, msg = 1)

def batchalter(request):
    if request.method == 'GET':
        try:
            batch = request.GET.get('batch')
            solvent = request.GET.get('solvent')
            mass = request.GET.get('mass') 
            volume = request.GET.get('volume') 
            conc = request.GET.get('conc')
            testconc = request.GET.get('testconc') 

            comment = request.GET.get('comment') #测试浓度 单位(miug/mL)
            info = {
                'solvent' : solvent, 
                'mass' : mass,
                'volume' : volume, 
                'conc' : conc, 
                'testconc' : testconc, 
                'comment' : comment,
                }
            lists = testrecord.objects.filter(batch = batch).values('id')
            for i in lists:
                testrecord.objects.select_for_update().filter(id = i['id']).update(**info)
            return recordindex(request, msg = 0)
        except:
            return recordindex(request, msg = 1)

def tbatchinput(request):
    if request.method == 'POST':
        file_obj = request.FILES.get('file')
        if not file_obj:
            return recordindex(request, msg=1)
        file_s = open(os.path.join("./data", file_obj.name), 'wb+')
        for line in file_obj.chunks():
            file_s.write(line)
        file_s.close()
        with open(os.path.join("./data", file_obj.name), 'r') as rf:
            reader = csv.reader(rf)
            line = reader.__next__()
            nnn = 0
            errlist = []
            for rows in reader:
                try:
                    infos = {
                        'testtype' : rows[0],
                        'fromcru' : crudeex.objects.get(mcccnumber=rows[1]), 
                        'fromcpd' : cpd.objects.get(cpdnumber=rows[2]), 
                        'solvent' : rows[3],
                        'mass' : rows[4], 
                        'volume' : rows[5],
                        'conc' : rows[6], 
                        'testconc' : rows[7], 
                        'department' : rows[8],
                        'batch' : rows[9],
                        'comment' : rows[10],
                        'provider' : request.user,
                    }
                    if rows[1]:
                        infos['fromcru'] = crudeex.objects.get(mcccnumber=rows[1])
                    else:
                        infos['fromcpd'] = cpd.objects.get(cpdnumber=rows[2])
                    testrecord.objects.create(**infos)
                    nnn = nnn + 1
                except:
                    nnn = nnn + 1
                    errlist.append(nnn)
        os.remove(os.path.join("./data", file_obj.name)) 
        if not len(errlist):
            return recordindex(request, msg = 0) 
        else:
            return recordindex(request, err = errlist,msg = 2)