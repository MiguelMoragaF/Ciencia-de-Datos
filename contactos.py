# SISTEMA DE GESTIÓN DE CONTACTOS

class Contacto:
    def __init__(self, nombre, telefono, correo, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    def __str__(self):
        return f"{self.nombre} | {self.telefono} | {self.correo} | {self.direccion}"


class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)
        print("✅ Contacto agregado")

    def mostrar_contactos(self):
        if not self.contactos:
            print("No hay contactos")
        for c in self.contactos:
            print(c)

    def buscar_contacto(self, dato):
        for c in self.contactos:
            if dato in c.nombre or dato in c.telefono:
                print("🔍 Encontrado:", c)

    def eliminar_contacto(self, nombre):
        self.contactos = [c for c in self.contactos if c.nombre != nombre]
        print("❌ Contacto eliminado")

    def editar_contacto(self, nombre):
        for c in self.contactos:
            if c.nombre == nombre:
                c.telefono = input("Nuevo teléfono: ")
                c.correo = input("Nuevo correo: ")
                c.direccion = input("Nueva dirección: ")
                print("✏️ Contacto actualizado")


def menu():
    agenda = Agenda()

    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar")
        print("2. Mostrar")
        print("3. Buscar")
        print("4. Editar")
        print("5. Eliminar")
        print("6. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")
            direccion = input("Dirección: ")
            agenda.agregar_contacto(Contacto(nombre, telefono, correo, direccion))

        elif opcion == "2":
            agenda.mostrar_contactos()

        elif opcion == "3":
            dato = input("Buscar: ")
            agenda.buscar_contacto(dato)

        elif opcion == "4":
            nombre = input("Nombre a editar: ")
            agenda.editar_contacto(nombre)

        elif opcion == "5":
            nombre = input("Nombre a eliminar: ")
            agenda.eliminar_contacto(nombre)

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()
