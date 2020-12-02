from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from  crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
import datetime
from django.db.models import *

from .models import User, Listing, Bid, Comment
from .forms import *



def watch_list(request):
    user = User.objects.get(username=request.user.username)
    listings = user.wishlist.all()
    return render(request, "auctions/watch_list.html", {
        'listings': listings
    })



def remove_watchlist(request, listing_id):
    user = User.objects.get(username=request.user.username)
    user.wishlist.remove(Listing.objects.get(pk = listing_id))
    return HttpResponseRedirect("/"+str(listing_id))

    

def add_watchlist(request, listing_id):
    user = User.objects.get(username=request.user.username)
    user.wishlist.add(Listing.objects.get(pk = listing_id))
    return HttpResponseRedirect("/"+str(listing_id))
     

def update_listing(id, price, user):
    listing = Listing.objects.get(pk=id)
    listing.bid = price
    listing.bid_user = user.username
    listing.save()

def close(request, listing_id):
    if request.user.username == Listing.objects.get(pk = listing_id).username:
        l= Listing.objects.get(id = listing_id)
        l.closed=True
        l.save()
    return HttpResponseRedirect(reverse('listing', args =[listing_id]))
    
def listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    bids = Bid.objects.filter(listing=listing_id).count()
    comments = Comment.objects.filter(listing=listing_id)
    user = User.objects.get(username=request.user.username)
    if user.wishlist.filter(id=listing_id).count()>=1:
        watch_list = True
    else:
        watch_list = False
    bid_user = listing.bid_user
    if bid_user==request.user.username:
        message = "Your bid is the current bid"
    else:
        message = "current bid is by: " + str(bid_user)
    if request.method == "POST":
        if 'submit_comment' in request.POST:
            form = comment_form(request.POST)
            if form.is_valid():
                comment = form.cleaned_data['comment']
                Comment(listing = Listing.objects.get(id = listing_id), username = request.user, comment = comment).save()
        elif 'submit_bid' in request.POST:
            form = bid_form(request.POST)
            if form.is_valid():
                bid = form.cleaned_data['bid']
                if bid > listing.bid:
                    Bid(username=request.user, bid = bid, listing = listing).save()
                    update_listing(id=listing_id, price=bid, user = request.user)
                    return HttpResponseRedirect("/"+str(listing_id))
                else:
                    response = "Bid must be greater than the current bid"
                    return render(request, "auctions/listing.html", {'listing': listing,
                'num_bids': bids,'message': message, 'response': response,
                'form' : bid_form(), 'comments': comments, 'watch_list': watch_list, 'comment_form': comment_form()})
            

    return render(request, "auctions/listing.html", {'listing': listing, 'num_bids': bids, 'message': message, 'bid_form' : bid_form(), "comments" : comments, 'watch_list': watch_list, 'comment_form': comment_form()})

    


def index(request):
    return render(request, "auctions/index.html", {'Listings' : Listing.objects.filter(closed=False)})

def create_listing(request):
    if request.method == 'POST': # If the form has been submitted...
        form = listing_form(request.POST) # A form bound to the POST data
        if form.is_valid():
            l = Listing(username = request.user.username,title= form.cleaned_data['title'], bid = form.cleaned_data['price'], desc = form.cleaned_data['desc'], image= form.cleaned_data['image'], time = datetime.datetime.now(), closed = False  )
            l.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/create_listing.html", {'form' : form, 'message' : "Form not valid"})
    else:
        return render(request, "auctions/create_listing.html", {'form' : listing_form()})

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
