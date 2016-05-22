from django.conf.urls import include, url, patterns
from .views import index, register, home, add_employee, employee_list, employee_detail, employee_update, employee_delete, report_employee, search_IT, search_developer, search_electronics, search_support

urlpatterns = [

    url(r'^$', employee_list, name='employee_list'),
    url(r'^lista_empleados/$', employee_list, name='employee_list'),
    url(r'^registrar/$', register.as_view(), name='register'),
    url(r'^indice/$', index.as_view(), name='index'),
    url(r'^home/$', employee_list, name='employee_list'),

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'blog/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),

    url(r'^agregar_empleado/$', add_employee, name='add_employee'),
    url(r'^employee_detail/(?P<id>\d+)/$', employee_detail, name='employee_detail'),
    url(r'^employee_detail/(?P<id>\d+)/edit/$', employee_update, name='employee_update'),
    url(r'^employee_delete/(?P<id>\d+)/$', employee_delete, name='employee_delete'),

    url(r'^reportes_empleados/$',report_employee.as_view(), name = 'report_employee_view'),

    url(r'^IT/$', search_IT, name = 'search_IT'),
    url(r'^electronica/$', search_electronics, name = 'search_electronics'),
    url(r'^desarrollador/$', search_developer, name = 'search_developer'),
    url(r'^soporte/$', search_support, name = 'search_support'),

]
