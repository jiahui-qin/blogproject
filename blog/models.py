from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
from django.utils.html import strip_tags

# Create your models here.

@python_2_unicode_compatible

class bact(models.Model):  #菌株
    bactnumber = models.CharField(max_length = 50) #菌株保藏编号
    sourcenum = models.CharField(max_length = 50, blank = True) #平台资源编号
    genus = models.CharField(max_length = 200) #属名
    species = models.CharField(max_length = 200) #种名
    chinesename = models.CharField(max_length = 200, blank = True) #中文名
    recadd = models.CharField(max_length = 100)#样品存储地址
    orinum = models.CharField(max_length = 100, blank = True) #原始资源编号
    history = models.CharField(max_length = 100, blank = True) #来源历史
    storetime = models.DateTimeField(auto_now_add=True,editable = True) #收藏时间
    media = models.CharField(max_length = 50) #培养基编号
    getmet = models.CharField(max_length = 100) #获取途径
    upload = models.ForeignKey(User, null = True)#保藏人
    modbact = models.CharField(max_length = 50, blank = True)#模式菌株
    mianuse = models.CharField(max_length = 100, blank = True) #主要用途
    danger = models.CharField(max_length = 100, blank = True) #生物危害程度
    comment = models.CharField(max_length = 500, blank = True)
    def __str__(self):
        return self.bactnumber + '|' + self.chinesename

class crudeex(models.Model): ##粗提物
    frombact = models.ForeignKey(bact) ##来源菌株
    mcccnumber = models.CharField(max_length = 50) #mccc编号
    chinesename = models.CharField(max_length = 200) #中文名
    recadd = models.CharField(max_length = 100)#样品存储地址
    media = models.CharField(max_length = 200) #培养基
    entertime = models.DateTimeField(auto_now_add=True,editable = True) #入库时间
    entervol = models.FloatField() #入库体积
    entercol =  models.FloatField() #入库浓度
    solvent = models.CharField(max_length = 100) #溶剂
    exrmethod = models.CharField(max_length = 500, blank = True) #提取方法
    provider = models.ForeignKey(User) #提供人
    comment = models.CharField(max_length = 500, blank = True)
    def __str__(self):
        return self.mcccnumber + '|' + self.chinesename




class cpd(models.Model): ##化合物
    cpdnumber = models.CharField(max_length = 20)#化合物编号
    frombact = models.ForeignKey(crudeex)#来源菌株
    mass = models.FloatField() #精确质量数
    stru = models.CharField(max_length = 50)#分子式
    recadd = models.CharField(max_length = 100)#样品存储地址
    nmr = models.CharField(max_length = 100, blank = True)#nmr数据
    ms = models.CharField(max_length = 100, blank = True)#ms数据
    rot = models.CharField(max_length = 100, blank = True)#旋光数据
    red = models.CharField(max_length = 100, blank = True)#红外数据
    blue = models.CharField(max_length = 100, blank = True)#紫外数据
    media = models.CharField(max_length = 50, blank = True)#培养基编号
    prov = models.ForeignKey(User)#提供人
    time = models.DateTimeField(auto_now_add=True, editable = True)#入库时间
    comment = models.CharField(max_length = 500, blank = True)
    def __str__(self):
        return self.cpdnumber + '|' + self.stru

class testrecord(models.Model):
    testtype = models.CharField(max_length = 20) #送测类型
    fromcru = models.ForeignKey(crudeex, null = True) ##链接至粗提物,可以在粗提物的每一行后边加一个按钮，增加送测记录。
    fromcpd = models.ForeignKey(cpd, null = True)#链接至化合物
    samst = models.IntegerField(blank = True) #样品起序号
    samend = models.IntegerField(blank = True) #样品终序号
    solvent = models.CharField(max_length = 100) #溶剂
    mass = models.FloatField() #重量，单位miug
    volume = models.FloatField() #体积单位niuL
    conc = models.FloatField() #浓度 单位(mg/mL)
    testconc = models.FloatField(blank= True) #测试浓度 单位(miug/mL)
    provider = models.ForeignKey(User) #提供人
    department = models.CharField(max_length=100) #测样单位
    sendtime = models.DateTimeField(auto_now_add=True, editable = True)
    comment = models.CharField(max_length = 500, blank = True)

    def __str__(self):
        return self.testtype