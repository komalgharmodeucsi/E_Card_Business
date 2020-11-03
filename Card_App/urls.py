from django.contrib import admin
from django.urls import path
from Card_App import views
#from .views import Login
from django.conf import settings
from django.conf.urls.static import static




pp_name = 'Card_App'

urlpatterns = [
    path('logg', views.sign, name='sign'),
    path('reg', views.person, name='person'),
    path('log', views.log, name='log'),
    ####################################################
    path('temp', views.index, name ='index'),
    #############################################
    path("photo", views.design, name="design"),
    path("edit", views.edit, name="edit"),
    path("mcard", views.mngcard, name="MangeCard"),
    path('new', views.new, name ='new'),
    path("slected", views.selectedimg, name='selectedimg')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
