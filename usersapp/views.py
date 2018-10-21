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
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import UserProfile

from sellersapp.models import Seller
from productsapp.models import Product, Post


class UserProfileCreate(SuccessMessageMixin, CreateView):
    model = UserProfile
    fields = [f.name for f in UserProfile._meta.get_fields()]
    fields.remove('id')
    fields.remove('userid')
    fields.remove('rating_number')
    fields.remove('rating')
    template_name = 'usersapp/userprofile.html'
    success_message = 'Added successully.'
    success_url = '/usersapp/createuser'

    def form_valid(self, form):
        form.instance.userid = self.request.user.id
        return super(UserProfileCreate, self).form_valid(form)


def home(request):
    template = 'usersapp/index.html'
    return render(request, template)


class SellerProfileCreate(SuccessMessageMixin, CreateView):
    model = Seller
    fields = [f.name for f in Seller._meta.get_fields()]
    fields.remove('id')
    fields.remove('userid')
    fields.remove('rank')
    template_name = 'usersapp/sellerprofile.html'
    success_message = 'Added successully.'
    success_url = '/usersapp/createseller'

    def form_valid(self, form):
        form.instance.userid = self.request.user.id
        return super(SellerProfileCreate, self).form_valid(form)


class ProductCreate(SuccessMessageMixin, CreateView):
    model = Product
    fields = [f.name for f in Product._meta.get_fields()]
    fields.remove('product_id')
    fields.remove('seller_id')
    fields.remove('date_first_available')
    template_name = 'usersapp/addproduct.html'
    success_message = 'Added successully.'
    success_url = '/usersapp/addproduct'

    def form_valid(self, form):
        print('Dummy')
        form.instance.seller_id = self.request.user.id
        return super(ProductCreate, self).form_valid(form)

    def form_invalid(self, form):
        print("form is invalid")
        return HttpResponse("form is invalid.. this is just an HttpResponse object")


class ProductCreate(SuccessMessageMixin, CreateView):
    model = Product
    fields = [f.name for f in Product._meta.get_fields()]
    fields.remove('product_id')
    fields.remove('seller_id')
    fields.remove('date_first_available')
    template_name = 'usersapp/addproduct.html'
    success_message = 'Added successully.'
    success_url = '/usersapp/addproduct'

    def form_valid(self, form):
        print('Dummy')
        form.instance.seller_id = self.request.user.id
        return super(ProductCreate, self).form_valid(form)


class PostCreate(SuccessMessageMixin, CreateView):
    model = Post
    fields = [f.name for f in Post._meta.get_fields()]
    fields.remove('post_id')
    fields.remove('user_id')
    fields.remove('date_published')
    template_name = 'usersapp/addpost.html'
    success_message = 'Added successully.'
    success_url = '/usersapp/addpost'

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super(PostCreate, self).form_valid(form)


class PostListView(ListView):
    model = Post
    template_name = "usersapp/postview.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = super(PostListView, self).get_queryset()
        search_text = self.request.GET.get('search', None)
        if search_text != None:
            queryset = queryset.filter(
                lost_or_found=lostorfound, title__icontains=search_text)

        return queryset


class ProductListView(ListView):
    model = Product
    template_name = "usersapp/dummy.html"
    paginate_by = 12

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        return queryset


class PostListView(ListView):
    model = Post
    template_name = "usersapp/postview.html"
    paginate_by = 12

    def get_queryset(self):
        queryset = super(PostListView, self).get_queryset()
        return queryset
