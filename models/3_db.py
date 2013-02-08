
Reciclagem = db.define_table("lixo",
	Field("papel"),
	Field("metal"),
	Field("plastico"),
	Field("vidro"))

UserAddress = db.define_table("user_address",
	Field("cpf", requires=IS_NOT_EMPTY()),
	Field("CEP"),
	Field("Pais"),
	Field("region"),
	Field("Estado"),
	Field("Cidade"),
	Field("address_type"),
	Field("address"),
	Field("home_number"),
	Field("tel"),
	Field("extra"),
	format="%(region)s")

Pictures = db.define_table("pictures",
	Field("pic", "reference auth_user"),
	Field("thumb", "upload"),
	Field("foto", "upload"))

Contacts = db.define_table("contacts",
	Field("name", requires=IS_NOT_EMPTY()),
	Field("email", requires=IS_NOT_EMPTY()),
	Field("posting", "text", required=IS_NOT_EMPTY()),
	format='%(name)s')

#social db
Wall = db.define_table("post",
	Field("body","text", requires=IS_NOT_EMPTY(),
		label='what happening?'),
	Field("posted_on","datetime", readable=False, writable=False),
	Field("posted_by", "reference auth_user", readable=False,
		writable=False),
	format='%(posted_by)s')

Link = db.define_table("link",
	Field("fonte", "reference auth_user"),
	Field("target", "reference auth_user"),
	Field("accepted", "boolean", default=False))

# and define some global variables that will make code more compact
User, Link, Post = db.auth_user, db.link, db.post
me, a0, a1 = auth.user_id, request.args(0), request.args(1)
myfriends = db(Link.fonte==me)(Link.accepted==True)
alphabetical = User.first_name | User.last_name
def name_of(user):
	return '%(first_name)s %(last_name)s' % user

class NOT_STARTS_WITH(object):
	def __init__(self, error_message="nao permitido iniciar com %s", letter="a"):
		self.error_message = error_message
		self.letter = letter

	def __call__(self, value):
		# (value, None) # passou
		# (value, error_message) # não passou
		if value.startswith(self.letter):
			return (value, self.error_message % self.letter)
		else:
			return (value, None)


# Userr.name.requires = [IS_NOT_EMPTY(error_message="voce deve preencher"),
#                           IS_NOT_IN_DB(db, 'Userr.name')]
# # Contacts.description.represent = lambda value, row: XML(value)
# Userr.name.label = "email"
# Userr.name.comment = "Your name"

#auth user
db.auth_user.avatar.label = "Sua foto"
db.auth_user.CPF.label = "Seu CPF"

# dbset = db(Userr.user_id == auth.user_id)
# Userr.name.requires = IS_IN_DB(dbset, "user_address.id", "%(country)s - %(city)s")