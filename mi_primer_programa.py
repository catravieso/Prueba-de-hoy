# Quiero imprimir por pantalla la frase "Hola a todos, me encanta el programa FIME First"
print("Hola a todos, me encanta el programa FIME First")

# Preguntar a quién más saludar
respuesta = input("¿A quién más quieres saludar? (Separa con comas si son varios): ")

# Procesar la respuesta
if respuesta.strip():
    nombres = [n.strip() for n in respuesta.split(',') if n.strip()]
    for nombre in nombres:
        print("Hola " + nombre)
else:
    print("No hay más saludos.")