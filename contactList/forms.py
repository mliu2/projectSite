from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name',
        'last_name',
        'street',
        'city',
        'state',
        'zip',
        'phone',
        'email',
        'title',
        'use_mail',
        'use_phone',
        'use_email']
        exclude = ['latitude','longitude']

    #first_name = forms.CharField(label='First name', max_length=50)
    #last_name = forms.CharField(label='Last name', max_length=50)
    #street = forms.CharField(label='Street Address', max_length=50,required=False)
    #city = forms.CharField(label='City', max_length=100,required=False)
    #state = forms.ChoiceField(label='State', choices=Contact.STATE_CHOICES)
    #zip = forms.CharField(label='Zip Code', max_length=5,required=False)
    #phone = forms.CharField(label='Phone Number', max_length=5, required=False)
    #email = forms.EmailField(label='Email', max_length=50, required=False)
    #title = forms.ChoiceField(label='Title', choices=Contact.TITLE_CHOICES)
    #use_mail = forms.BooleanField(required=False)
    #use_phone = forms.BooleanField(required=False)
    #use_email = forms.BooleanField(required=False)

    #def save(self, commit=True):
        #data = self.cleaned_data
        #data.save()
