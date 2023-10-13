from django.db import models

# Create your models here.
class Categorgy(models.Model):
    slug=models.CharField(max_length=50,null=False,blank=False)
    name=models.CharField(max_length=50,null=False,blank=False)
    image=models.ImageField(upload_to="images",null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=defualt,1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=defualt,1=Hidden")
    def __str__(self):
        return self.name

 
class Product(models.Model):
    categorgy=models.ForeignKey(Categorgy,on_delete=models.CASCADE)
    slug=models.CharField(max_length=50,null=False,blank=False)
    name=models.CharField(max_length=50,null=False,blank=False)
    image=models.ImageField(upload_to="images",null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=defualt,1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=defualt,1=Hidden")
    description=models.CharField(max_length=500,null=False,blank=False)
    quanty=models.IntegerField(null=False,blank=False)
    orignalprice=models.FloatField(null=False,blank=False)
    sellingprice=models.FloatField(null=False,blank=False)

     
    def __str__(self):
            return self.name

def get_file_path(request,filename):
    orginal_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename ="%s%s" % (nowTime,orginal_filename)
    return os.path.join('uploads/',filename)