from . import models
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404


class OrganisationList(ListView):
    model = models.Organisation
    context_object_name = 'organisations'


class OrganisationDetail(DetailView):
    model = models.Organisation
    context_object_name = 'organisation'

    def get_context_data(self, **kwargs):
        context = super(OrganisationDetail, self).get_context_data(**kwargs)
        return context
