from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Contact
from .config import MapBoxConfig

class ContactList(generic.ListView):
	template_name = 'contactList/index.html'
	context_object_name = 'contact_list'

	def get_queryset(self):
		return Contact.objects.order_by('last_name'),MapBoxConfig.access_token

def thanks(request):
	return render(request, 'contactList/thanks.html')

class ContactCreate(generic.edit.CreateView):
    model = Contact
    success_url = '../thanks/'
    fields = '__all__'

class ContactUpdate(generic.edit.UpdateView):
    model = Contact
    success_url = '../'
    fields = '__all__'

class ContactDelete(generic.edit.DeleteView):
    model = Contact
    success_url = '../'
