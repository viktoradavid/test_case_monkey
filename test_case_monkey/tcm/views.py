from . import models
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

# TODO check user permissions


class OrganisationList(ListView):
    model = models.Organisation
    context_object_name = 'organisations'


class OrganisationDetail(DetailView):
    model = models.Organisation
    context_object_name = 'organisation'
    pk_url_kwarg = 'org_pk'

    def get_context_data(self, **kwargs):
        context = super(OrganisationDetail, self).get_context_data(**kwargs)
        return context


class ProjectDetail(DetailView):
    model = models.Project
    context_object_name = 'project'
    pk_url_kwarg = 'project_pk'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetail, self).get_context_data(**kwargs)

        # check parent organisation exists, otherwise return 404
        parent_org = get_object_or_404(models.Organisation,
                                       name=self.kwargs['org_pk'])

        return context


class ScenarioTemplateDetail(DetailView):
    model = models.TestScenarioTemplate
    context_object_name = 'scenario'
    pk_url_kwarg = 'scenario_pk'

    def get_context_data(self, **kwargs):
        context = super(ScenarioTemplateDetail, self).get_context_data(**kwargs)

        # check if scenario is listed in given project and organisation,
        # otherwise return 404
        parent_project = get_object_or_404(models.Project,
                                           name=self.kwargs['project_pk'])
        parent_org = get_object_or_404(models.Organisation,
                                       name=self.kwargs['org_pk'])
        if parent_project not in parent_org.projects.all():
            pass
            # TODO return 404

        return context


class TestCaseTemplateDetail(DetailView):
    model = models.TestCaseTemplate
    context_object_name = 'testcase'
    pk_url_kwarg = 'testcase_pk'

    def get_context_data(self, **kwargs):
        context = super(TestCaseTemplateDetail, self).get_context_data(**kwargs)

        # check if scenario is listed in given project and organisation,
        # otherwise return 404
        parent_scenario_template = get_object_or_404(
            models.TestScenarioTemplate,
            id=self.kwargs['scenario_pk'])
        parent_project = get_object_or_404(models.Project,
                                           name=self.kwargs['project_pk'])
        parent_org = get_object_or_404(models.Organisation,
                                       name=self.kwargs['org_pk'])
        if parent_scenario_template not in parent_project.scenarios.all():
            pass
            # TODO return 404
        if parent_project not in parent_org.projects.all():
            pass
            # TODO return 404

        return context


class TestRunDetail(DetailView):
    model = models.TestRun
    context_object_name = 'testrun'
    pk_url_kwarg = 'testrun_pk'

    def get_context_data(self, **kwargs):
        context = super(TestRunDetail, self).get_context_data(**kwargs)

        # check if scenario is listed in given project and organisation,
        # otherwise return 404
        parent_project = get_object_or_404(models.Project,
                                           name=self.kwargs['project_pk'])
        parent_org = get_object_or_404(models.Organisation,
                                       name=self.kwargs['org_pk'])
        if parent_project not in parent_org.projects.all():
            pass
            # TODO return 404

        return context


class TestRunList(ListView):
    model = models.TestRun
    context_object_name = 'testruns'

    def get_context_data(self, **kwargs):
        context = super(TestRunList, self).get_context_data(**kwargs)

        # check if testrun is listed in given project and organisation,
        # otherwise return 404
        parent_project = get_object_or_404(models.Project,
                                           name=self.kwargs['project_pk'])
        parent_org = get_object_or_404(models.Organisation,
                                       name=self.kwargs['org_pk'])
        if parent_project not in parent_org.projects.all():
            pass
            # TODO return 404

        return context


class ScenarioDetail(DetailView):
    model = models.TestScenario
    context_object_name = 'scenario'
    pk_url_kwarg = 'scenario_pk'

    def get_context_data(self, **kwargs):
        context = super(ScenarioDetail, self).get_context_data(**kwargs)

        # check if scenario is listed in given project and organisation,
        # otherwise return 404
        parent_testrun = get_object_or_404(models.TestRun,
                                           id=self.kwargs['testrun_pk'])
        parent_project = get_object_or_404(models.Project,
                                           name=self.kwargs['project_pk'])
        parent_org = get_object_or_404(models.Organisation,
                                       name=self.kwargs['org_pk'])

        if parent_project not in parent_org.projects.all() \
                or parent_testrun not in parent_project.testruns.all():
            pass
            # TODO return 404

        return context
