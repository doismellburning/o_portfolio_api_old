from django.conf import settings
from django.conf.urls import *
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView

from .views import EntryEndpoint, UserEndpoint


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^favicon.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'favicon.ico')),

    url(r'^user/$', UserEndpoint.as_view(), name='user'),
    url(r'^entry/$', EntryEndpoint.as_view(), name='entry'),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

)

urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

