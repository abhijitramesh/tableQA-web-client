from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from agent import views


urlpatterns = [
    url(r'^$', views.simple_upload, name='simple_upload'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)