# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

# TODO remove after creating real view
from django.views import defaults as default_views

app_name = 'tcm'
urlpatterns = [
    # list of orgs. TODO redirect to one specific org?
    url(
        r'^$',
        views.OrganisationList.as_view(),
        name='org-list'
    ),

    # org detail page
    url(
        r'^(?P<org_pk>[\w ]+)/$',
        views.OrganisationDetail.as_view(),
        name='org-detail'
    ),

    # TODO list of org's projects
    url(r'^(?P<org_short>[\w]+)/projects$', default_views.page_not_found, kwargs={'exception': Exception('View yet to be created. ')}),

    # creation of org's projects
    url(
        r'^(?P<org_pk>[\w ]+)/projects/create$',
        views.ProjectCreate.as_view(),
        name='project-create'
    ),

    # project detail page
    url(
        r'^(?P<org_pk>[\w ]+)/projects/(?P<project_pk>[\w ]+)/$',
        views.ProjectDetail.as_view(),
        name='project-detail'
    ),

    # project delete
    url(
        r'^(?P<org_pk>[\w ]+)/projects/(?P<project_pk>[\w ]+)/delete/$',
        views.ProjectDelete.as_view(),
        name='project-delete'
    ),

    # TODO edit project details
    url(r'^(?P<org_short>[\w]+)/projects/(?P<project_id>\d+)/edit$', default_views.page_not_found, kwargs={'exception': Exception('View yet to be created. ')}),

    # TODO list of project's scenarios templates
    url(r'^(?P<org_short>[\w]+)/projects/(?P<project_id>\d+)/scenarios$', default_views.page_not_found, kwargs={'exception': Exception('View yet to be created. ')}),

    # TODO create scenario templates
    url(r'^(?P<org_short>[\w]+)/projects/(?P<project_id>\d+)/scenarios/create$', default_views.page_not_found, kwargs={'exception': Exception('View yet to be created. ')}),

    # scenario template detail page
    url(
        r'^(?P<org_pk>[\w ]+)/projects/(?P<project_pk>[\w ]+)/scenarios/(?P<scenario_pk>\d+)/$',
        views.ScenarioTemplateDetail.as_view(),
        name='scenario-detail',
    ),

    # TODO edit scenario template
    url(r'^(?P<org_short>[\w]+)/projects/(?P<project_id>\d+)/scenarios/(?P<scenario_id>\d+)/edit$', default_views.page_not_found, kwargs={'exception': Exception('View yet to be created. ')}),

    # TODO create scenario template's testcase template
    url(r'^(?P<org_short>[\w]+)/projects/(?P<project_id>\d+)/scenarios/(?P<scenario_id>\d+)$/testcases/create', default_views.page_not_found, kwargs={'exception': Exception('View yet to be created. ')}),

    # test case template detail page
    url(
        r'^(?P<org_pk>[\w ]+)/projects/(?P<project_pk>[\w ]+)/scenarios/(?P<scenario_pk>\d+)/testcases/(?P<testcase_pk>\d+)/$',
        views.TestCaseTemplateDetail.as_view(),
        name='testcase-template-detail',
    ),

    # list of project's testruns
    url(
        r'^(?P<org_pk>[\w ]+)/projects/(?P<project_pk>[\w ]+)/testruns/$',
        views.TestRunList.as_view(),
        name='testrun-list',
    ),

    # testrun detail page
    url(
        r'^(?P<org_pk>[\w ]+)/projects/(?P<project_pk>[\w ]+)/testruns/(?P<testrun_pk>\d+)/$',
        views.TestRunDetail.as_view(),
        name='testrun-detail',
    ),

    # TODO test run edit page
    url(r'^(?P<org_short>[\w]+)/projects/(?P<project_id>\d+)/testruns/(?P<testrun_id>\d+)/edit$', default_views.page_not_found, kwargs={'exception': Exception('View yet to be created. ')}),

    # scenario detail page
    url(
        r'^(?P<org_pk>[\w ]+)/projects/(?P<project_pk>[\w ]+)/testruns/(?P<testrun_pk>\d+)/scenarios/(?P<scenario_pk>\d+)/$',
        views.ScenarioDetail.as_view(),
        name='scenario-detail',
    ),

    # TODO list of testrun's scenarios
    url(r'^(?P<org_short>[\w]+)/projects/(?P<project_id>\d+)/testruns/(?P<testrun_id>\d+)/scenarios$', default_views.page_not_found, kwargs={'exception': Exception('View yet to be created. ')}),

    # TODO edit of testrun's scenarios
    url(r'^(?P<org_short>[\w]+)/projects/(?P<project_id>\d+)/testruns/(?P<testrun_id>\d+)/scenarios/edit$', default_views.page_not_found, kwargs={'exception': Exception('View yet to be created. ')}),

    # TODO list of scenarios's testcases
    url(r'^(?P<org_short>[\w]+)/projects/(?P<project_id>\d+)/testruns/(?P<testrun_id>\d+)/scenarios/(?P<scenario_id>\d+)$', default_views.page_not_found, kwargs={'exception': Exception('View yet to be created. ')}),

    # TODO edit of scenarios's testcases
    url(r'^(?P<org_short>[\w]+)/projects/(?P<project_id>\d+)/testruns/(?P<testrun_id>\d+)/scenarios/(?P<scenario_id>\d+)/edit$', default_views.page_not_found, kwargs={'exception': Exception('View yet to be created. ')}),

]
