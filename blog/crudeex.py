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
        genus = request.GET.get('genus')
        species = request.GET.get('species')
        chinesename = request.GET.get('chinesename')
        media = request.GET.get('media')
        medianumber = request.GET.get('medianumber')
        mass = request.GET.get('mass')
        stockmass = request.GET.get('stockmass')
        cointermass = request.GET.get('cointermass')
        #entertime = request.GET.get('entertime')
        entervol = request.GET.get('entervol')
        entercol = request.GET.get('entercol')
        testcol = request.GET.get('testcol')
        testvol = request.GET.get('testvol')
        activecol = request.GET.get('activecol')
        solvent = request.GET.get('solvent')
        culture = request.GET.get('culture')
        exrmethod = request.GET.get('exrmethod')
        department = request.GET.get('department')
        activeresult = request.GET.get('activeresult')
        comment = request.GET.get('comment')
        frombact = bact.objects.get(id=bactid)
        info = {
                'frombact' : frombact,
                'mcccnumber' : mcccnumber, 
                'genus' : genus, 
                'species' : species, 
                'chinesename' : chinesename, 
                'media' : media, 
                'medianumber' : medianumber, 
                'mass' : mass, 
                'stockmass' : stockmass, 
                'cointermass' : cointermass, 
                #'entertime' : entertime, 
                'entervol' : entervol, 
                'entercol' : entercol, 
                'testcol' : testcol, 
                'testvol' : testvol, 
                'activecol' : activecol, 
                'solvent' : solvent, 
                'culture' : culture, 
                'exrmethod' : exrmethod,
                'department' : department, 
                'activeresult' : activeresult, 
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
        id = request.GET.get('id')
        frombact = request.GET.get('frombact')
        mcccnumber = request.GET.get('mcccnumber')
        genus = request.GET.get('genus')
        species = request.GET.get('species')
        chinesename = request.GET.get('chinesename')
        media = request.GET.get('media')
        medianumber = request.GET.get('medianumber')
        mass = request.GET.get('mass')
        stockmass = request.GET.get('stockmass')
        cointermass = request.GET.get('cointermass')
        #entertime = request.GET.get('entertime')
        entervol = request.GET.get('entervol')
        entercol = request.GET.get('entercol')
        testcol = request.GET.get('testcol')
        testvol = request.GET.get('testvol')
        activecol = request.GET.get('activecol')
        solvent = request.GET.get('solvent')
        culture = request.GET.get('culture')
        exrmethod = request.GET.get('exrmethod')
        department = request.GET.get('department')
        activeresult = request.GET.get('activeresult')
        comment = request.GET.get('comment')
        infos = {
            'frombact' : frombact,
            'mcccnumber' : mcccnumber, 
            'genus' : genus, 
            'species' : species, 
            'chinesename' : chinesename, 
            'media' : media, 
            'medianumber' : medianumber, 
            'mass' : mass, 
            'stockmass' : stockmass, 
            'cointermass' : cointermass, 
            #'entertime' : entertime, 
            'entervol' : entervol, 
            'entercol' : entercol, 
            'testcol' : testcol, 
            'testvol' : testvol, 
            'activecol' : activecol, 
            'solvent' : solvent, 
            'culture' : culture, 
            'exrmethod' : exrmethod,
            'department' : department, 
            'activeresult' : activeresult, 
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