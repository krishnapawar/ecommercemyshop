from django.db import models

# Create your models here.
class addproduct(models.Model):
	pro_id = models.AutoField
	pro_name = models.CharField(max_length=50, default="")
	category = models.CharField(max_length=30, default="")
	subcategory = models.CharField(max_length=30, default="")
	price = models.IntegerField()
	desc = models.CharField(max_length=300, default="")
	pub_date = models.DateField()
	pro_image = models.ImageField(upload_to="shop/images", default="")

	def __str__(self):
		return self.pro_name


class contact(models.Model):
	msg_id = models.AutoField(primary_key = True)
	name = models.CharField(max_length=50, default="")
	email = models.CharField(max_length=70, default="")
	phone = models.CharField(max_length=20, default="")
	desc = models.CharField(max_length=500, default="")

	def __str__(self):
		return self.name

class orders(models.Model):
	order_id = models.AutoField(primary_key = True,)
	items_json = models.CharField(max_length=5000 , default="")
	name = models.CharField(max_length=50, default="")
	email = models.CharField(max_length=70, default="")
	address = models.CharField(max_length=260, default="")
	city = models.CharField(max_length=40, default="")
	zip_code = models.CharField(max_length=10, default="")
	phone = models.CharField(max_length=20, default="")

	def __str__(self):
		return self.name + ', ' + self.address+', ' + self.city


class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."