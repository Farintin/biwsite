from django.db import models



class Member(models.Model):
	fname = models.CharField(max_length = 20,)
	lname = models.CharField(max_length = 20,)
	email = models.EmailField(max_length = 200, null = True)
	phoneNo = models.CharField(max_length = 20, blank = True, null = True)
	addr = models.CharField(max_length = 1000, blank = True, null = True)


class Subscribers(models.Model):
	email = models.EmailField(max_length = 200, null = True)
