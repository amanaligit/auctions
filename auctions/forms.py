from django.db.models import *
from django import forms
from  crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import User, Listing, Bid, Comment


class listing_form(forms.Form):
    title = forms.CharField(label="Title \n")
    price = forms.IntegerField(label="Starting Price")
    desc =  forms.CharField(widget=forms.Textarea, label="Something about the Product")
    image = forms.URLField(label = "Optional URL of the image", required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            'title',
            'price',
            'desc',
            'image',
            Submit('submit', 'Submit', css_class = "btn-btn-primary")
        )

class bid_form(forms.Form):
    bid = forms.IntegerField(label=" Enter your bid")


class comment_form(forms.Form):
    
    
    comment = forms.CharField(label=" Comment", widget=forms.Textarea, required=False)
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            'comment',
            Submit('submit_comment', 'Post comment', css_class = "btn-btn-primary")
        )