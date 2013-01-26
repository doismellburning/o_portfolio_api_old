from django.conf import settings
from django.conf.urls import *
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView, TemplateView
from rest_framework.authtoken.views import ObtainAuthToken

from .views import EntryEndpoint, EntryListEndpoint, UserEndpoint, UserRegistrationEndpoint


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^favicon.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'favicon.ico')),

    url(r'^login/$', ObtainAuthToken.as_view(), name='login'),
    url(r'^register/$', UserRegistrationEndpoint.as_view(), name='register'),
    url(r'^users/$', UserEndpoint.as_view(), name='user'),
    url(r'^entries/$', EntryListEndpoint.as_view(), name='entry'),
    url(r'^entries/(?P<pk>\d)/$', EntryEndpoint.as_view(), name='entry'),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

)

urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

