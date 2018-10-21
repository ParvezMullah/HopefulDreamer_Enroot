from django.contrib import admin

from .models import Seller
from usersapp.models import (
    UserProfile
)
# from productsapp.models import (
#     Product, Review, Transactions, Post
# )
from productsapp.models import (
    Product, Post
)
# Register your models here.
admin.site.site_header = ' Admininstration'
admin.site.register(Product)
admin.site.register(UserProfile)
# admin.site.register(Review)
# admin.site.register(WishList)
admin.site.register(Seller)
admin.site.register(Post)
