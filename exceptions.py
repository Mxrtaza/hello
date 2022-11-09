import sys

try: 
    x = int (input("x: "))
    y = int (input("y: "))
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)


try: 
    results = x / y 
except ZeroDivisionError:
    print("ErrorL Cannot divide by 0")
    sys.exit(1)
    
print(f"{x}/{y}= {results}")

