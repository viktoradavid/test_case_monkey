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
