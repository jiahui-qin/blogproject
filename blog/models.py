from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
from django.utils.html import strip_tags

# Create your models here.

@python_2_unicode_compatible
#class meta(models.Model):
#    metabolomics = models.CharField(max_length = 200)
#    mz = models.FloatField()
#    rt = models.FloatField()
#    provider = models.ForeignKey(User)
#    updatetime = models.DateTimeField()
#    def __str__(self):
#        return self.metabolomics

class testrecord(models.Model):
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
    sendtime.editable = 'True'     #送样时间
    comment = models.CharField(max_length = 500, blank = True)

    def __str__(self):
        return self.samplename

class crudeex(models.Model):
    crudenumber = models.CharField(max_length = 50) #粗提物编号
    mcccnumber = models.CharField(max_length = 50) #mccc编号
    genus = models.CharField(max_length = 200) #属名
    species = models.CharField(max_length = 200) #种名
    chinesename = models.CharField(max_length = 200) #中文名
    media = models.CharField(max_length = 200) #培养基
    medianumber = models.CharField(max_length = 50) #培养基编号
    mass = models.FloatField() #重量，单位mg
    stockmass = models.FloatField() #库存量，单位mg
    cointermass = models.FloatField() #样品瓶重量，单位miug
    entertime = models.DateTimeField() #入库时间
    entervol = models.FloatField() #入库体积
    entercol =  models.FloatField() #入库浓度
    tetscol = models.FloatField() #测试浓度
    testvol = models.FloatField() #测试体积
    activecol = models.FloatField() #活性浓度
    solvent = models.CharField(max_length = 100) #溶剂
    culture = models.CharField(max_length = 500, blank = True) #培养条件
    exrmethod = models.CharField(max_length = 500, blank = True) #提取方法
    provider = models.ForeignKey(User) #提供人
    department = models.CharField(max_length=100) #测样单位
    sendtime = models.DateTimeField(auto_now_add=True,editable = True) #送样时间
    activeresult = models.CharField(max_length = 500, blank = True) #活性检测结果
    comment = models.CharField(max_length = 500, blank = True)
    def __str__(self):
        return self.crudenumber + '|' + self.chinesename


class bact(models.Model):
    bactnumber = models.CharField(max_length = 50) #菌株保藏编号
    sourcenum = models.CharField(max_length = 50) #平台资源编号
    genus = models.CharField(max_length = 200) #属名
    species = models.CharField(max_length = 200) #种名
    chinesename = models.CharField(max_length = 200) #中文名
    othersourcenum = models.CharField(max_length = 100) #其它平台资源编号
    history = models.CharField(max_length = 100) #来源历史
    storetimr = models.DateTimeField() #收藏时间
    def __str__(self):
        return self.bactnumber + '|' + self.chinesename






