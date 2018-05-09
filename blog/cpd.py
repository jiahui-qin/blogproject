from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect  
from django.http import HttpResponse
from django.shortcuts import render
from .models import testrecord, crudeex, bact,cpd
from django.db.models import Q
from django.utils import timezone

def cpdindex(request, msg = -1):   ##化合物
    lists = cpd.objects.all()
    num = len(lists)
    return render(request, 'blog/cpd.html', context = {'tests' : lists, 'msg' : msg, 'num' : num} )

def cpdload(request):
    if request.method == 'GET':
        cpdnumber = request.GET.get('cpdnumber')
        frombact = request.GET.get('frombact')
        mass = request.GET.get('mass')
        stru = request.GET.get('stru')
        nmr = request.GET.get('nmr')
        ms = request.GET.get('ms')
        rot = request.GET.get('rot')
        red = request.GET.get('red')
        blue = request.GET.get('blue')
        media = request.GET.get('media')
        depa = request.GET.get('depa')
        spc = request.GET.get('spc')
        resu = request.GET.get('resu')
        dtime = request.GET.get('dtime')
        info = {
                'cpdnumber' : cpdnumber,
                'frombact' : frombact,
                'mass' : mass,
                'stru' : stru,
                'nmr' : nmr,
                'ms' : ms,
                'rot' : rot,
                'red' : red,
                'blue' : blue,
                'media' : media,
                'depa' : depa,
                'spc' : spc,
                'resu' : resu,
                'dtime' : dtime,
                'prov': request.user
        }
        cpd.objects.create(**info)
        return cpdindex(request, msg = 0) #msg = 0代表正常插入

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
            cpdnumber = request.GET.get('cpdnumber')
            frombact = request.GET.get('frombact')
            mass = request.GET.get('mass')
            stru = request.GET.get('stru')
            nmr = request.GET.get('nmr')
            ms = request.GET.get('ms')
            rot = request.GET.get('rot')
            red = request.GET.get('red')
            blue = request.GET.get('blue')
            media = request.GET.get('media')
            depa = request.GET.get('depa')
            spc = request.GET.get('spc')
            resu = request.GET.get('resu')
            dtime = request.GET.get('dtime')
            infos = {
                    'cpdnumber' : cpdnumber,
                    'frombact' : frombact,
                    'mass' : mass,
                    'stru' : stru,
                    'nmr' : nmr,
                    'ms' : ms,
                    'rot' : rot,
                    'red' : red,
                    'blue' : blue,
                    'media' : media,
                    'depa' : depa,
                    'spc' : spc,
                    'resu' : resu,
                    'dtime' : dtime,
                    'prov': request.user
            }
            cpd.objects.select_for_update().filter(id = id).update(**infos)
            return cpdindex(request, msg = 0)
        except:
            return cpdindex(request, msg = 1)