from django.db import models

# Create your models here.



# user_name, heartPulse, dhtTemp, dhtHum, gyroX, gyroY, gyroZ, acceleroX, acceleroY, acceleroZ  

class SensorData(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    pub_date = models.DateField()
    pub_time = models.CharField(max_length=10, default="")


    heartPulse = models.IntegerField(default=0)

    dhtTemp = models.IntegerField(default=0)
    dhtHum  = models.IntegerField(default=0)

    # send in list
    gyroX = models.FloatField(default=0)
    gyroY = models.FloatField(default=0)
    gyroZ = models.FloatField(default=0)
    
    # send in list
    acceleroX = models.FloatField(default=0)
    acceleroY = models.FloatField(default=0)
    acceleroZ = models.FloatField(default=0)



    def __str__(self):
        return f'{self.id}- {self.user_name} {self.pub_date} - heartPulse : {self.heartPulse}'



class UserData(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    api_key = models.CharField(max_length=200)
    
    pub_date = models.DateField()


    def __str__(self):
        return f'{self.id}- {self.user_name} {self.pub_date}'



# class Product(models.Model):
#     Product_id = models.AutoField(primary_key=True)
#     product_name = models.CharField(max_length=50)
#     category = models.CharField(max_length=50, default="")
#     slug = models.CharField(max_length=100, default="")
#     price = models.IntegerField(default=0)
#     desc = models.CharField(max_length=300)
#     image = models.ImageField(upload_to="tze/images", default="")
#     testimoniallink = models.CharField(max_length=300, default="")
#     ytlink = models.CharField(max_length=300, default="")
#     benifits = models.CharField(max_length=300, default="")
#     how_to_use = models.CharField(max_length=400, default="")
#     doc_link = models.CharField(max_length=300, default="")
#     net_Qty = models.CharField(max_length=100, default="")
#     pack_of = models.CharField(max_length=50, default="")
#     # pub_date = models.DateField()
#     # subcategory = models.CharField(max_length=30, default="")

#     def __str__(self):
#         return self.product_name
    
# # mem: member
# class Contact(models.Model):
#     mem_id = models.AutoField(primary_key=True)

#     mem_name = models.CharField(max_length=60, default="")
#     mem_image = models.ImageField(upload_to="tze/contactImages", default="")
#     mem_desc = models.CharField(max_length=300, default="")
#     mem_email = models.CharField(max_length=100, default="")
#     mem_phone = models.IntegerField(default=0)
#     mem_fb_link = models.CharField(max_length=100, default="")
#     mem_IG_link = models.CharField(max_length=100, default="")
#     mem_status = models.CharField(max_length=100, default="")
#     mem_tag = models.CharField(max_length=20, default="")

#     def __str__(self):
#         return self.mem_name
    
# class Contact(models.Model):
#     msg_id = models.AutoField(primary_key=True)

#     name = models.CharField(max_length=50, default="")
#     email = models.CharField(max_length=70, default="")
#     phone = models.IntegerField(default=0)
#     msg = models.CharField(max_length=500, default="")


#     def __str__(self):
#         return self.name