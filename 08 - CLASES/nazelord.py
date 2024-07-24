"""
Ejercicio
"""

class Programmer:
    surname: str = None
    def __init__(self, name: str, age: int, language: list) -> None:
        self.name = name
        self.age = age
        self.language = language
    def print(self):
        print(f"Nombre: {self.name} | Apellido: {self.surname} | Edad: {self.age} | Lenguajes de programación: {self.language}")
        

my_programmer = Programmer("Brais", 36,["Python", "Kotlin", "Swift"])

my_programmer.print()

my_programmer.surname = "Moure"

my_programmer.print()

my_programmer.age = 37

my_programmer.print()


"""
Extra
"""
# Stack
class Stack:
    def __init__(self) -> None:
        self.stack = []
    
    def push (self, item):
        self.stack.append(item)
    def pop(self):
        if self.count() == 0:
            return None
        return self.stack.pop()
    def count(self):
        return len(self.stack)
    def print(self):
        for item in reversed(self.stack): 
            print(item)

my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")

my_stack.print()

print(my_stack.count())

my_stack.pop()
my_stack.pop()
print(my_stack.count())

# Queue

class Queue:
    def __init__(self) -> None:
        self.queue = []
    
    def enqueue (self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.count() == 0:
            return None
        return self.queue.pop(0)

    def count(self):
        return(len(self.queue))

    def print(self):
        for item in self.queue: 
            print(item)

my_queue = Queue()

my_queue.enqueue("a")
my_queue.enqueue("b")
my_queue.enqueue("c")

my_queue.print()

print(my_queue.count())

my_queue.dequeue()

print(my_queue.count())
my_queue.print()

