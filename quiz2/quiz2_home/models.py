from django.db import models
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser
from django.core.urlresolvers import reverse
from PIL import Image, ImageOps
# Create your models here.
class Artist(models.Model):
	user_profile = models.OneToOneField(User)
	mail = models.EmailField()
	phone = models.IntegerField()

	def __unicode__(self):
		return self.user_profile.username

class Artwork(models.Model):
	artist = models.ForeignKey(Artist)
	art_name = models.CharField(max_length=50)
	art_photo = models.ImageField(upload_to='art_gallery/', null=True, blank=True)
	description = models.TextField(max_length=200)
	art_type = models.CharField(max_length=50, null=True, blank=True)
	update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
	publish_date = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return 'author: %s art: %s' %(self.artist.user_profile.username, self.art_name)

	def get_absolute_url(self):
		return reverse("art_detail", kwargs={"id": self.id})
