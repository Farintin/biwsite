from django.template import loader
from django.core.mail import send_mail



def subscribe_email(sender, recipient):
	sub_subject = 'BIW Models Newsletter Subscribtion'

	v_msg = ('\tThanks for Subscribing to Our Newsletter. You will be notified of any current post or event from BIW Models.')
	html_v_msg = loader.render_to_string('pages/email/newsletter_subscribtion.html')

	send_mail(sub_subject, v_msg, sender, [recipient], fail_silently = True, html_message = html_v_msg)
	print('done sending to visitor')


	admin_msg = ('%s just recieved:\n\t %s\n from %s by %s' %(recipient, v_msg, 'BIW Models', sender))
	admin_report = {
		'from_report': '%s just recieved this email' %(recipient),
		'to_report': 'From %s by %s' %('BIW Models', sender)
		}
	html_admin_msg = loader.render_to_string('pages/email/newsletter_subscribtion.html', admin_report)

	send_mail(sub_subject, admin_msg, sender, [sender], fail_silently = True, html_message = html_admin_msg)
	print('done sending to admin')


def register_email(sender, recipient, fullName):
	reg_subject = 'BIW Models Membership'

	regVMsg = ('\tThanks %s for filling the form. We will try to be responsive as possible. Our team will get back to you soon for upcoming events.'%(fullName))
	memData = {
		'fullName': fullName
		}
	htmlVMsg = loader.render_to_string('pages/email/registered.html', memData)
	send_mail(reg_subject, regVMsg, sender, [recipient], fail_silently = True, html_message = htmlVMsg)

	adminMsg = ('%s just recieved:\n\t %s\n from %s by %s' %(recipient, regVMsg, 'BIW Models', sender))
	regAdminReport = {
		'from_report': '%s just recieved this email' %(recipient),
		'fullName': fullName,'to_report': 'From %s by %s' %('BIW Models', sender)
		}
	htmlAdminMsg = loader.render_to_string('pages/email/registered.html', regAdminReport)
	send_mail(reg_subject, adminMsg, sender, [sender], fail_silently = True, html_message = htmlAdminMsg)
