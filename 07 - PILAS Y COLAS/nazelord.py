"""
Ejercicio
"""

#Pila / Stack (LIFO)

stack = []

# Push
stack.append("1")
stack.append("2")
stack.append("3")
print(stack)

# Pop
stack_item = stack[len(stack)-1]
del stack[len(stack)-1]

print(stack_item)

print(stack.pop())

print(stack)

# Cola / Queue (FIFO)

queue = []

# Enqueue
queue.append(1)
queue.append(2)
queue.append(3)

# Dequeue

queue_item = queue[0]
del queue[0]
print(queue_item)

print(queue.pop(0))

print(queue)


"""
Extra
"""

def browser():
    pages = ["Google.com","Facebook.com","Twitter.com","Instagram.com"]
    pages_history = []
    while True:
        print("\n")
        print("\nBrowser ")
        print(f"You are in this page: {pages[-1]}")
        print("1. Go Back")
        print("2. Go Forward")
        print("3. Visit Page")
        print("4. Quit")
        choice = input("Choose an option: ")
        match choice:
            case "1":
                if len(pages) > 1:
                    pages_history.append(pages[-1])
                    pages.pop()
                    print(f"Visiting: {pages[-1]}")
                else:
                    print("No more pages to go back.")
            case "2":
                if len(pages_history) > 0:
                    pages.append(pages_history.pop())
                    print(f"Visiting: {pages[-1]}")
                else:
                    print("No more pages to go forward.")
            case "3":
                page = input("Enter the page to visit: ")
                pages.append(page)
                #pages_history.append(page)
                print(f"Visiting: {page}")
            case "4":
                print("Exiting...")
                break     



# Impresora

def printer():
    pages = []
    while True:
        print("\nPrinter")
        print("Welcome to Impresora")
        print("1. Print Page")
        print("2. Add Page")
        print("3. Quit")
        choice = input("Choose an option: ")
        match choice:
            case "1":
                if len(pages) > 0:
                    page = pages.pop(0)
                    print(f"Printing: {page}")
                else:
                    print("No more pages to print.")
            case "2":
                page = input("Enter the page to add: ")
                pages.append(page)
                print(f"Page added: {page}")
            case "3":
                print("Exiting...")
                break

def main():
    while True:
        print("\nMenu")
        print("1. Browser")
        print("2. Printer")
        print("3. Exit")
        choice = input("Choose an option: ")
        match choice:
            case "1":
                browser()
            case "2":
                printer()
            case "3":
                print("Exiting...")
                break

main()