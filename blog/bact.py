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
def bactindex(request, msg = -1, err = []):
    lists =bact.objects.annotate(num_crudeex=Count('crudeex'))
    #lists = bact.objects.all()
    num = len(lists)
    return render(request, 'blog/bact.html', context = {'tests' : lists, 'msg' : msg, 'num': num, 'err' : err} )

def bactload(request):
    if request.method == "GET":
        try:
            bactnumber = request.GET.get('bactnumber') 
            sourcenum = request.GET.get('sourcenum') 
            genus = request.GET.get('genus') 
            species = request.GET.get('species')
            chinesename = request.GET.get('chinesename') 
            recadd =  request.GET.get('recadd')
            orinum = request.GET.get('orinum') 
            history = request.GET.get('history')
            media = request.GET.get('media') 
            getmet = request.GET.get('getmet') 
            modbact =request.GET.get('modbact')
            mianuse =request.GET.get('mianuse')
            danger =request.GET.get('danger')
            comment =request.GET.get('comment')
            if bactnumber == "" or genus == "" or species == "" or recadd == "" or  media == "" or getmet == "":
                return bactindex(request, msg = 1)
            info = {
                'bactnumber' : bactnumber,
                'sourcenum' : sourcenum, 
                'genus' : genus, 
                'species' : species,
                'chinesename' : chinesename, 
                'recadd' : recadd,
                'orinum' : orinum, 
                'history' : history,
                'media' : media, 
                'getmet' : getmet, 
                'upload' : request.user,
                'modbact' : modbact,
                'mianuse' : mianuse,
                'danger' : danger,
                'comment' : comment,
            }        
            bact.objects.create(**info)
            #return HttpResponseRedirect('/bactindex')
            return bactindex(request, msg = 0) #msg = 0代表正常插入
        except:
            return bactindex(request, msg = 1) #msg = 1 代表插入失败

def bactdel(request):
    if request.method == "GET":
        try:
            id = request.GET.get('id')
            bact.objects.get(id = id).delete()
            return bactindex(request, msg = 0)
        except:
            return bactindex(request, msg = 1)


def bactalter(request):
    if request.method == 'GET':
        ##之前失败是因为提供了收藏时间··这个不应该被修正的
        try:
            id = request.GET.get('id')
            bactnumber = request.GET.get('bactnumber') 
            sourcenum = request.GET.get('sourcenum') 
            genus = request.GET.get('genus') 
            species = request.GET.get('species')
            chinesename = request.GET.get('chinesename') 
            recadd =  request.GET.get('recadd')
            orinum = request.GET.get('orinum') 
            history = request.GET.get('history')
            media = request.GET.get('media') 
            getmet = request.GET.get('getmet') 
            modbact =request.GET.get('modbact')
            mianuse =request.GET.get('mianuse')
            danger =request.GET.get('danger')
            comment =request.GET.get('comment')
            infos = {
                'bactnumber' : bactnumber,
                'sourcenum' : sourcenum, 
                'genus' : genus, 
                'species' : species,
                'chinesename' : chinesename, 
                'recadd' : recadd,
                'orinum' : orinum, 
                'history' : history,
                'media' : media, 
                'getmet' : getmet, 
                'upload' : request.user,
                'modbact' : modbact,
                'mianuse' : mianuse,
                'danger' : danger,
                'comment' : comment,
            }
            bact.objects.select_for_update().filter(id = id).update(**infos)
            return bactindex(request, msg = 0)
        except:
            return bactindex(request, msg = 1)

def batchinput(request):
    if request.method == 'POST':
        file_obj = request.FILES.get('file')
        if not file_obj:
            return bactindex(request, msg=1)
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
                        'bactnumber' : rows[0],
                        'sourcenum' : rows[1], 
                        'genus' : rows[2], 
                        'species' : rows[3],
                        'chinesename' : rows[4], 
                        'recadd' : rows[5],
                        'orinum' : rows[6], 
                        'history' : rows[7],
                        'media' : rows[8], 
                        'getmet' : rows[9], 
                        'modbact' : rows[10],
                        'mianuse' : rows[11],
                        'danger' : rows[12],
                        'comment' : rows[13],
                        'upload' : request.user,
                    }
                    bact.objects.create(**infos)
                    nnn = nnn + 1
                except:
                    nnn = nnn + 1
                    errlist.append(nnn)
        os.remove(os.path.join("./data", file_obj.name))
        if not len(errlist):
            return bactindex(request, msg = 0) 
        else:
            return bactindex(request, msg = 2, err = errlist)

def bact2cru(request, bactid):
    bacts = bact.objects.get(id = bactid)
    lists = crudeex.objects.filter(frombact = bacts)
    return render(request, 'blog/crudeex.html', context = {'tests' : lists, 'msg' : -1} )