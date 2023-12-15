# Análisis de Datos del Sistema Compartido de Alquiler de Bicicletas - CAPITAL BIKESHARE Washington D.C. (2011)

## Objetivo
Sumérgete en nuestro repositorio de análisis de datos para desentrañar los secretos detrás del sistema de alquiler de bicicletas en Washington D.C., enfocándonos en las estaciones del año. Buscamos revelar patrones de uso, preferencias estacionales y proporcionar información valiosa para mejorar la experiencia del usuario y generar un trabajo más óptimo.🚴‍♂️📊

## Estructura del Proyecto
- **notebooks** : Explora los Jupyter Notebooks de exploración y limpieza.
- **data** : Descubre nuestras bases de datos en diferentes etapas:
1. Raw : Datos crudos tal como llegaron.
2. Process : Datos procesados para el período 2011 y 2012.
3. Final : Datos limpios y listos para comenzar nuestro descriptivo.
- **img** : Contiene las imágenes necesarias para nuestros repositorios, incluyendo el logo de CAPITAL BIKESHARE.
- **utils** : Un archivo de Python con funciones que alimentan nuestro análisis, especialmente diseñadas para explorar los datos univariante y bivariante.
- *EDA* : El Jupyter Notebook final con todos los descubrimientos fascinantes.

#### **Requisitos**
- Python 3.09 o superior.
- Jupyter Notebook para una experiencia interactiva.
- Bibliotecas de Python, entre las que destacan: pandas, matplotlib, seaborn, plotly, scipy.stats y numpy.

#### **Instrucciones de Uso** 🚀

- Clona este repositorio:
  
bash - Copy code
` git clone https://github.com/tu-usuario/CAPITAL_BIKESHARE_Analysis.git `

- Instala las herramientas mágicas:

bash - Copy code
`pip install -r requirements.txt`

## Contenido de la base de datos: 

| Número | Campo        | Descripción                                                                                           |
|--------|--------------|-------------------------------------------------------------------------------------------------------|
| 1      | **instant**   | Índice del registro. Este campo simplemente contiene un número de índice que identifica cada registro en el conjunto de datos.                                   |
| 2      | **dteday**    | Fecha. Este campo almacena la fecha en la que se registró la información.                                |
| 3      | **season**    | Estación (1: invierno, 2: primavera, 3: verano, 4: otoño). Indica la estación del año en la que se registraron los datos, con valores numéricos que corresponden a las estaciones.          |
| 4      | **yr**        | Año (0: 2011, 1: 2012). Representa el año en el que se registraron los datos, donde "0" se refiere a 2011 y "1" a 2012.                                                |
| 5      | **mnth**      | Mes (1 a 12). Indica el mes en el que se registraron los datos, con valores numéricos del 1 al 12 correspondientes a los meses.                                      |
| 6      | **hr**        | Hora (0 a 23). Muestra la hora del día en la que se registraron los datos.                  |
| 7      | **holiday**   | Indica si el día en cuestión es un día festivo ("1" si lo es y "0" si no lo es). La información se extrae de un calendario de festivos.       |
| 8      | **weekday**   | Día de la semana (0 a 6). Representa el día de la semana en el que se registraron los datos. (0: Lunes, 1: Martes, 2: Miércoles, 3: Jueves, 4: Viernes, 5: Sábado, 6: Domingo)                  |
| 9      | **workingday**| Indica si el día es laborable (día hábil) con un valor de "1" si no es un fin de semana ni un día festivo, y "0" en caso contrario. |
| 10     | **weathersit**| Situación meteorológica en el momento de la observación, con valores numéricos que representan diferentes condiciones climáticas.                                        |
| 11     | **temp**      | Temperatura normalizada en Celsius. La temperatura se encuentra normalizada y se expresa en grados Celsius. Los valores se han ajustado y se dividen entre 41, donde 41 es la temperatura máxima posible.                            |
| 12     | **atemp**     | Sensación térmica normalizada en Celsius. Al igual que la temperatura, la sensación térmica se encuentra normalizada y se expresa en grados Celsius. Los valores se han ajustado y se dividen entre 50, donde 50 es la sensación térmica máxima posible.        |
| 13     | **hum**       | Humedad normalizada. La humedad se encuentra normalizada y los valores se dividen entre 100, donde 100 representa la humedad máxima posible.                                 |
| 14     | **windspeed** | Velocidad del viento normalizada. La velocidad del viento se encuentra normalizada y los valores se dividen entre 67, donde 67 es la velocidad máxima posible del viento.            |
| 15     | **casual**    | Conteo de usuarios casuales. Muestra la cantidad de usuarios que alquilaron bicicletas de forma casual.                                                               |
| 16     | **registered**| Conteo de usuarios registrados. Indica la cantidad de usuarios que están registrados en el sistema y alquilaron bicicletas.                                             |
| 17     | **cnt**       | Conteo total de bicicletas alquiladas, incluyendo usuarios casuales y registrados. Representa el total de bicicletas alquiladas en un período determinado, incluyendo tanto a usuarios casuales como a usuarios registrados. |

### ------------------------------------ ¡A pedalear juntos hacia el conocimiento! 🚴‍♀️🌐 -------------------------------


