import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# df_acelero = pd.read_csv("/Users/josegiraldogomez/Documents/Prueba/acelero.txt")
df_acelero = pd.read_csv("./acelero.txt")
df_acelero["Fecha"] = pd.to_datetime(df_acelero["Tiempo"], unit="s")
df_acelero["Fecha"] = pd.to_datetime(df_acelero["Fecha"])

print(df_acelero)

ventana_media_movil = 20
df_acelero["Media_Movil_Posicion"] = (
    df_acelero["Posición"].rolling(window=ventana_media_movil).mean()
)

# Obtener el valor máximo y mínimo de la columna 'Posición' con cuatro decimales
max_posicion = df_acelero["Posición"].max().round(4)
min_posicion = df_acelero["Posición"].min().round(4)

# Graficar scatter plot de Posición
fig, ax1 = plt.subplots()

color = "tab:red"
ax1.set_xlabel("Tiempo")
ax1.set_ylabel("Posición", color=color)
ax1.scatter(df_acelero["Fecha"], df_acelero["Posición"], label="Posición", color=color)
ax1.plot(
    df_acelero["Fecha"],
    df_acelero["Media_Movil_Posicion"],
    color="red",
    label=f"Media Móvil Posición ({ventana_media_movil} puntos)",
)
ax1.axhline(
    y=max_posicion,
    color="green",
    linestyle="--",
    label=f"Máximo Posición: {max_posicion}",
)
ax1.axhline(
    y=min_posicion,
    color="blue",
    linestyle="--",
    label=f"Mínimo Posición: {min_posicion}",
)
ax1.tick_params(axis="y", labelcolor=color)

# Crear un segundo eje y para la columna 'Temperatura'
ax2 = ax1.twinx()
color = "tab:blue"
ax2.set_ylabel("Temperatura", color=color)
ax2.scatter(
    df_acelero["Fecha"], df_acelero["Temperatura"], label="Temperatura", color=color
)
ax2.tick_params(axis="y", labelcolor=color)

fig.tight_layout()
plt.title("Tiempo vs Posición y Temperatura")
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))

correlacion = df_acelero["Posición"].corr(df_acelero["Temperatura"])

print(f"Correlación entre Posición y Temperatura: {correlacion}")


df_acelero["Fecha"] = pd.to_datetime(df_acelero["Fecha"])


# Calcular la diferencia entre los valores consecutivos de 'Posición'
df_acelero["Cambio_Posicion"] = df_acelero["Posición"].diff()

# Establecer un umbral para las variaciones que quieres resaltar
umbral_variacion = 0.03  # Puedes ajustar este valor según tus necesidades

# Filtrar las variaciones que están por encima del umbral
variaciones_destacadas = df_acelero[
    df_acelero["Cambio_Posicion"].abs() > umbral_variacion
]

# Graficar scatter plot
plt.scatter(df_acelero["Fecha"], df_acelero["Posición"], label="Posición")

# Graficar la línea de media móvil
plt.plot(
    df_acelero["Fecha"],
    df_acelero["Media_Movil_Posicion"],
    color="red",
    label=f"Media Móvil Posición",
)

# Resaltar las variaciones por encima del umbral con líneas verticales y etiquetas
for fecha, posicion, variacion in zip(
    variaciones_destacadas["Fecha"],
    variaciones_destacadas["Posición"],
    variaciones_destacadas["Cambio_Posicion"],
):
    plt.vlines(fecha, ymin=0, ymax=posicion, color="orange", linestyle="--")
    plt.text(
        fecha,
        posicion,
        f'{fecha.strftime("%Y-%m-%d")}\nVariación: {variacion:.2f}',
        color="orange",
        fontsize=8,
        ha="left",
        va="bottom",
        rotation=45,
    )


def encontrar_variaciones(df, columna, umbral):
    # Calcular la diferencia entre los valores consecutivos de la columna
    df_acelero["Cambio_Posicion"] = df_acelero["Posición"].diff()

    # Filtrar las variaciones que están por encima del umbral
    variaciones_destacadas = df[df_acelero["Cambio_Posicion"].abs() > umbral]

    return variaciones_destacadas


print(variaciones_destacadas)
plt.show()
