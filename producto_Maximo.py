A = [-9, 3, 5, -2, 9, -7, 4, 8, 6]

max_producto = float('-inf')
num1 = num2 = None

for i in range(len(A)):
    for j in range(i + 1, len(A)):
        producto = A[i] * A[j]
        if producto > max_producto:
            max_producto = producto
            num1, num2 = A[i], A[j]

print("producto maximo")
print(f"Números: {num1} y {num2}")
print(f"Producto máximo: {max_producto}")