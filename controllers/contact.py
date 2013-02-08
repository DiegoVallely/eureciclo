from gluon.tools import Mail


def contact():
	u_cont = User(a0 or me)
	form = SQLFORM(db.contacts)
	if form.process().accepted:
		mensagem = "%s %s <br>Enviou</br> %s " % (form.vars.name, form.vars.email,
													form.vars.posting)
		
		status = mail.send(to=['dsousamiranda@gmail.com'],reply_to=form.vars.email,
                    		subject=None,
                    		message=[None,mensagem])
	if status == True:
		response.flash = "Obrigado!"
	else:
		response.flash = "por favor, preencha os campos"
	input_text = form.elements(_type="text")[0]
	input_text["_required"] = "required"

	return dict(cont=cont)