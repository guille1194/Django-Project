from django.db import models
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser
from django.core.urlresolvers import reverse

# Create your models here.
class Profile(models.Model):
	user_profile = models.OneToOneField(User)
	mail = models.EmailField()
	phone = models.IntegerField()

	def __unicode__(self):
		return self.user_profile.username

class Employees(models.Model):
    employee_name = models.CharField(max_length=50)
    employee_last_name = models.CharField(max_length=50)
    employee_number = models.DecimalField(max_digits=6, decimal_places=0)
    employee_department = models.CharField(max_length=60, null=True, blank=True)
    employee_work_hours = models.IntegerField()
    employee_wages = models.DecimalField(max_digits=8, decimal_places=2)
    publish_date = models.DateTimeField(auto_now_add=True, auto_now=False)
