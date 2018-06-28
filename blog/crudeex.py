from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect  
from django.http import HttpResponse
from django.shortcuts import render
from .models import testrecord, crudeex, bact,cpd
from django.db.models import Q
from django.utils import timezone

def crudeexindex(request, msg = -1):  ##粗提物
    lists = crudeex.objects.all()
    num = len(lists)
    return render(request, 'blog/crudeex.html', context = {'tests' : lists, 'msg' : msg, 'num' : num} )

def curdeexupload(request):
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
        #try:
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
        crudeex.objects.select_for_update().filter(id = id).update(**infos)
        return crudeexindex(request, msg = 0)
    #except:
    #    return crudeexindex(request, msg = 1)

def bact2cru(request, bactid):
    bacts = bact.objects.get(id = bactid)
    lists = crudeex.objects.filter(frombact = bacts)
    return render(request, 'blog/crudeex.html', context = {'tests' : lists, 'msg' : -1} )

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