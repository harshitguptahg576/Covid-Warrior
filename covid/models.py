from django.db import models

# class Medicine(models.Model):
#     medicine_id = models.AutoField
#     medicine_name= models.CharField(max_length=30)
#     medicine_desc= models.CharField(max_length=300)
#     medicine_price= models.IntegerField(default=0)
#     medicine_image= models.ImageField(upload_to="static\images", height_field="200px", width_field="200px", default="")

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    product_desc= models.CharField(max_length=300)
    product_price= models.IntegerField()
    product_image= models.ImageField(upload_to="static\images")
    link=models.CharField(max_length=200, default="www.amazon.com")
    def __str__(self):
        return self.product_name


class Center(models.Model):
    center_id = models.AutoField
    hospital_name = models.CharField(max_length=70)
    city = models.CharField(max_length=30)
    pincode = models.CharField(max_length=6)
    address = models.CharField(max_length=70)
    public = models.BooleanField()
    mobile = models.CharField(max_length=10)
    date = models.DateField(auto_now=True)
    hospital_image = models.ImageField(upload_to="static\images\hosp")

    total_iso_bed = models.SmallIntegerField()
    iso_bed = models.SmallIntegerField()

    total_oxy_bed = models.SmallIntegerField()
    oxy_bed = models.SmallIntegerField()

    total_icu_bed = models.SmallIntegerField()
    icu_bed = models.SmallIntegerField()


    def __str__(self):
        return self.hospital_name

# class State(models.Model):

#     state=models.CharField(max_length=20)

#     def __str__(self):
#         return self.state