from django.conf.urls import patterns, url, include
from django.conf.urls import *
from django.views.generic import TemplateView


from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from django.contrib import admin

from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', TemplateView.as_view(template_name='home.html'), name='index' ),
    # Examples:
    #url(r'^pages/', include('django.contrib.flatpages.urls')),
    #url(r'^$', 'pages.views.site', {'alias': 'home'}),

    url(r'^$', include('pages.urls')),

    url(r'^order/', include('orderform.urls')),
    url(r'^site/', include('pages.urls')),
    url(r'^admin/',  include(admin.site.urls)), # admin site
    #url(r'^redactor/', include('redactor.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
)

urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )

handler404 = 'app.views.handler404'
#handler500 = 'devel.views.error5'


if settings.DEBUG:

    if settings.MEDIA_ROOT:

        urlpatterns += static(settings.MEDIA_URL,

            document_root=settings.MEDIA_ROOT)



urlpatterns += staticfiles_urlpatterns()