from django.db import models

# Create your models here.

# class Position(models.Model):
#     title = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.title

# class Employee(models.Model):
#     fullname = models.CharField(max_length=100)
#     emp_code = models.CharField(max_length=3)
#     mobile= models.CharField(max_length=15)
class Products(models.Model):
    product_url = models.CharField(max_length=200)
    affiliate_tag = models.CharField(max_length=200)
    def _get_aff_link(self):
        "Returns the person's full name."
        return '{0}&tag={1}'.format(self.product_url,self.affiliate_tag)

    affiliate_url = property(_get_aff_link)
    
