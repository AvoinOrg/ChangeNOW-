from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import TemplateView, ListView, DetailView, View, CreateView
from django.views.generic.edit import FormView
from prototype.models import Offer
from prototype.models import Bid
from prototype.forms import UserForm
from prototype.forms import BidForm

# Create your views here.
class Index(FormView):
    form_class = UserForm
    success_url = '/prototype/account/'
    template_name = 'templates/index.html'
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
    
class Offers(ListView):
    model = Offer
        
class Offers(ListView):
    model = Offer

class Bidding(FormView):
    model = Bid
    success_url = '/account/'
    template_name = 'templates/index.html'
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)

