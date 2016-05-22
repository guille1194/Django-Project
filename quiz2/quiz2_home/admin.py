from django.contrib import admin
from .models import Artist, Artwork
# Register your models here.

class ArtworkInline(admin.StackedInline):
	model = Artwork
	extra = 2

class ArtistAdmin(admin.ModelAdmin):
	fieldsets = [
		('Name', {'fields': ['user_profile']}),
		('Contact', {'fields': ['mail', 'phone'], 'classes': ['collapse']})
	]
	inlines = [ArtworkInline]


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Artwork)
