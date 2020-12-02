from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("<int:listing_id>", views.listing, name="listing"),
    path("watch_list", views.watch_list, name="watch_list"),
    path("<int:listing_id>/add_to_watchlist", views.add_watchlist, name="add_watchlist"),
    path("<int:listing_id>/remove_watchlist", views.remove_watchlist, name="remove_watchlist"),
]
