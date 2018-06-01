from flask import Flask, render_template, request
from metodos import Newton, Punto, Euler, Taylor
import forms

app= Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/Newton.html', methods = ['GET', 'POST'])
def newrap(t = "", m = "", df = ""):
	comment_form = forms.CommentForm1(request.form)
	if request.method =='POST':
		t, m, df = Newton(comment_form.ecuacion.data,comment_form.inicio.data,comment_form.grado.data).resultado()
	return render_template('Newton.html', form=comment_form, decuacion=str(df), tabla = t, mensajes = m)

@app.route('/Puntofijo.html', methods = ['GET', 'POST'])
def puntfij(t = "", m = ""):
	comment_form = forms.CommentForm2(request.form)
	if request.method =='POST':
		t, m = Punto(comment_form.ecuacion.data,comment_form.inicio.data,comment_form.grado.data).resultado()
	return render_template('Puntofijo.html', form=comment_form, tabla = t, mensajes = m)

@app.route('/euler.html', methods = ['GET', 'POST'])
def eule(t = "", m = ""):
	comment_form = forms.CommentForm3(request.form)
	if request.method =='POST':
		t, m = Euler(comment_form.ecuacion.data,comment_form.inicio.data,comment_form.a.data,comment_form.b.data,comment_form.intervalos.data).resultado()
	return render_template('euler.html', form=comment_form, tabla = t, mensajes = m)

@app.route('/taylor.html', methods = ['GET', 'POST'])
def taylo(t = "", m = ""):
	comment_form = forms.CommentForm4(request.form)
	if request.method =='POST':
		t, m = Taylor(comment_form.ecuacion.data,comment_form.inicio.data,comment_form.a.data,comment_form.b.data,comment_form.intervalos.data).resultado()
	return render_template('taylor.html', form=comment_form, tabla = t, mensajes = m)

if __name__== '__main__':
    app.run(debug = True)
