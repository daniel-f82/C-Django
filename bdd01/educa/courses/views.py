from braces.views import CsrfExemptMixin ,  JsonRequestResponseMixin
from django.apps import apps

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)

from django.forms.models import modelform_factory
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import ModuleFormSet
from .models import Content, Course, Module

class OwnerMixin:
     def get_queryset(self):
         qs = super().get_queryset()
         return qs.filter(owner=self.request.user)
    

class OwnerEditMixin:
    def form_valid(self, form):
          form.instance.owner = self.request.user
          return super().form_valid(form)
      
class OwnerCourseMixin(
     OwnerMixin , LoginRequiredMixin, PermissionRequiredMixin
):
     model = Course
     fiels = ['subject', 'title', 'slug', 'overview']
     success_url = reverse_lazy('manage_course_list')

