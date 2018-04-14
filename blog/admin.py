from django.contrib import admin

# Register your models here.
from .models import testrecord,crudeex,bact,cpd
#class metaAdmin(admin.ModelAdmin):
#    list_display = ['metabolomics', 'mz', 'rt', 'provider', 'updatetime']
admin.site.register(testrecord)
admin.site.register(crudeex)
admin.site.register(bact)
admin.site.register(cpd)

class testrecordAdmin(admin.ModelAdmin):
    list_display = ['samplename', 'solvent','provider','department','sendtime']
    