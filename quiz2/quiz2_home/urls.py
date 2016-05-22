from django.conf.urls import include, url, patterns
from .views import index, register, search, home, add_art, art_list, art_detail, art_delete, report_arts, report_artist, search_paintings, search_photography, search_sculpting, search_films, art_update

urlpatterns = [

    url(r'^$', art_list, name='art_list'),
    url(r'^lista_arte/$', art_list, name='art_list'),
    url(r'^registrar/$', register.as_view(), name='register'),
    url(r'^indice/$', index.as_view(), name='index'),
    url(r'^home/$', art_list, name='art_list'),
    url(r'^busqueda/$', search.as_view(), name='search'),

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'blog/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),

    url(r'^agregar_arte/$', add_art, name='add_art'),
    url(r'^art_detail/(?P<id>\d+)/$', art_detail, name='art_detail'),
    url(r'^art_detail/(?P<id>\d+)/edit/$', art_update, name='art_update'),
    url(r'^art_delete/(?P<id>\d+)/$', art_delete, name='art_delete'),

    url(r'^reportes_obras/$',report_arts.as_view(), name = 'report_arts_view'),
    url(r'^reportes_artistas/$',report_artist.as_view(), name = 'report_artist_view'),

    url(r'^pinturas/$', search_paintings, name = 'search_paintings'),
    url(r'^fotografia/$', search_photography, name = 'search_photography'),
    url(r'^escultura/$', search_sculpting, name = 'search_sculpting'),
    url(r'^peliculas/$', search_films, name = 'search_films'),

]
