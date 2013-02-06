from gluon.storage import Storage

config = Storage(db=Storage(),
	auth=Storage(settings=Storage(extra_fields=Storage()),
		messages=Storage()), 
	mail=Storage())

config.db.uri = "sqlite://recycle.sqlite"
config.db.check_reserved = ['all']


config.auth.settings.formstyle = 'divs'
config.auth.settings.registration_requires_verification = False
config.auth.settings.registration_requires_approval = False
config.auth.settings.login_after_registration = False
config.auth.settings.login_next = URL('home')
config.auth.settings.register_next = URL('home')
config.auth.messages.logged_in = 'Logged in'
config.auth.messages.registration_successful = 'Registration successful'


config.auth.settings.extra_fields.auth_user = [
	Field("CPF"),
	Field("pais"),
	Field("region"),
	Field("estado"),
	Field("cidade"),
	Field("address_type"),
	Field("address"),
	Field("home_number"),
	Field("tel", requires=IS_MATCH('[\d\-\(\)] +')),
	Field("avatar", "upload"),
	Field("thumbnail", "upload")]

config.mail.server = 'smtp.gmail.com:587'
config.mail.sender = ''
config.mail.login = ''


from gluon import current
current.config = config

response.title = "EuReciclo"
response.subtitle = T("EuReciclo")

response.meta.author = "Diego Miranda"
response.meta.description = "App for recycling trash"
response.meta.keywords = "web2py, python framework"
response.meta.generator = "web2py web framework"
response.meta.copyright = "DSMTech Copyright 2012"
response.generic_patterns = ['*']