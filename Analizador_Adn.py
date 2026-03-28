
Nombre = "Mateo"
Apellido = "Tejerina"
Edad = 21
Carrera = "Biología Molecular"
Universidad = "Uba"

print ("Hola, mi nombre es " + Nombre + " " + Apellido + " y tengo " + str(Edad) + " años. ")
print (" estoy estudiando " + Carrera + " en la " + Universidad) 

nombre_usuario = input ("¿Cuál es tu nombre? ")
edad_usuario = input ("¿Cuál es tu edad? ")
carrera_usuario = input ("¿Qué carrera estudias? ")
universidad_usuario = input ("¿En qué universidad estudias? ")

print ("Hola " + nombre_usuario + ", que bueno que estudies " + carrera_usuario + " en " + universidad_usuario + " y tengas " + edad_usuario + " años. ")
print ("Te parece si hacemos un poco de trabajo Genetico,"+ nombre_usuario + "?" )

codigo_genetico = input ("enviame tu codigo genetico para hacer el trabajo: ")

print ("Gracias por compartir tu codigo genetico, " + nombre_usuario + ". Ahora podemos empezar a trabajar con él.")
print ("Vamos a contar cuantas veces aparece la letra 'A' en tu codigo genetico.")
contador_A = codigo_genetico.count("A")
print ("La letra 'A' aparece " + str(contador_A) + " veces en tu codigo genetico.")
contador_T = codigo_genetico.count("T")
print ("La letra 'T' aparece " + str(contador_T) + " veces en tu codigo genetico.")
contador_G = codigo_genetico.count("G")
print ("La letra 'G' aparece " + str(contador_G) + " veces en tu codigo genetico.")
contador_C = codigo_genetico.count("C")
print ("La letra 'C' aparece " + str(contador_C) + " veces en tu codigo genetico.")
