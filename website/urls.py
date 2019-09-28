
from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index_view'),
    path('about', about, name='about_view'),
    path('datascience', datascience, name='datascience_view'),
    path('software', software, name='software_view'),
    path('cloud', cloud, name='cloud_view'),
    path('cyber', cyber, name='cyber_view'),
    path('digital', digital, name='digital_view'),
    path('testing', testing, name='testing_view'),
    path('development', development, name='development_view'),
    path('itconsultancy', itconsultancy, name='itconsultancy_view'),
    path('contact', contact, name='contact_view'),
]