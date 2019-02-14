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

def thanks(request):
	return render(request, 'contactList/thanks.html')

class FormView(generic.edit.FormView):
    template_name = 'contactList/mailer.html'
    form_class = ContactForm
    success_url = '../thanks/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
