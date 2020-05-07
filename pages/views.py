import os, shutil
from os import path
from PIL import Image

from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings

sender_email = settings.EMAIL_HOST_USER

from pages.forms import Register, Subscriber, Contact
from pages.models import Member, Subscribers
from pages.email import subscribe_email, register_email





def home(request):
	return render(request, 'pages/home.html')


def services(request):
	form = Subscriber()
	context = {'form': form}
	if request.method == 'POST':
		form = Subscriber(request.POST)
		if form.is_valid():
			print('form.is_valid()')
			form.save(commit = False)
			email = form.cleaned_data.get('email')
			if email in Subscribers.objects.values_list('email', flat = True):
				context['err'] = 'Your email address has already been collected sucessfully, Thank you.'
				if email == sender_email:
					subscribe_email(sender_email, email)
					context['err'] = ''
					context['sucess'] = 'Thanks for Subscribing, please check your email for confirmation'
			else:
				subscribe_email(sender_email, email)
				form.save()
				context['sucess'] = 'Thanks for Subscribing, please check your email for confirmation'
		else:
			context = {'form': form}
	else:
		form = Subscriber()
		context = {'form': form}
		
	context['services_page'] = True
	return render(request, 'pages/services.html', context)


def photos(request, photo=""):
	full_photos_folder = 'pages/static/pages/img/photos/'
	photos_filename = [file for file in os.listdir(full_photos_folder) if file.endswith(('jpg', 'png'))]

	if not photo:
		thumbs_folder = full_photos_folder + 'thumbnails/'
		os.makedirs(thumbs_folder, exist_ok = True)
		thumbs_filename = os.listdir(thumbs_folder)

		for thumb_filename in thumbs_filename:
			if not thumb_filename in photos_filename:
				os.remove(thumbs_folder + thumb_filename)
		for photo_filename in photos_filename:
			if not photo_filename in thumbs_filename:
				photo_pathname = full_photos_folder + photo_filename
				thumb_obj = Image.open(photo_pathname)
				thumb_obj.thumbnail((400,400))
				thumb_pathname = thumbs_folder + photo_filename
				thumb_obj.save(thumb_pathname)
				thumb_obj.close()

		context = {
			'photos': photos_filename,
			'photos_page': True
			}
		return render(request, 'pages/photos.html', context)

	else:
		photo_index = photos_filename.index(photo)
		last_photo_index = len(photos_filename) - 1

		if photo_index == last_photo_index:
			next_photo = photos_filename[0]
		else:
			next_photo = photos_filename[photo_index + 1]
		if photo_index == 0:
			prev_photo = photos_filename[last_photo_index]
		else:
			prev_photo = photos_filename[photo_index - 1]

		context = {
			'photo': photo,
			'prev_photo': prev_photo,
			'next_photo': next_photo
			}
		return render(request, 'pages/photoView.html', context)


def videos(request):
	context = {
		'videos_page': True
		}
	return render(request, 'pages/videos.html', context)


def about(request):
	context = {
		'about_page': True
		}
	return render(request, 'pages/about.html', context)


def contact(request):
	form = Contact(request.POST or None)
	context = {
		'form': form,
		'contact_page': True}

	if request.method == 'POST' and form.is_valid():
		name = form.cleaned_data.get('name')
		email = form.cleaned_data.get('email')
		subject = form.cleaned_data.get('subject')

		msg_detail = 'A visitor:\n\tName: %s\n\tEmail: %s\nsent this message through BIW website contact page.\n\n\t' %(name, email)
		msg = (msg_detail + str(form.cleaned_data.get('message')))

		if email == sender_email:
			recipients = [sender_email]
			send_mail(subject, msg, sender_email, recipients, fail_silently = True)
			form = Contact()
			
		else:
			recipients = ['beyondimaginationgang@gmail.com', sender_email]
			send_mail(subject, msg, sender_email, recipients, fail_silently = True)
			form = Contact()

		context = {
			'form': form,
			'success': 'Thank you for writing to BIW'
			}
	return render(request, 'pages/contact.html', context)


def register(request):
	form = Register()
	if request.method == 'POST':
		form = Register(request.POST)
		if form.is_valid():
			form.save(commit = False)

			fullName = form.cleaned_data.get('fname') + ' ' + form.cleaned_data.get('lname')
			email = form.cleaned_data.get('email')


			if email in Member.objects.values_list('email', flat = True):
				context = {'form': form,'err': 'Your email address is registered, Thank you.'}
				if email == sender_email:
					register_email(sender_email, email, fullName)
					context['err'] = ''
					context['sucess'] = 'Thanks for Signing up with BIW, please check the mail just sent to your email'
			else:
			    register_email(sender_email, email, fullName)
			    form.save()
			    context = {
			    	'form': form,
				    'sucess': 'Thanks for Signing up with BIW, please check the mail just sent to your email'
					}
			    
		else:
			context = {
				'form': form
				}

	else:
		form = Register()
		context = {
			'form': form
			}
	context['register_page'] = True
	return render(request, 'pages/register.html', context)