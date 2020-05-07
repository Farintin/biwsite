from django.forms import ModelForm
from pages.models import Member, Subscribers

from django import forms


class Register(ModelForm):

	class Meta():
		model = Member
		fields = ( 'fname', 'lname', 'email', 'phoneNo', 'addr')


class Subscriber(ModelForm):
	email = forms.EmailField(required = True)

	class Meta():
		model = Subscribers
		fields = ('email',)


class Contact(forms.Form):
	name = forms.CharField(max_length = 100)
	email = forms.EmailField()
	subject = forms.CharField(max_length = 100)
	message = forms.CharField(widget = forms.Textarea)
