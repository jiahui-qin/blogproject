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
def cpdindex(request, msg = -1, err = []):   ##化合物
    ##lists = cpd.objects.all()
    lists = cpd.objects.annotate(num_rec=Count('testrecord'))
    num = len(lists)
    return render(request, 'blog/cpd.html', context = {'tests' : lists, 'msg' : msg, 'num' : num, 'err' : err} )

def cpdload(request):
    if request.method == 'GET':
        #try:
        fromcru = request.GET.get('fromcru')
        cpdnumber = request.GET.get('cpdnumber')
        fromcru = crudeex.objects.get(id=fromcru)
        frombact = fromcru.frombact
        mass = request.GET.get('mass')
        stru = request.GET.get('stru')
        recadd = request.GET.get('recadd')
        nmr = request.GET.get('nmr')
        ms = request.GET.get('ms')
        rot = request.GET.get('rot')
        red = request.GET.get('red')
        blue = request.GET.get('blue')
        media = request.GET.get('media')
        comment = request.GET.get('comment')
        info = {
                'cpdnumber' : cpdnumber,
                'fromcru' : fromcru,
                'frombact' : frombact,
                'mass' : mass,
                'stru' : stru,
                'recadd' : recadd,
                'nmr' : nmr,
                'ms' : ms,
                'rot' : rot,
                'red' : red,
                'blue' : blue,
                'media' : media,
                'prov': request.user,
                'comment' : comment,
        }
        print(info)
        cpd.objects.create(**info)
        return cpdindex(request, msg = 0) #msg = 0代表正常插入
        #except:
        #    return cpdindex(request, msg = 1)

def cpddel(request):
    if request.method == "GET":
        try:
            id = request.GET.get('id')
            cpd.objects.get(id = id).delete()
            return cpdindex(request, msg = 0)
        except:
            return cpdindex(request, msg = 1)


def cpdalter(request):
    if request.method == 'GET':
        try:
            id = request.GET.get('id')
            fromcru = request.GET.get('fromcru')
            cpdnumber = request.GET.get('cpdnumber')
            fromcru = crudeex.objects.get(id=fromcru)
            frombact = fromcru.frombact
            mass = request.GET.get('mass')
            stru = request.GET.get('stru')
            recadd = request.GET.get('recadd')
            nmr = request.GET.get('nmr')
            ms = request.GET.get('ms')
            rot = request.GET.get('rot')
            red = request.GET.get('red')
            blue = request.GET.get('blue')
            media = request.GET.get('media')
            comment = request.GET.get('comment')

            infos = {
                    'cpdnumber' : cpdnumber,
                    'fromcru' : fromcru,
                    'frombact' : frombact,
                    'mass' : mass,
                    'stru' : stru,
                    'recadd' : recadd,
                    'nmr' : nmr,
                    'ms' : ms,
                    'rot' : rot,
                    'red' : red,
                    'blue' : blue,
                    'media' : media,
                    'prov': request.user,
                    'comment' : comment,
            }
            cpd.objects.select_for_update().filter(id = id).update(**infos)
            return cpdindex(request, msg = 0)
        except:
            return cpdindex(request, msg = 1)

def cpdbatchinput(request):
    if request.method == 'POST':
        file_obj = request.FILES.get('file')
        if not file_obj:
            return cpdindex(request, msg=1)
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
                        'cpdnumber' : rows[0],
                        'fromcru' : crudeex.objects.get(mcccnumber=rows[1]), 
                        'frombact' : fromcru.frombact,
                        'mass' : rows[2], 
                        'stru' : rows[3],
                        'recadd' : rows[4], 
                        'nmr' : rows[5],
                        'ms' : rows[6], 
                        'rot' : rows[7],
                        'red' : rows[8], 
                        'blue' : rows[9], 
                        'media' : rows[10],
                        'comment' : rows[11],
                        'prov' : request.user,
                    }
                    infos['frombact'] = info.get('fromcru').frombact
                    cpd.objects.create(**infos)
                    nnn = nnn + 1
                except:
                    nnn = nnn + 1
                    errlist.append(nnn)
        os.remove(os.path.join("./data", file_obj.name))
        if not len(errlist):
            return cpdindex(request, msg = 0) 
        else:
            return cpdindex(msg = 2, err = errlist)

def cpd2rec(request, cpdid):
    cpds = cpd.objects.get(id = cpdid)
    lists = testrecord.objects.filter(fromcpd = cpds)
    return render(request, 'blog/record.html', context = {'tests' : lists, 'msg' : -1} )