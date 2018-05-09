from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect  
from django.http import HttpResponse
from django.shortcuts import render
from .models import testrecord, crudeex, bact,cpd
from django.db.models import Q
from django.utils import timezone


def bactindex(request, msg = -1):
    lists = bact.objects.all()
    num = len(lists)
    return render(request, 'blog/bact.html', context = {'tests' : lists, 'msg' : msg, 'num': num} )

def bactload(request):
    if request.method == "GET":
        bactnumber = request.GET.get('bactnumber') 
        sourcenum = request.GET.get('sourcenum') 
        genus = request.GET.get('genus') 
        species = request.GET.get('species')
        chinesename = request.GET.get('chinesename') 
        othersourcenum =  request.GET.get('othersourcenum')
        history = request.GET.get('history')
        ##storetime = request.GET.get('storetime')  
        orinumber = request.GET.get('orinumber')
        mainuse = request.GET.get('mainuse')
        danger = request.GET.get('danger') 
        hostname = request.GET.get('hostname') 
        ill =request.GET.get('ill')
        media =request.GET.get('media')
        mediatem =request.GET.get('mediatem')
        tranroute =request.GET.get('tranroute')
        gene =request.GET.get('gene')
        recadd =request.GET.get('recadd')
        shareme =request.GET.get('shareme')
        getmet =request.GET.get('getmet')
        callme =request.GET.get('callme')
        mainkey =request.GET.get('mainkey')
        prod =request.GET.get('prod')
        didv =request.GET.get('didv')
        judge =request.GET.get('judge')
        genenumber =request.GET.get('genenumber')
        info = {
            'bactnumber' : bactnumber,
            'sourcenum' : sourcenum, 
            'genus' : genus, 
            'species' : species,
            'chinesename' : chinesename, 
            'othersourcenum' : othersourcenum,
            'history' : history, 
            ##'storetime' : storetime,
            'orinumber' : orinumber,
            'mainuse' : mainuse,
            'danger' : danger, 
            'hostname' : hostname, 
            'ill' : ill,
            'tranroute' : tranroute,
            'media' : media,
            'mediatem' : mediatem,
            'gene' : gene,
            'recadd' : recadd,
            'shareme' : shareme,
            'getmet' : getmet,
            'callme' : callme,
            'mainkey' : mainkey,
            'prod' : prod,
            'didv' : didv,
            'judge' : judge,
            'genenumber' : genenumber,
            'upload' : request.user
        }        
        bact.objects.create(**info)
        return bactindex(request, msg = 0) #msg = 0代表正常插入
        #except:
        #    return bactindex(request, msg = 1) #msg = 1 代表插入失败

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
        try:
            id = request.GET.get('id')
            bactnumber = request.GET.get('bactnumber') 
            sourcenum = request.GET.get('sourcenum') 
            genus = request.GET.get('genus') 
            species = request.GET.get('species')
            chinesename = request.GET.get('chinesename') 
            othersourcenum =  request.GET.get('othersourcenum')
            history = request.GET.get('history')
            ##storetime = request.GET.get('storetime')  
            orinumber = request.GET.get('orinumber')
            mainuse = request.GET.get('mainuse')
            danger = request.GET.get('danger') 
            hostname = request.GET.get('hostname') 
            ill =request.GET.get('ill')
            media =request.GET.get('media')
            mediatem =request.GET.get('mediatem')
            tranroute =request.GET.get('tranroute')
            gene =request.GET.get('gene')
            recadd =request.GET.get('recadd')
            shareme =request.GET.get('shareme')
            getmet =request.GET.get('getmet')
            callme =request.GET.get('callme')
            mainkey =request.GET.get('mainkey')
            prod =request.GET.get('prod')
            didv =request.GET.get('didv')
            judge =request.GET.get('judge')
            genenumber =request.GET.get('genenumber')
            infos = {
                'bactnumber' : bactnumber,
                'sourcenum' : sourcenum, 
                'genus' : genus, 
                'species' : species,
                'chinesename' : chinesename, 
                'othersourcenum' : othersourcenum,
                'history' : history, 
                ##'storetime' : storetime,
                'orinumber' : orinumber,
                'mainuse' : mainuse,
                'danger' : danger, 
                'hostname' : hostname, 
                'ill' : ill,
                'tranroute' : tranroute,
                'media' : media,
                'mediatem' : mediatem,
                'gene' : gene,
                'recadd' : recadd,
                'shareme' : shareme,
                'getmet' : getmet,
                'callme' : callme,
                'mainkey' : mainkey,
                'prod' : prod,
                'didv' : didv,
                'judge' : judge,
                'genenumber' : genenumber,
            }
            bact.objects.select_for_update().filter(id = id).update(**infos)
            return bactindex(request, msg = 0)
        except:
            return bactindex(request, msg = 1)
