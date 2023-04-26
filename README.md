# Usted si sabe, Dr. Snow

No estamos hablando de ese John Snow, sino un pionero de los SIG, la Ciencia de Datos y Visualización de Datos.

El Dr. John Snow (1813-1858) fue un famoso médico británico y es ampliamente reconocido como una figura legendaria en la historia de la salud pública y uno de los principales pioneros en el desarrollo de la anestesia. Algunos incluso dicen que es uno de los médicos más grandes de todos los tiempos.

Como defensor principal tanto de la anestesia como de las prácticas higiénicas en la medicina, no solo experimentó con éter y cloroformo, sino que también diseñó una máscara y un método para administrarlo. Personalmente administró cloroformo a la Reina Victoria durante los nacimientos de su octavo y noveno hijos, en 1853 y 1857, lo que aseguró una creciente aceptación pública del uso de anestésicos durante el parto.

Pero, como mostraremos más adelante, no toda su vida fue solo un éxito. John Snow ahora también es reconocido como uno de los fundadores de la epidemiología moderna (algunos también lo consideran como el fundador de la visualización de datos, el análisis espacial, la ciencia de datos en general y muchos otros campos relacionados) por su enfoque científico y bastante moderno en la recolección de datos para identificar la fuente de un brote de cólera en Soho, Londres, en 1854, pero no siempre fue así. De hecho, durante mucho tiempo fue simplemente ignorado por la comunidad científica y actualmente se mitifica con frecuencia.

En este cuaderno, no solo vamos a redescubrir su "historia de datos", sino también a analizar de nuevo los datos que recopiló en 1854 y recrear su famoso mapa (también conocido como "El Mapa Fantasma").

Utilizaremos la librería de pandas, ojo, lo estoy escribiendo como si estuvieramos en la consola pero se escribe de otra forma:

    # Loading in the pandas module
    import pandas as pd

    # Reading in the data
    deaths = pd.read_csv('datasets/deaths.csv')

    # Print out the shape of the dataset
    print(deaths.shape)

    # Printing out the first 5 rows
    deaths.head()
     
