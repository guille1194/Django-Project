from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, FormView, CreateView, ListView, UpdateView
from .models import Employees, Profile
from .forms import User_form, Add_Employee_Form
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
	context['employees'] = Employees.objects.all().order_by('-publish_date')
	# print context
	return render(request, "blog/index.html", context)

class register(FormView):
	template_name = 'blog/register.html'
	form_class = User_form
	success_url = reverse_lazy('employee_list')

	def form_valid(self,form):
		user=form.save()
		new_user = authenticate(username=form.cleaned_data['username'],
									password=form.cleaned_data['password1']
									)
		p = Profile()
		p.user_profile = user
		p.mail = form.cleaned_data['mail']
		p.phone = form.cleaned_data['phone']
		p.save()
		login(self.request, new_user)
		return super(register,self).form_valid(form)

def add_employee(request):
	if request.method == 'POST':
		form = Add_Employee_Form(request.POST or None, request.FILES or None)
		if form.is_valid():
			try:
				instance = form.save()
				instance.save()
				return HttpResponseRedirect('/lista_empleados/')
			except:
				print 'An error'
		else:
			form = add_Employee_Form()
			context = { "form": form, 'err': True, }
			return render(request, 'blog/add_employee.html', context)
	else:
		form = Add_Employee_Form()
		context = { "form": form, }
		return render(request, 'blog/add_employee.html', context)

def employee_delete(request, id=None):
	employee = get_object_or_404(Employees, id=id)
	employee.delete()
	return redirect("blog:employee_list")

def employee_update(request, id=None):
	art = get_object_or_404(Employees, id=id)
	form = Add_Employee_Form(request.POST or None, request.FILES or None, instance=employee)
	if form.is_valid():
		try:
			employee = form.save()
			employee.save()
			context = {
				"employee": employee,
			}
			return render(request, "blog/employee_detail.html", context)
		except:
			print 'An error'
	context = {
		"object_list": "eee",
		"employee": employee,
		"form": form,
	}
	return render(request, "blog/employee_update.html", context)

def employee_detail(request, id=None):
	employee = get_object_or_404(Employees, id=id)
	context = {
		"object_list": "eee",
		"employee": employee,
	}
	return render(request, "blog/employee_detail.html", context)

def employee_list(request):
	queryset_list = Employees.objects.all().order_by('-publish_date')
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
	return render(request, "blog/employee_list.html", context)

class report_employee(ListView):
	template_name = 'blog/report_employee.html'
	model = Employees

def search_IT(request):
	p = Employees.objects.filter(employee_department = 'IT')
	if p:
		ctx = {'object_list':p}
	else:
		ctx = {'mensaje':'no hay datos'}
	return render(request,'blog/IT.html',ctx)

def search_electronics(request):
	p = Employees.objects.filter(employee_department = 'Electronics')
	if p:
		ctx = {'object_list':p}
	else:
		ctx = {'mensaje':'no hay datos'}
	return render(request,'blog/electronics.html',ctx)

def search_developer(request):
	p = Employees.objects.filter(employee_department = 'Developer')
	if p:
		ctx = {'object_list':p}
	else:
		ctx = {'mensaje':'no hay datos'}
	return render(request,'blog/developer.html',ctx)

def search_support(request):
	p = Employees.objects.filter(employee_department = 'Support')
	if p:
		ctx = {'object_list':p}
	else:
		ctx = {'mensaje':'no hay datos'}
	return render(request,'blog/support.html',ctx)
