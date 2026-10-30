s = int(input("Ingresa el precio por unidad: "))
f = int(input("Ingresa el costo fijo: "))
v = int(input("Ingresa el costo variable por unidad: "))
x = int(input("Ingresa el número de unidades vendidas: "))

ganancia = s*x-(f+v*x)
pequilibrio = f/(s-v)
print("El punto de equilibrio es: ", pequilibrio)
print("La ganancia es: ", ganancia)
