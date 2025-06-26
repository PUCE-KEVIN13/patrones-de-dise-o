# Patrón Singleton: asegura que solo haya una instancia de la clase
class Singleton:
    _instancia = None  # Atributo de clase para guardar la única instancia

    def __new__(cls):
        if cls._instancia is None:  # Si no existe instancia, se crea una
            cls._instancia = super(Singleton, cls).__new__(cls)
        return cls._instancia  # Siempre devuelve la misma instancia

# Uso
"""
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True: ambas variables apuntan al mismo objeto"""
# Interfaz base
class Animal:
    def hablar(self):
        pass

# Clases concretas
class Perro(Animal):
    def hablar(self):
        return "Guau"

class Gato(Animal):
    def hablar(self):
        return "Miau"

# Fábrica que decide qué objeto crear según el tipo
class FabricaAnimales:
    def crear_animal(self, tipo):
        if tipo == "perro":
            return Perro()
        elif tipo == "gato":
            return Gato()

# Uso
"""fabrica = FabricaAnimales()
animal = fabrica.crear_animal("gato")
print(animal.hablar())  # Miau"""

# Productos concretos
class BotonWindows:
    def dibujar(self):
        return "Botón Windows"

class BotonLinux:
    def dibujar(self):
        return "Botón Linux"

# Fábricas concretas
class FabricaWindows:
    def crear_boton(self):
        return BotonWindows()

class FabricaLinux:
    def crear_boton(self):
        return BotonLinux()

# Uso
"""fabrica = FabricaWindows()
boton = fabrica.crear_boton()
print(boton.dibujar())  # Botón Windows"""
# Producto final
class Pizza:
    def __init__(self):
        self.ingredientes = []

    def mostrar(self):
        return f"Pizza con {', '.join(self.ingredientes)}"

# Builder
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def agregar_queso(self):
        self.pizza.ingredientes.append("queso")
        return self

    def agregar_tomate(self):
        self.pizza.ingredientes.append("tomate")
        return self

    def build(self):
        return self.pizza

# Uso
"""builder = PizzaBuilder()
pizza = builder.agregar_queso().agregar_tomate().build()
print(pizza.mostrar())  # Pizza con queso, tomate"""

import copy

# Clase base
class Documento:
    def __init__(self, texto):
        self.texto = texto

    def clonar(self):
        return copy.deepcopy(self)  # Devuelve una copia del objeto

# Uso
"""doc1 = Documento("Contrato original")
doc2 = doc1.clonar()
print(doc2.texto)  # Contrato original"""

# Sujeto observado
class Subject:
    def __init__(self):
        self.observers = []  # Lista de observadores

    def attach(self, obs):
        self.observers.append(obs)  # Se agrega observador

    def notify(self, msg):
        for obs in self.observers:
            obs.update(msg)  # Se notifica a todos los observadores

# Observador
class Observer:
    def update(self, msg):
        print(f"Recibido: {msg}")

# Uso
"""s = Subject()
o1 = Observer()
s.attach(o1)
s.notify("¡Hola mundo!")  # Recibido: ¡Hola mundo!"""
# Estrategias
class EstrategiaSuma:
    def operar(self, a, b):
        return a + b

class EstrategiaResta:
    def operar(self, a, b):
        return a - b

# Contexto
class Calculadora:
    def __init__(self, estrategia):
        self.estrategia = estrategia  # Recibe la estrategia a usar

    def calcular(self, a, b):
        return self.estrategia.operar(a, b)

# Uso
"""calc = Calculadora(EstrategiaSuma())
print(calc.calcular(5, 3))  # 8"""

# Comando concreto
class EncenderLuz:
    def ejecutar(self):
        print("Luz encendida")

# Invocador
class Boton:
    def __init__(self, comando):
        self.comando = comando

    def presionar(self):
        self.comando.ejecutar()

# Uso
"""comando = EncenderLuz()
boton = Boton(comando)
boton.presionar()  # Luz encendida"""

# Estados
class Estado:
    def manejar(self):
        pass

class EstadoEncendido(Estado):
    def manejar(self):
        print("El sistema está encendido")

class EstadoApagado(Estado):
    def manejar(self):
        print("El sistema está apagado")

# Contexto
class Sistema:
    def __init__(self, estado):
        self.estado = estado

    def cambiar_estado(self, estado):
        self.estado = estado  # Se cambia el estado

    def ejecutar(self):
        self.estado.manejar()  # Ejecuta comportamiento según el estado

# Uso
"""sistema = Sistema(EstadoApagado())
sistema.ejecutar()
sistema.cambiar_estado(EstadoEncendido())
sistema.ejecutar()"""

# Mediador
class ChatRoom:
    def enviar_mensaje(self, remitente, mensaje):
        print(f"{remitente}: {mensaje}")

# Participante
class Usuario:
    def __init__(self, nombre, sala):
        self.nombre = nombre
        self.sala = sala

    def enviar(self, mensaje):
        self.sala.enviar_mensaje(self.nombre, mensaje)

# Uso
"""sala = ChatRoom()
juan = Usuario("Juan", sala)
juan.enviar("Hola a todos")"""

# Modelo
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Vista
class VistaProducto:
    def mostrar(self, producto):
        print(f"Producto: {producto.nombre} - Precio: ${producto.precio}")

# Controlador
class ControladorProducto:
    def __init__(self, producto, vista):
        self.producto = producto
        self.vista = vista

    def actualizar_precio(self, nuevo_precio):
        self.producto.precio = nuevo_precio  # Actualiza el modelo
        self.vista.mostrar(self.producto)    # Actualiza la vista

# Uso
"""producto = Producto("Laptop", 1200)
vista = VistaProducto()
controlador = ControladorProducto(producto, vista)
controlador.vista.mostrar(producto)
controlador.actualizar_precio(1000)"""