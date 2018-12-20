from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=50)
    last_name = forms.CharField(label='Last name', max_length=50)
    street = forms.CharField(label='Street Address', max_length=50)
    city = forms.CharField(label='City', max_length=100)
    state = forms.ChoiceField(label='State')
    zip = forms.CharField(label='Zip Code', max_length=5)
    phone = forms.CharField(label='Phone Number', max_length=5, required=False)
    email = forms.EmailField(label='Email', max_length=50, required=False)
    title = forms.ChoiceField(label='Email')
    use_mail = forms.BooleanField()
    use_phone = forms.BooleanField()
    use_email = forms.BooleanField()
