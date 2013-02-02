def contact():
	u_cont = User(a0 or me)
	cont = SQLFORM(db.contacts)
	if cont.process().accepted:
		response.flash = "Obrigado!"
	else:
		response.flash = "por favor, preencha os campos"
	input_text = cont.elements(_type="text")[0]
	input_text["_required"] = "required"
	return dict(cont=cont)