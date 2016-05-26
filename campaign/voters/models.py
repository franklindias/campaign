from django.db import models

# Create your models here.
class Person(models.Model):
	indication = models.ForeignKey('Person',verbose_name='Indicação', blank=True, null=True, 
		on_delete=models.SET_NULL)
	
	#identificação
	name = models.CharField('nome',max_length=100)
	dataNascimento = models.DateField("Data de Nascimento", auto_now=False, auto_now_add=False)

	CHOICE_VEICULO = (
		(False, 'Não'),
		(True, 'Sim')
	)

	veiculo = models.BooleanField("Vai precisar de Veículo?", default=False, choices=CHOICE_VEICULO)

	#contato
	cellphone = models.CharField('celular', max_length=15, blank=True)
	whatsapp = models.CharField('whatsapp', max_length=15, blank=True)
	phone = models.CharField('telefone secundario', max_length=15, blank=True)
	email = models.EmailField('email', max_length=50, blank=True)
	facebook = models.URLField('facebook', max_length=200, blank=True)

	#endereco
	street = models.CharField('rua de residência', max_length=50)
	district = models.CharField('Bairro de residência', max_length=50)
	city = models.CharField('cidade de residência', max_length=50, default='São Gonçalo do Amarante')
	state = models.CharField('estado de residência', max_length=2, default='RN')

	#endereco votação
	localNameVoting = models.CharField('Nome do Local de Votação', max_length=50)
	districtVoting = models.CharField('Bairro do Local de Votação', max_length=50)

	zona = models.CharField('Zona de Votação', max_length=100, default="51ª ZONA ELEITORAL")
	sessao = models.CharField('Sessão de Votação', max_length=5)


	def __str__(self):
		return self.name

	def qntIndications(self):
		return self.person_set.count()

	def get_fields(self):
		return [(field.verbose_name.title, field.value_to_string(self)) for field in Person._meta.fields]