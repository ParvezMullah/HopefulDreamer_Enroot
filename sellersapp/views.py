from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

from .models import Seller


class SellerCreate(SuccessMessageMixin, CreateView):
    model = Seller
    fields = fields = [f.name for f in Seller._meta.get_fields()]
    fields.remove('id')
    fields.remove('userid')
    template_name = ''
    success_message = 'Added successully.'
    success_message = ''

    def form_valid(self, form):
        form.instance.userid = self.request.user.id
        return super(SellerCreate, self).form_valid(form)
