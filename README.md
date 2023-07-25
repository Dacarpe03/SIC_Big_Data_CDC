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



# Datos inventados de clasificaciones de universidades (rango 1-100, siendo 1 la mejor y 100 la peor)
universidades = ['Universidad A', 'Universidad B', 'Universidad C', 'Universidad D', 'Universidad E']
rankings = [10, 30, 50, 80, 90]
posiciones_y = [1, 2, 3, 4, 5]

# Tamaño de los círculos proporcional a la posición en el eje y
tamanio_circulos = [150 + pos * 100 for pos in posiciones_y]

# Configuración de la gráfica
plt.figure(figsize=(8, 6))

# Dibujar los círculos en las coordenadas indicadas
for universidad, ranking, y, size in zip(universidades, rankings, posiciones_y, tamanio_circulos):
    plt.scatter(ranking, y, s=size, color='skyblue', edgecolor='black')
    plt.text(ranking + 2, y, universidad, ha='left', va='center')

# Configuración de ejes y etiquetas
plt.xlabel('Ranking de Universidades')
plt.ylabel('Posición en el eje Y')
plt.title('Clasificación de Universidades', fontsize=16)
plt.yticks(posiciones_y, universidades)

# Mostrar gráfica
plt.grid(True)
plt.tight_layout()
plt.show()



# Ajustar la relación de aspecto para que el gráfico se vea como un círculo
ax.axis('equal')

# Mostrar el gráfico de donut
plt.title('Gráfico de Donut con Colores Pasteles')
plt.show()
------------------------------------------------------------------------------------------------------
