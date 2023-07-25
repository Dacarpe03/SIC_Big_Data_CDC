# SIC_Big_Data_CDC
https://www.whed.net/home.php

https://www.universidades.gob.es/estadistica-de-estudiantes/

https://www.ine.es/jaxi/Datos.htm?tpx=4889

http://siiu.universidades.gob.es/QEDU/

https://www.topuniversities.com/university-rankings/university-subject-rankings/2020/accounting-finance

https://www.adscientificindex.com/university/Universidad+Polit%C3%A9cnica+de+Madrid/

https://estadisticas.universidades.gob.es/dynPx/inebase/index.htm?type=pcaxis&path=/Universitaria/Indicadores/2022/1_Grado&file=pcaxis&l=s0

arte_diseno_arquitectura: arquitectura, diseño, bellas artes

agricultura_forestal

empresariales_administracion: empresa, empresariales, relaciones

economicas: economicas

educacion: educación

ingenieria_tecnologia: Ingenieria, politécnica, informática,

historia_filosofia_teologia:filosofía, historia

leyes_abogacia: derecho, jurídicas

ciencias_salud: psicología, salud, medicina , farmacia, alimentación, deporte, ontodología

ciencias_naturales: Física, matematicas

ciencias_sociales: comunicación, humanidades, sociologia , humana

otros


--------------------------------------------------------------------------------------------
DONUT:
import matplotlib.pyplot as plt

# Datos de ejemplo para el gráfico de donut
categorias = ['Categoría 1', 'Categoría 2', 'Categoría 3', 'Categoría 4']
valores = [30, 25, 15, 30]

# Colores pasteles personalizados (puedes cambiarlos por los que prefieras)
colores_pasteles = ['#F2B5D4', '#AED4E6', '#F1CB94', '#D2B4DE']

# Crear un gráfico de donut con colores pasteles
fig, ax = plt.subplots()
pie = ax.pie(valores, labels=categorias, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.3), colors=colores_pasteles)

# Agregar un círculo blanco en el centro para crear el efecto de donut
centro_circulo = plt.Circle((0, 0), 0.70, color='white')
ax.add_artist(centro_circulo)

# Ajustar la relación de aspecto para que el gráfico se vea como un círculo
ax.axis('equal')

# Mostrar el gráfico de donut
plt.title('Gráfico de Donut con Colores Pasteles')
plt.show()
------------------------------------------------------------------------------------------------------
