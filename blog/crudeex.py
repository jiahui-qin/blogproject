from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect  
from django.http import HttpResponse
from django.shortcuts import render
from .models import testrecord, crudeex, bact,cpd
from django.db.models import Q
from django.utils import timezone
import os
import csv
from django.core.urlresolvers import reverse  
from django.shortcuts import redirect  
from django.db.models.aggregates import Count

@login_required
def crudeexindex(request, msg = -1, err = []):  ##粗提物
    ##lists = crudeex.objects.all()
    lists = crudeex.objects.annotate(num_cpd=Count('cpd')).order_by('-id')
    num = len(lists)
    return render(request, 'blog/crudeex.html', context = {'tests' : lists, 'msg' : msg, 'num' : num, 'err' : err} )

def curdeexupload(request):
    try:
        if request.method == 'GET':
            bactid = request.GET.get('frombact')
            mcccnumber = request.GET.get('mcccnumber')
            chinesename = request.GET.get('chinesename')
            media = request.GET.get('media')
            recadd = request.GET.get('recadd')
            entervol = request.GET.get('entervol')
            entercol = request.GET.get('entercol')
            solvent = request.GET.get('solvent')
            exrmethod = request.GET.get('exrmethod')
            comment = request.GET.get('comment')
            frombact = bact.objects.get(id=bactid)
            info = {
                    'frombact' : frombact,
                    'mcccnumber' : mcccnumber, 
                    'chinesename' : chinesename, 
                    'media' : media, 
                    'recadd' : recadd, 
                    'entervol' : entervol, 
                    'entercol' : entercol, 
                    'solvent' : solvent, 
                    'exrmethod' : exrmethod,
                    'comment' : comment, 
                    'provider': request.user,
            }
            crudeex.objects.create(**info)
            return crudeexindex(request, msg = 0) #msg = 0代表正常插入
    except:
        return crudeexindex(request, msg = 1)

def crudel(request):
    if request.method == "GET":
        try:
            id = request.GET.get('id')
            crudeex.objects.get(id = id).delete()
            return crudeexindex(request, msg = 0)
        except:
            return crudeexindex(request, msg = 1)


def crualter(request):
    if request.method == 'GET':
        try:
            id = request.GET.get('id')
            bactid = request.GET.get('frombact')
            mcccnumber = request.GET.get('mcccnumber')
            chinesename = request.GET.get('chinesename')
            media = request.GET.get('media')
            recadd = request.GET.get('recadd')
            entervol = request.GET.get('entervol')
            entercol = request.GET.get('entercol')
            solvent = request.GET.get('solvent')
            exrmethod = request.GET.get('exrmethod')
            comment = request.GET.get('comment')
            frombact = bact.objects.get(id=bactid)
            infos = {
                'frombact' : frombact,
                'mcccnumber' : mcccnumber, 
                'chinesename' : chinesename, 
                'media' : media, 
                'recadd' : recadd, 
                'entervol' : entervol, 
                'entercol' : entercol, 
                'solvent' : solvent, 
                'exrmethod' : exrmethod,
                'comment' : comment, 
                'provider': request.user,
            }
            #print(infos)
            crudeex.objects.select_for_update().filter(id = id).update(**infos)
            return crudeexindex(request, msg = 0)
        except:
            return crudeexindex(request, msg = 1)



def cru2rec(request):
    if request.method == "GET":
        cruid = request.GET.get('cruid')
        testtype = request.GET.get('testtype') #或者改成两个可选项？粗提物或者化合物
        boxnumber = request.GET.get('boxnumber') #盒序号
        samplestart = request.GET.get('samplestart') #样品起序号
        sampleend = request.GET.get('sampleend') #样品终序号
        samplename = request.GET.get('samplename') #样品名
        samplenum = int(sampleend) - int(samplestart) + 1 #样品数量
        solvent = request.GET.get('solvent') #溶剂
        mass = request.GET.get('mass')#重量，单位miug
        volume = request.GET.get('volume') #体积单位niuL
        concentration = request.GET.get('concentration') #浓度 单位(mg/mL)
        testconcentration = request.GET.get('testconcentration') #测试浓度 单位(miug/mL)
        department = request.GET.get('department') #测样单位
        comment =request.GET.get('comment')
        cru = crudeex.objects.get(id = cruid)
        info = {
            'fromcru' : cru,
            'testtype' : testtype, 
            'boxnumber' : boxnumber, 
            'samplestart' : samplestart, 
            'sampleend' : sampleend, 
            'samplenum' : samplenum,
            'samplename' : samplename, 
            'solvent' : solvent, 
            'mass' : mass, 
            'volume' : volume, 
            'concentration' : concentration, 
            'testconcentration' : testconcentration, 
            'department' : department,  
            'comment' : comment,
            'provider': request.user,
        }        
        testrecord.objects.create(**info)
        return crudeexindex(request, msg = 0)

def cbatchinput(request):
    if request.method == 'POST':
        file_obj = request.FILES.get('file')
        if not file_obj:
            return crudeexindex(request, msg=1)
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
                        'frombact' : bact.objects.get(bactnumber=rows[0]),
                        'mcccnumber' : rows[1], 
                        'chinesename' : rows[2], 
                        'recadd' : rows[3],
                        'media' : rows[4], 
                        'entervol' : rows[5],
                        'entercol' : rows[6], 
                        'solvent' : rows[7],
                        'exrmethod' : rows[8], 
                        'comment' : rows[9], 
                        'provider' : request.user,
                    }
                    crudeex.objects.create(**infos)
                    nnn = nnn + 1
                except:
                    nnn = nnn + 1
                    errlist.append(nnn)
        os.remove(os.path.join("./data", file_obj.name))
        return crudeexindex(request, msg = 0)
        if not len(errlist):
            return crudeexindex(request, msg = 0)
        else:
            return crudeexindex(request, msg = 2, err = errlist)

def cru2cpd(request, cruid):
    cru = crudeex.objects.get(id = cruid)
    lists = cpd.objects.filter(fromcru = cru)
    return render(request, 'blog/cpd.html', context = {'tests' : lists, 'msg' : -1} )