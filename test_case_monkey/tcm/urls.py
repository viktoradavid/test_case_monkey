# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

# TODO remove after creating real view
from django.views import defaults as default_views

urlpatterns = [
    # list of orgs. TODO redirect to one specific org?
    url(
        r'^$',
        views.OrganisationList.as_view(),
        name='org-list'
    ),

    # org detail page
    url(
        r'^(?P<pk>[\w]+)/$',
        views.OrganisationDetail.as_view(),
        name='org-detail'
    ),

    # TODO list of org's projects
    url(r'^(?P<org_short>[\w]+)/projects$', default_views.page_not_found, kwargs={'exception': Exception('View yet to be created. ')}),

    # TODO creation of org's projects
    url(r'^(?P<org_short>[\w]+)/projects/create$', default_views.page_not_found, kwargs={'exception': Exception('View yet to be created. ')}),

    # TODO edit project details
    url(r'^(?P<org_short>[\w]+)/projects/(?P<project_id>\d+)/edit$', default_views.page_not_found, kwargs={'exception': Exception('View yet to be created. ')}),

    # TODO list of project's scenarios templates
    url(r'^(?P<org_short>[\w]+)/projects/(?P<project_id>\d+)/scenarios$', default_views.page_not_found, kwargs={'exception': Exception('View yet to be created. ')}),

    # TODO create scenario templates
    url(r'^(?P<org_short>[\w]+)/projects/(?P<project_id>\d+)/scenarios/create$', default_views.page_not_found, kwargs={'exception': Exception('View yet to be created. ')}),

    # TODO list of scenarios's testcases templates
    url(r'^(?P<org_short>[\w]+)/projects/(?P<project_id>\d+)/scenarios/(?P<scenario_id>\d+)$', default_views.page_not_found, kwargs={'exception': Exception('View yet to be created. ')}),

    # TODO edit scenario template
    url(r'^(?P<org_short>[\w]+)/projects/(?P<project_id>\d+)/scenarios/(?P<scenario_id>\d+)/edit$', default_views.page_not_found, kwargs={'exception': Exception('View yet to be created. ')}),

    # TODO create scenario's testcase template
    url(r'^(?P<org_short>[\w]+)/projects/(?P<project_id>\d+)/scenarios/(?P<scenario_id>\d+)$/create', default_views.page_not_found, kwargs={'exception': Exception('View yet to be created. ')}),

    # TODO list of project's testruns
    url(r'^(?P<org_short>[\w]+)/projects/(?P<project_id>\d+)/testruns$', default_views.page_not_found, kwargs={'exception': Exception('View yet to be created. ')}),

    # TODO test run detail page
    url(r'^(?P<org_short>[\w]+)/projects/(?P<project_id>\d+)/testruns/(?P<testrun_id>\d+)$', default_views.page_not_found, kwargs={'exception': Exception('View yet to be created. ')}),

    # TODO test run edit page
    url(r'^(?P<org_short>[\w]+)/projects/(?P<project_id>\d+)/testruns/(?P<testrun_id>\d+)/edit$', default_views.page_not_found, kwargs={'exception': Exception('View yet to be created. ')}),

    # TODO list of testrun's scenarios
    url(r'^(?P<org_short>[\w]+)/projects/(?P<project_id>\d+)/testruns/(?P<testrun_id>\d+)/scenarios$', default_views.page_not_found, kwargs={'exception': Exception('View yet to be created. ')}),

    # TODO edit of testrun's scenarios
    url(r'^(?P<org_short>[\w]+)/projects/(?P<project_id>\d+)/testruns/(?P<testrun_id>\d+)/scenarios/edit$', default_views.page_not_found, kwargs={'exception': Exception('View yet to be created. ')}),

    # TODO list of scenarios's testcases
    url(r'^(?P<org_short>[\w]+)/projects/(?P<project_id>\d+)/testruns/(?P<testrun_id>\d+)/scenarios/(?P<scenario_id>\d+)$', default_views.page_not_found, kwargs={'exception': Exception('View yet to be created. ')}),

    # TODO edit of scenarios's testcases
    url(r'^(?P<org_short>[\w]+)/projects/(?P<project_id>\d+)/testruns/(?P<testrun_id>\d+)/scenarios/(?P<scenario_id>\d+)/edit$', default_views.page_not_found, kwargs={'exception': Exception('View yet to be created. ')}),

]
