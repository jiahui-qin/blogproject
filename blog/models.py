from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
from django.utils.html import strip_tags

# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser

class bact(models.Model):  #菌株
    bactnumber = models.CharField(max_length = 50,blank = False, unique = True) #菌株保藏编号 唯一
    sourcenum = models.CharField(max_length = 50, blank = True) #平台资源编号 输入
    genus = models.CharField(max_length = 200,blank = False) #属名 输入
    species = models.CharField(max_length = 200,blank = False) #种名 输入
    chinesename = models.CharField(max_length = 200, blank = True) #中文名 输入
    recadd = models.CharField(max_length = 100,blank = False)#样品存储地址 输入
    orinum = models.CharField(max_length = 100, blank = True) #原始资源编号 输入
    history = models.CharField(max_length = 100, blank = True) #来源历史 输入
    storetime = models.DateTimeField(auto_now_add=True,editable = True) #收藏时间
    media = models.CharField(max_length = 50,blank = False) #培养基编号 输入
    getmet = models.CharField(max_length = 100,blank = False) #获取途径 输入
    upload = models.ForeignKey(User, null = True)#保藏人
    modbact = models.CharField(max_length = 50, blank = True)#模式菌株 输入
    mianuse = models.CharField(max_length = 100, blank = True) #主要用途 输入
    danger = models.CharField(max_length = 100, blank = True) #生物危害程度 输入
    comment = models.CharField(max_length = 500, blank = True) #输入
    def __str__(self):
        return self.bactnumber + '|' + self.chinesename

class crudeex(models.Model): ##粗提物
    ##10/22修改，加入一列粗提物编号
    frombact = models.ForeignKey(bact) ##来源菌株  %%没有显示出来
    #crunumber = models.CharField(max_length = 50) #粗提物编号，唯一
    mcccnumber = models.CharField(max_length = 50, unique = True) #mccc编号
    chinesename = models.CharField(max_length = 200, blank = True) #中文名
    recadd = models.CharField(max_length = 100)#样品存储地址
    media = models.CharField(max_length = 200) #培养基
    entertime = models.DateTimeField(auto_now_add=True,editable = True) #入库时间
    entervol = models.FloatField(blank = True,null = True) #入库体积
    entercol =  models.FloatField(blank = True,null = True) #入库浓度
    solvent = models.CharField(max_length = 100, blank = True) #溶剂
    exrmethod = models.CharField(max_length = 500, blank = True) #提取方法
    provider = models.ForeignKey(User) #提供人
    comment = models.CharField(max_length = 500, blank = True)
    def __str__(self):
        return self.mcccnumber + '|' + self.chinesename




class cpd(models.Model): ##化合物
    ##10.22修改，加入一列来源菌株
    cpdnumber = models.CharField(max_length = 20, unique = True)#化合物编号，唯一
    fromcru = models.ForeignKey(crudeex)#来源粗提物
    frombact = models.ForeignKey(bact) #来源菌株
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
    #12/15修正，修改体积、浓度、送测批次，修正为可以为空
    ###送测批次TrueTrue
    ###按照送测批次修改，送测批次应该为必填项
    #12/19修正，加入recordid
    recordid = models.CharField(max_length = 20, unique = True)
    testtype = models.CharField(max_length = 20) #送测类型
    fromcru = models.ForeignKey(crudeex, null = True) ##链接至粗提物
    fromcpd = models.ForeignKey(cpd, null = True)#链接至化合物
    solvent = models.CharField(max_length = 100) #溶剂
    mass = models.FloatField() #重量，单位miug
    volume = models.FloatField(blank = True,null = True) #体积单位niuL
    conc = models.FloatField(blank = True,null = True) #浓度 单位(mg/mL)
    testconc = models.FloatField(blank = True,null = True) #测试浓度 单位(miug/mL)
    provider = models.ForeignKey(User) #提供人
    department = models.CharField(max_length=100) #测样单位
    sendtime = models.DateTimeField(auto_now_add=True, editable = True)#送样时间
    batch = models.CharField(max_length = 20) #送测批次
    comment = models.CharField(max_length = 500, blank = True)#备注

    def __str__(self):
        return self.testtype