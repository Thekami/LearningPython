# -*- coding: utf-8 -*-
import datetime

hoy = datetime.date.today()


print hoy

print """
el dia es: """,hoy.day,"el mes es: ",hoy.month,"el años es: ",hoy.year

print """
el numero del dia es: """,hoy.weekday() #el dia 0 es el lunes, el 1 es el martes y asi...}

semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']

numero = hoy.weekday()

print """
el dia es: """,semana[numero]


hoy = datetime.datetime.today()

print """
Aqui se imprime fecha y hora: """hoy