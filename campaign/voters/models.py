from django.db import models

# Create your models here.
class Person(models.Model):
	indication = models.ForeignKey('Person',verbose_name='Indicação', blank=True, null=True, 
		on_delete=models.SET_NULL)
	
	#identificação
	name = models.CharField('nome',max_length=100)
	dataNascimento = models.DateField("Data de Nascimento", auto_now=False, auto_now_add=False)


	qnt_veiculo = models.IntegerField("Quantidade de Veículos", default=0)
	qnt_combustivel = models.IntegerField("Quantidade de Combustível", default=0)

	#contato
	cellphone = models.CharField('celular', max_length=15, blank=True)
	whatsapp = models.CharField('whatsapp', max_length=15, blank=True)
	phone = models.CharField('telefone Secundario', max_length=15, blank=True)
	email = models.EmailField('email', max_length=50, blank=True)
	facebook = models.CharField('Usuário do Facebook', max_length=200, blank=True)

	#endereco
	street = models.CharField('Rua/Nº de Residência', max_length=50)
	district = models.CharField('Bairro de Residência', max_length=50)
	city = models.CharField('Cidade de Residência', max_length=50, default='São Gonçalo do Amarante')
	state = models.CharField('UF de Residência', max_length=2, default='RN')

	#endereco votação
	localNameVoting = models.CharField('Nome do Local de Votação', max_length=50)
	districtVoting = models.CharField('Bairro do Local de Votação', max_length=50)

	zona = models.CharField('Zona de Votação', max_length=100, default="51ª ZONA ELEITORAL")
	sessao = models.CharField('Sessão de Votação', max_length=5)

	def get_all_children(self, include_self=True):
		r = []
		if include_self:
			r.append(self.name)
		for c in Person.objects.filter(indication=self):
			r.append(c.get_all_children(include_self=False))
		
		return r

	def __str__(self):
		return self.name

	def qntIndications(self):
		return self.person_set.count()

	def get_fields(self):
		return [(field.verbose_name.title, field.value_to_string(self)) for field in Person._meta.fields]