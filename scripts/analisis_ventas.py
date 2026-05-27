
import pandas as pd
import matplotlib.pyplot as plt

# Leer dataset
df = pd.read_csv("datos/ventas.csv")

# Calcular ventas totales
ventas_totales = df["venta_total"].sum()

# Producto más vendido
producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()

# Ventas por producto
ventas_por_producto = df.groupby("producto")["venta_total"].sum()

# Mostrar resultados
print("Ventas totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido)

# Generar gráfico
ventas_por_producto.plot(
    kind="bar",
    color="red"
)

plt.title("Ventas por producto")
plt.xlabel("Producto")
plt.ylabel("Ventas")

plt.xticks(rotation=0)

# Guardar gráfico
plt.savefig("resultados/grafico_ventas.png")

print("Gráfico guardado correctamente")
