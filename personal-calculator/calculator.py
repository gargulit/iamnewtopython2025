def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "חילוק באפס אסור!"

print("ברוכה הבאה למחשבון!")
print("בחרי פעולה:")
print("1. חיבור")
print("2. חיסור")
print("3. כפל")
print("4. חילוק")

choice = input("הכניסי את מספר הבחירה שלך (1/2/3/4): ")

num1 = float(input("הכניסי את המספר הראשון: "))
num2 = float(input("הכניסי את המספר השני: "))

if choice == '1':
    print("תוצאה:", add(num1, num2))
elif choice == '2':
    print("תוצאה:", subtract(num1, num2))
elif choice == '3':
    print("תוצאה:", multiply(num1, num2))
elif choice == '4':
    print("תוצאה:", divide(num1, num2))
else:
    print("בחירה לא חוקית.")
