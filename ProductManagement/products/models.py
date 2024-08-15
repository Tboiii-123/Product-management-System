from django.db import models
import datetime

# Create your models here.




class Seller(models.Model):

    FirstName = models.CharField(max_length=200)

    LastName =models.CharField(max_length=200)

    number =models.CharField(max_length=11)

    email =models.EmailField()


    Company_code_name =models.CharField(max_length=10)




    def __str__(self):

        return f'{self.FirstName}  {self.LastName}  {self.email}  {self.number}  {self.Company_code_name}'





class Product(models.Model):

    name =models.CharField(max_length=200)

    price1 =models.FloatField()


    def __str__(self):

        return f"{self.name}  "



class Product_detail(models.Model):

    name =models.ForeignKey(Product, on_delete=models.CASCADE)


    price =models.FloatField()

    quantity =models.IntegerField(default=1)

    buyer_name =models.CharField(max_length=300)

    buyer_number =models.CharField(max_length=11)


    payment_status =models.BooleanField(default=False)

    


    buyer_email =models.EmailField()

    price_paid =models.FloatField(blank=True)
    
    price_owing =models.FloatField(blank=True)




    time_bought =models.DateField(default =datetime.datetime.today)








    def __str__(self):
        return f'{self.name}   {self.quantity}   {self.buyer_name}  {self.buyer_number}' 
    















