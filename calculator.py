
import numpy as np

def get_array(prompt):
    try:
        return np.array([float(x.strip()) for x in input(prompt).split(',')])
    except ValueError:
        print("Invalid input. Please enter numbers separated by commas.")
        exit()

arr1 = get_array("Enter first number: ")
arr2 = get_array("Enter second number: ")

if arr1.size != arr2.size:
    print("Error: Arrays must be of the same length.")
    exit()

print("\nChoose operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    result = np.add(arr1, arr2)
elif choice == '2':
    result = np.subtract(arr1, arr2)
elif choice == '3':
    result = np.multiply(arr1, arr2)
elif choice == '4':
    with np.errstate(divide='ignore', invalid='ignore'):
        result = np.divide(arr1, arr2)
        result[np.isinf(result)] = np.nan
else:
    print("Invalid choice.")
    exit()

print("Result:", result)
