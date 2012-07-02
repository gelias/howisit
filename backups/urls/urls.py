from django.conf.urls.defaults import *
from backups.views import *

urlpatterns = patterns('',
    
    (r'^status/', 'mostra_status'),
)
