from django.db import models

class Contact(models.Model):
	NJ = 'NJ'
	NY = 'NY'
	PA = 'PA'
	CT = 'CT'
	STATE_CHOICES = (
		(NJ, 'New Jersey'),
		(NY, 'New York'),
		(PA, 'Pennsylvania'),
		(CT, 'Connecticut'),
	)
	MR = 'Mr.'
	MS = 'Ms.'
	MRS = 'Mrs.'
	DR = 'Dr.'
	TITLE_CHOICES = (
		(MR,MR),
		(MS,MS),
		(MRS,MRS),
		(DR,DR),
	)

	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	street = models.CharField(max_length=50)
	city = models.CharField(max_length=100)
	state = models.CharField(
		max_length=20,
		choices = STATE_CHOICES,
		default = NJ,
	)
	zip = models.CharField(max_length=5)
	phone = models.CharField(max_length=12)
	email = models.CharField(max_length=50)
	title = models.CharField(
		max_length=5,
		choices = TITLE_CHOICES,
		default = MR,
	)
	use_mail = models.BooleanField()
	use_phone = models.BooleanField()
	use_email = models.BooleanField()
