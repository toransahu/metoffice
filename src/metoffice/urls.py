from django.conf.urls import url
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'store'

#doing changes to implement Generic Views

urlpatterns = [
    url(r'^load$', views.main, name='main'),
    url(r'^climate$', views.graph_climate, name='graph_climate'),
    url(r'^weather$', views.graph_weather, name='graph_weather'),
]

#urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
