from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect  
from django.http import HttpResponse
from django.shortcuts import render
from .models import testrecord, crudeex, bact,cpd
from django.db.models import Q
from django.utils import timezone

def cpdindex(request, msg = -1):
    lists = cpd.objects.all()
    return render(request, 'blog/cpd.html', context = {'tests' : lists, 'msg' : msg} )

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
        time = request.GET.get('time')
        resu = request.GET.get('resu')
        prov = request.GET.get('prov')
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
                'time' : time,
                'resu' : resu,
                'prov' : prov,
                'dtime' : dtime,
        }
        cpd.objects.create(**info)
        return cpdindex(request, msg = 0) #msg = 0代表正常插入
