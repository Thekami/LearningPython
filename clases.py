class PrimeraClase():
	def hola(self):
		print "hola, soy la funcion 1 de la PrimeraClase"

	def adios(self):
		print "hola, soy la funcion 2 de la PrimeraClase"


class SegundaClase(PrimeraClase):
	def hola2(self):
		print "hola, soy la funcion 1 de la SegundaClase"

	def adios2(self):
		print "hola, soy la funcion 2 de la SegundaClase"

	def herencia(self):
		PrimeraClase.hola(self)

	def herencia2(self):
		PrimeraClase.adios(self)


def main():

# se declara una variable (objeto) de tipo "PrimeraClase" y despues se llama al metodo de la clase

	objeto_tipo_primeraClase = PrimeraClase()

	print """
	primera funcion de la primera clase
	"""

	objeto_tipo_primeraClase.hola() 

	print """
	segunda funcion de la primera clase
	"""

	objeto_tipo_primeraClase.adios()


# se declara una variable (objeto) de tipo "SegundaClase" y despues se llama al metodo de la clase

	objeto_tipo_segundaClase = SegundaClase()

	print """
	primera funcion de la segunda clase
	"""

	objeto_tipo_segundaClase.hola2()

	print """
	segunda funcion de la segunda clase
	"""

	objeto_tipo_segundaClase.adios2()

	print """
	tercera
	"""

	objeto_tipo_segundaClase.herencia()

	print """
	cuarta
	"""

	objeto_tipo_segundaClase.herencia2()

if __name__ == "__main__":
	main()