from django.conf.urls import url
from . import views
urlpatterns = [url(r'^$',views.index,name='index'),url(r'contact',views.contact,name='contact'),url(r'home',views.home,name='home'),url(r'gk',views.gk,name='gk'),url(r'about',views.about,name='about'),url(r'books_links',views.books_links,name='E_books & links'),]

