from gluon.storage import Storage

def origin():
		return dict()

def index():
	if auth.user:
		redirect(URL('home'))
	return locals()

# @auth.requires_login()
def login():
	# lg = auth.login()
	# te = db.logn(request.args(0)) or redirect(URL('index','index'))
	# form = SQLFORM(Login, FORM('E-mail:',
	# 	INPUT(_type='text', _placeholder='', _class='input-block-level',
	# 		requires=IS_NOT_EMPTY()),'password:',
	# 	INPUT(_type='Password', _placeholder='password', _class='input-block-level',
	# 		requires=IS_NOT_EMPTY()),
	# 	INPUT(_type='Submit', _class='btn btn-large btn-primary', _value='Sing in', 
	# 		_onclick="")))
	# form = SQLFORM(db.logn, formstyle="divs", 
	# 	submit_button="sing in").process()
	# inputname = form.elements(_type="submit")
	# inputname["_class"] = "btn btn-large btn-primary"
	# if request.args in Userr == True:
	# 	response.flash="success"
	# 	redirect(URL('index','index'))
	# elif lg.errors:
	# 	response.flash="try again"
	# else:
	# 	response.flash = "please fill the form"
	return dict(lg=auth.login())


def user():
	objects = Storage()
	if request.args(0) in ['login','register']:
		objects.login = auth.login()
		response.flash = "logged in"
		objects.register = auth.register()
	else:
		objects.form = auth()
	return dict(objects=objects)


def download():
	return response.download(request, db)

def call():
	session.forget()
	return service()

def data():
	return dict(form=crud())


@auth.requires_login()
def home():
	user = User(a0 or me)
	name = name_of(user)
	Post.posted_by.default = me
	Post.posted_on.default = request.now
	crud.settings.formstyle = "divs"
	form = crud.create(Post)
	friends = [me]+[row.target for row in myfriends.select(Link.target)]
	posts = db(Post.posted_by.belongs(friends)).select(orderby=~Post.posted_on,
		limitby=(0,100))
	form_lixo = SQLFORM(Reciclagem).process()

	return locals()


@auth.requires_login()
def wall():
	user = User(a0 or me)
	if not user or not (user.id==me or \
		myfriends(Link.target==user.id).count()):
		redirect(URL('home'))
	posts = db(Post.posted_by==user.id).select(orderby=~Post.posted_on,
		limitby=(0,100))
	return locals()


@auth.requires_login()
def search():
	form = SQLFORM.factory(Field('name', requires=IS_NOT_EMPTY()))
	if form.accepts(request):
		tokens = form.vars.name.split()
		query = reduce(lambda a,b:a&b,
			[User.first_name.contains(k) | User.last_name.contains(k)\
			for k in tokens])
		people = db(query).select(orderby=alphabetical)
	else:
		people = []

	return locals()


@auth.requires_login()
def friends():
	friends = db(User.id==Link.fonte)(Link.target==me).select(orderby=alphabetical)
	requests = db(User.id==Link.target)(Link.fonte==me).select(orderby=alphabetical)
	return locals()

# this is the Ajax callback
@auth.requires_login()
def friendship():
	"""Ajax callback"""
	if request.env.request_method != 'POST': raise HTTP(400)
	if a0 == 'request' and not Link(fonte=a1, target=me):
		# insert a new friendship request
		Link.insert(fonte=me, target=a1)
	elif a0 == 'accept':
		# accept an existing friendship request
		db(Link.target==me)(Link.fonte==a1).update(accepted=True)
	if not db(Link.fonte==me)(Link.target==a1).count():
		Link.insert(fonte=me, target=a1)
	elif a0 == 'deny':
		# deny an existing friendship request
		db(Link.target==me)(Link.fonte==a1).delete()
	elif a0 == 'remove':
		# delete a previous friendship request
		db(Link.fonte==me)(Link.target==a1).delete()


def address():
	u_id = User(a0 or me) or redirect(URL('home'))
	if u_id in session:
		form = SQLFORM(UserAddress, formstyle='divs')
	if form.process().accepted:
		redirect(URL('home'))
	return dict(form=form)