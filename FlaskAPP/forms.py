from wtforms import Form, TextField, FloatField, IntegerField

class CommentForm1(Form):
	ecuacion = TextField('Digite la ecuacion:')
	inicio = FloatField('Digite el valor inicial:')
	grado = IntegerField('Digite el grado de tolerancia:')
	
class CommentForm2(Form):
	ecuacion = TextField('Digite la ecuacion (igualada a cero):')
	inicio = FloatField('Digite el valor inicial:')
	grado = IntegerField('Digite el grado de tolerancia:')

class CommentForm3(Form):
	ecuacion = TextField('Digite la ecuacion f(y,t):')
	inicio = FloatField('Digite el valor inicial:')
	a = FloatField('Digite el valor de a:')
	b = FloatField('Digite el valor de b:')
	intervalos = IntegerField('Digite el numero de intervalos:')
	
class CommentForm4(Form):
	ecuacion = TextField('Digite la ecuacion f(y,t):')
	inicio = FloatField('Digite el valor inicial:')
	a = FloatField('Digite el valor de a:')
	b = FloatField('Digite el valor de b:')
	intervalos = IntegerField('Digite el numero de intervalos:')
	