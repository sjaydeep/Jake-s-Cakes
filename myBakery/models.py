from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField( default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 0 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")   
    shop_name = models.CharField(max_length=50, default="")
    shop_address = models.CharField(max_length=500, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='static/img', default="")

    def __str__(self):
        return self.product_name

class BirthdayProduct(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")   
    shop_name = models.CharField(max_length=50, default="")
    shop_address = models.CharField(max_length=500, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='static/img', default="")

    def __str__(self):
        return self.product_name


class WeddingProduct(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")   
    shop_name = models.CharField(max_length=50, default="")
    shop_address = models.CharField(max_length=500, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='static/img', default="")

    def __str__(self):
        return self.product_name



class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    phone = models.BigIntegerField()
    desc = models.TextField(max_length=2000)
    date = models.DateField()

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key = True)
    items_json = models.CharField(max_length=5000)
    fname = models.CharField(max_length=111)
    lname = models.CharField( max_length=111 )
    email = models.CharField( max_length=111 )
    address = models.CharField( max_length=111 )
    phone = models.CharField( max_length=111, default="" )
    state = models.CharField( max_length=111 )
    city = models.CharField( max_length=111 )
    zip_code = models.CharField( max_length=111 )

class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."

