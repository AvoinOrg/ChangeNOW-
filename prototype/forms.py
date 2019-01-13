from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=30)
    address = forms.CharField(label='Your address', max_length=50)
    email = forms.EmailField(label='Your email', max_length=50)
    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

class BidForm(forms.Form):
    price = forms.CharField(label='Your bid', max_length=100)
    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass