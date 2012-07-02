from django.conf.urls.defaults import *

urlpatterns = patterns('howisit',
     (r'^howisit/', 'backups.views.mostra_status'),
)

