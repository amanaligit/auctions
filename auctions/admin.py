from django.contrib import admin
from .models import Listing, User, bid, comment
# Register your models here.

admin.site.register(Listing)
admin.site.register(User)
admin.site.register(bid)
admin.site.register(comment)

