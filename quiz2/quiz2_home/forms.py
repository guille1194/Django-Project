from django import forms
from django.forms import ModelForm
from .models import Artist, Artwork
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

class Add_Art_Form(forms.ModelForm):
	class Meta:
		model = Artwork
		fields = '__all__'

	def clean(self):
		print self.cleaned_data
		return self.cleaned_data


class User_form(UserCreationForm):
	mail = forms.CharField(max_length=100)
	phone = forms.IntegerField()
