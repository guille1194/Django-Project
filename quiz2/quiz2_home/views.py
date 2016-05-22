from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, FormView, CreateView, ListView, UpdateView
from .models import Artist, Artwork
from .forms import User_form, Add_Art_Form
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

class index(TemplateView):
	template_name = "blog/index.html"

def home(request):
	context = dict()
	context['arts'] = Artwork.objects.all().order_by('-publish_date')
	# print context
	return render(request, "blog/index.html", context)

class register(FormView):
	template_name = 'blog/register.html'
	form_class = User_form
	success_url = reverse_lazy('art_list')

	def form_valid(self,form):
		user=form.save()
		new_user = authenticate(username=form.cleaned_data['username'],
									password=form.cleaned_data['password1']
									)
		p = Artist()
		p.user_profile = user
		p.mail = form.cleaned_data['mail']
		p.phone = form.cleaned_data['phone']
		p.save()
		login(self.request, new_user)
		return super(register,self).form_valid(form)

def add_art(request):
	if request.method == 'POST':
		form = Add_Art_Form(request.POST or None, request.FILES or None)
		if form.is_valid():
			try:
				instance = form.save()
				instance.save()
				return HttpResponseRedirect('/lista_arte/')
			except:
				print 'An error'
		else:
			form = Add_Art_Form()
			context = { "form": form, 'err': True, }
			return render(request, 'blog/add_art.html', context)
	else:
		form = Add_Art_Form()
		context = { "form": form, }
		return render(request, 'blog/add_art.html', context)

def art_delete(request, id=None):
	art = get_object_or_404(Artwork, id=id)
	art.delete()
	return redirect("blog:art_list")

def art_update(request, id=None):
	art = get_object_or_404(Artwork, id=id)
	form = Add_Art_Form(request.POST or None, request.FILES or None, instance=art)
	if form.is_valid():
		try:
			art = form.save()
			art.save()
			context = {
				"art": art,
			}
			return render(request, "blog/art_detail.html", context)
		except:
			print 'An error'
	context = {
		"object_list": "eee",
		"art": art,
		"form": form,
	}
	return render(request, "blog/art_update.html", context)

def art_detail(request, id=None):
	art = get_object_or_404(Artwork, id=id)
	context = {
		"object_list": "eee",
		"art": art,
	}
	return render(request, "blog/art_detail.html", context)

def art_list(request):
	queryset_list = Artwork.objects.all().order_by('-publish_date')
	paginator = Paginator(queryset_list, 5) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context = {
		"object_list": queryset
	}
	return render(request, "blog/art_list.html", context)

class report_arts(ListView):
	template_name = 'blog/report_arts.html'
	model = Artwork

class report_artist(ListView):
	template_name = 'blog/report_artist.html'
	model = Artist

def search_paintings(request):
	p = Artwork.objects.filter(art_type = 'Painting')
	if p:
		ctx = {'object_list':p}
	else:
		ctx = {'mensaje':'no hay datos'}
	return render(request,'blog/paintings.html',ctx)

def search_photography(request):
	p = Artwork.objects.filter(art_type = 'Photography')
	if p:
		ctx = {'object_list':p}
	else:
		ctx = {'mensaje':'no hay datos'}
	return render(request,'blog/photography.html',ctx)

def search_sculpting(request):
	p = Artwork.objects.filter(art_type = 'Sculpting')
	if p:
		ctx = {'object_list':p}
	else:
		ctx = {'mensaje':'no hay datos'}
	return render(request,'blog/sculpting.html',ctx)

def search_films(request):
	p = Artwork.objects.filter(art_type = 'Film')
	if p:
		ctx = {'object_list':p}
	else:
		ctx = {'mensaje':'no hay datos'}
	return render(request,'blog/films.html',ctx)

class search(TemplateView):
	template_name = "blog/search.html"

	def post(self, request, *arg, **kwargs):
		search = request.POST['search']
		artworks = Artwork.objects.filter(art_name__contains=search)
		artists = Artist.objects.filter(user_profile__username__contains=search)
		if artworks:
			if artists:
				return render(request, 'blog/search.html', {'artworks': artworks, 'artists': artists, 'artist': True, 'artwork': True})
			else:
				return render(request, 'blog/search.html', {'artworks': artworks, 'artist': False, 'artwork': True})
		else:
			return render(request, 'blog/search.html', {'artists': artists, 'artist': True})
