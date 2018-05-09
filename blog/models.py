from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
from django.utils.html import strip_tags

# Create your models here.

@python_2_unicode_compatible

class bact(models.Model):  #菌株
    bactnumber = models.CharField(max_length = 50) #菌株保藏编号
    sourcenum = models.CharField(max_length = 50) #平台资源编号
    genus = models.CharField(max_length = 200) #属名
    species = models.CharField(max_length = 200) #种名
    chinesename = models.CharField(max_length = 200, blank = True) #中文名
    othersourcenum = models.CharField(max_length = 100, blank = True) #其它平台资源编号
    history = models.CharField(max_length = 100, blank = True) #来源历史
    storetime = models.DateTimeField(auto_now_add=True,editable = True) #收藏时间
    orinumber = models.CharField(max_length = 20, blank = True)#原始资源编号
    mainuse = models.CharField(max_length = 200, blank = True)#主要用途
    danger = models.CharField(max_length = 50, blank = True)#生物危害程度
    hostname = models.CharField(max_length = 100, blank = True)#寄主名称
    ill = models.CharField(max_length = 100, blank = True) #致病名称
    tranroute = models.CharField(max_length = 100, blank = True) #传播途径
    media = models.CharField(max_length = 50, blank = True) #培养基编号
    mediatem = models.CharField(max_length = 10, blank = True) #培养基温度
    gene = models.CharField(max_length = 50, blank = True) # 基因元器件
    recadd = models.CharField(max_length = 100, blank = True)#记录地址
    shareme = models.CharField(max_length = 100, blank = True)#共享方式
    getmet = models.CharField(max_length = 100, blank = True) #获取途径
    callme = models.CharField(max_length = 30, blank = True)#联系方式
    mainkey = models.CharField(max_length = 100, blank = True)#源数据主键
    prod = models.CharField(max_length = 30, blank = True)#提供人
    didv = models.CharField(max_length = 30, blank = True)#分离人
    judge = models.CharField(max_length = 30, blank = True)#鉴定人
    genenumber = models.CharField(max_length = 50, blank = True)#基因序列注册号
    upload = models.ForeignKey(User, null = True)
    def __str__(self):
        return self.bactnumber + '|' + self.chinesename

class crudeex(models.Model): ##粗提物
    frombact = models.ForeignKey(bact)
    mcccnumber = models.CharField(max_length = 50) #mccc编号
    genus = models.CharField(max_length = 200) #属名
    species = models.CharField(max_length = 200) #种名
    chinesename = models.CharField(max_length = 200) #中文名
    media = models.CharField(max_length = 200) #培养基
    medianumber = models.CharField(max_length = 50) #培养基编号
    mass = models.FloatField() #重量，单位mg
    stockmass = models.FloatField() #库存量，单位mg
    cointermass = models.FloatField() #样品瓶重量，单位miug
    testcol = models.FloatField(blank = True) #测试浓度
    testvol = models.FloatField(blank = True) #测试体积
    activecol = models.FloatField(blank = True) #活性浓度
    solvent = models.CharField(max_length = 100) #溶剂
    culture = models.CharField(max_length = 500, blank = True) #培养条件
    exrmethod = models.CharField(max_length = 500, blank = True) #提取方法
    provider = models.ForeignKey(User) #提供人
    department = models.CharField(max_length=100) #测样单位
    sendtime = models.DateTimeField(auto_now_add=True, editable = True) #送样时间
    activeresult = models.CharField(max_length = 500, blank = True) #活性检测结果
    entertime = models.DateTimeField(null = True) #入库时间
    entervol = models.FloatField(blank = True) #入库体积
    entercol =  models.FloatField(blank = True) #入库浓度
    comment = models.CharField(max_length = 500, blank = True)

    
    
    #def __str__(self):
    #    return self.crudenumber + '|' + self.chinesename




class cpd(models.Model): ##化合物
    cpdnumber = models.CharField(max_length = 20)#化合物编号
    frombact = models.CharField(max_length = 20)#来源菌株
    mass = models.FloatField() #精确质量数
    stru = models.CharField(max_length = 50)#分子式
    nmr = models.CharField(max_length = 100)#nmr数据
    ms = models.CharField(max_length = 100)#ms数据
    rot = models.CharField(max_length = 100)#旋光数据
    red = models.CharField(max_length = 100)#红外数据
    blue = models.CharField(max_length = 100)#紫外数据
    media = models.CharField(max_length = 50)#培养基编号
    depa = models.CharField(max_length = 100)#活性送测单位
    spc = models.CharField(max_length = 100)#活性种类
    time = models.DateTimeField(auto_now_add=True, editable = True)#活性送测时间!!!!
    resu = models.CharField(max_length = 100)#活性结果
    prov = models.ForeignKey(User)#提供人
    dtime = models.DateTimeField()#入库时间
    
    def __str__(self):
        return self.cpdnumber + '|' + self.stru

class testrecord(models.Model):
    fromcru = models.ForeignKey(crudeex, null = True) ##链接至粗提物,可以在粗提物的每一行后边加一个按钮，增加送测记录。
    testtype = models.CharField(max_length = 20) #或者改成两个可选项？粗提物或者化合物
    boxnumber = models.IntegerField(blank = True) #盒序号
    samplestart = models.IntegerField(blank = True) #样品起序号
    sampleend = models.IntegerField(blank = True) #样品终序号
    samplenum = models.IntegerField(blank = True) #样品数量
    samplename = models.CharField(max_length = 100) #样品名
    solvent = models.CharField(max_length = 100) #溶剂
    mass = models.FloatField() #重量，单位miug
    volume = models.FloatField() #体积单位niuL
    concentration = models.FloatField() #浓度 单位(mg/mL)
    testconcentration = models.FloatField(blank= True) #测试浓度 单位(miug/mL)
    provider = models.ForeignKey(User) #提供人
    department = models.CharField(max_length=100) #测样单位
    sendtime = models.DateTimeField(auto_now_add=True, editable = True)
    comment = models.CharField(max_length = 500, blank = True)

    def __str__(self):
        return self.samplename