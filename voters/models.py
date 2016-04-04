from django.db import models

# Create your models here.
class Person(models.Model):
	indication = models.ForeignKey('Person',verbose_name='Indicação', blank=True, null=True)
	
	#identificação
	name = models.CharField(max_length=100)
	cpf = models.CharField('CPF', max_length=15)

	#contato
	cellphone = models.CharField('celular', max_length=15)
	phone = models.CharField('telefone secundario', max_length=15)
	email = models.EmailField('email', max_length=50)
	facebook = models.URLField('facebook', max_length=200)

	#endereco
	street = models.CharField('rua', max_length=50)
	number = models.CharField('número', max_length=6)
	district = models.CharField('Bairro', max_length=50)
	city = models.CharField('cidade', max_length=50)
	state = models.CharField('estado', max_length=2, default='RN')

	

	def __str__(self):
		return self.name

	def qntIndications(self):
		return self.person_set.count()

	def get_fields(self):
		return [(field.name, field.value_to_string(self)) for field in Person._meta.fields]