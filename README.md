# Usted si sabe, Dr. Snow

No estamos hablando de ese John Snow, sino un pionero de los SIG, la Ciencia de Datos y Visualización de Datos.

El Dr. John Snow (1813-1858) fue un famoso médico británico y es ampliamente reconocido como una figura legendaria en la historia de la salud pública y uno de los principales pioneros en el desarrollo de la anestesia. Algunos incluso dicen que es uno de los médicos más grandes de todos los tiempos.

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
    
  Para que puedan utilizar los archivos CSV deben de llamarlos de esta forma:
  
       #Leer los datos
        url = 'https://raw.githubusercontent.com/tu_usuario/johnsnow/main/datasets/deaths.csv'
        deaths = pd.read_csv(url,encoding = 'utf-8')
     
