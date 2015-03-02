from django.conf.urls import patterns, include, url
from HMFcalc import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import RedirectView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'HMF/results/', 'hmf_finder.views.HMF'),
    # url(r'^HMF/$', 'hmf_finder.views.home'),
    # url(r'^HMF_Site/', include('HMF_Site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^favicon\.ico$',
        RedirectView.as_view(url='http://hmfstatic.appspot.com/img/favicon.ico')),
    url(r'^$', \
        views.home.as_view(),
        name='home'),
    url(r'^hmf_finder/form/create/$',
        views.HMFInputCreate.as_view(),
        name='calculate'),
    url(r'^hmf_finder/form/add/$',
        views.HMFInputAdd.as_view(),
        name='calculate'),
    url(r'^hmf_parameters/$',
        views.parameters.as_view(),
        name='parameters'),
#    url(r'^hmf_parameter_discussion/',
#        views.param_discuss.as_view(),
#        name='param-discuss'),
    url(r'^hmf_resources/',
        views.resources.as_view(),
        name='resources'),
    url(r'^hmf_acknowledgments/',
        views.acknowledgments.as_view(),
        name='acknowledgments'),
    url(r'^hmf_finder/hmf_image_page/$',
        views.ViewPlots.as_view(),
        name='image-page'),
    url(r'^hmf_finder/(?P<plottype>\w+).(?P<filetype>\w{3})$',
        'HMFcalc.views.plots',
        name='images'),
#     url(r'^hmf_finder/hmf_image_page/plots.zip$',
#         'HMFcalc.views.hmf_all_plots',
#         name='all-plots'),
    url(r'^hmf_finder/hmf_image_page/allData.zip$',
        'HMFcalc.views.data_output',
        name='data-output'),
    url(r'^hmf_finder/hmf_image_page/parameters.txt$',
        'HMFcalc.views.header_txt',
        name='header-txt'),

    url(r'^contact_info/$',
        views.contact.as_view(),
        name='contact-info'),
    url(r'^contact_info/emailme/$',
        views.ContactFormView.as_view(),
        name='contact-email'),
    url(r'^email-sent/$',
        views.EmailSuccess.as_view(),
        name='email-success'),
    url(r'^hmf_finder/hmf_image_page/halogen.zip$',
        'HMFcalc.views.halogen',
        name='halogen-output'),
#    url(r'^downloads/(?P<name>\w+).(?P<type>\w+)$',
#        'HMFcalc.views.get_code',
#        name='get-code')
    )

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()


