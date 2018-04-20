from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect  
from django.http import HttpResponse
from django.shortcuts import render
from .models import testrecord, crudeex, bact,cpd
from django.db.models import Q
from django.utils import timezone


def recordindex(request, msg = -1):
    lists = testrecord.objects.all()
    print(type(lists))
    return render(request, 'blog/record.html', context = {'tests' : lists, 'msg' : msg} )

def upload(request):
    if request.method == "GET":
        try:
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
            #sendtime = request.GET.get('sendtime') #送样时间
            comment =request.GET.get('comment')
            info = {
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
                'provider': request.user
            }        
            testrecord.objects.create(**info)
            return recordindex(request, msg = 0) #msg = 0代表正常插入
        except:
            return recordindex(request, msg = 1) #msg = 1 代表插入失败

def recdel(request):
    if request.method == "GET":
        id = request.GET.get('id')
        testrecord.objects.get(id = id).delete()
        return recordindex(request, msg = 0)

def recalter(request):
    if request.method == 'POST':
        #try:
        id = request.POST['id']
        testtype = request.POST['testtype'] #或者改成两个可选项？粗提物或者化合物
        boxnumber = request.POST['boxnumber'] #盒序号
        samplestart = request.POST['samplestart'] #样品起序号
        sampleend = request.POST['sampleend'] #样品终序号
        samplename = request.POST['samplename'] #样品名
        samplenum = int(sampleend) - int(samplestart) + 1 #样品数量
        solvent = request.POST['solvent'] #溶剂
        mass = request.POST['mass']#重量，单位miug
        volume = request.POST['volume'] #体积单位niuL
        concentration = request.POST['concentration'] #浓度 单位(mg/mL)
        testconcentration = request.POST['testconcentration'] #测试浓度 单位(miug/mL)
        department = request.POST['department'] #测样单位
        #sendtime = request.POST['sendtime') #送样时间
        comment =request.POST['comment']
        infos = {
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
            'provider': request.user
        }        
        obj = testrecord.objects.get(id = id)
        for info in infos:
            if infos[info] != obj[info]:
                obj.info = infos[info]
        obj.save()
        return recordindex(request, msg = 0)