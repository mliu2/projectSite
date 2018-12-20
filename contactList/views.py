from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Contact
from .forms import ContactForm

class IndexView(generic.ListView):
	template_name = 'contactList/index.html'
	context_object_name = 'contact_list'

	def get_queryset(self):
		return Contact.objects.order_by('last_name')

class FormView(generic.edit.FormView):
    template_name = 'contactList/index.html'
    form_class = 'ContactForm'
    success_url = ''
