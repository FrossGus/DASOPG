class Persona:
    def __init__(self):
        self.nombre = ""
        self.edad = 0


print("Prueba Clase Persona")
personita = Persona()
personita.nombre = "Nestor"
personita.edad = 57

print(personita.nombre + " tiene " + str(personita.edad) + " años.")

