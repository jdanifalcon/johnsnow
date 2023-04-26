# Usted si sabe, Dr. Snow

No estamos hablando de ese John Snow, sino un pionero de los SIG, la Ciencia de Datos y Visualización de Datos.

![alt text](https://pithysummary.com/wp-content/uploads/2022/02/theactualghostmap.jpg)

El Dr. John Snow (1813-1858) fue un famoso médico británico y es ampliamente reconocido como una figura legendaria en la historia de la salud pública y uno de los principales pioneros en el desarrollo de la anestesia. Algunos incluso dicen que es uno de los médicos más grandes de todos los tiempos.

En este cuaderno, no solo vamos a redescubrir su "historia de datos", sino también a analizar de nuevo los datos que recopiló en 1854 y recrear su famoso mapa (también conocido como "El Mapa Fantasma").
    
  Para que puedan utilizar los archivos CSV deben de llamarlos de esta forma:
  
       #Leer los datos
        url = 'https://raw.githubusercontent.com/tu_usuario/johnsnow/main/datasets/deaths.csv'
        deaths = pd.read_csv(url,encoding = 'utf-8')
     
Si quieren trabajar desde Anaconda les dejo un pequeño ejemplo:

    #Leer los datos
    deaths = pd.read_csv('datasets/deaths.csv')

¡Este taller básico de Pandas esta dirigido para todos aquellas personas que quieran reforzar sus conocimientos con la libreria Pandas y utilizarlo como ejercicio! 

Un gran agradecimiento a [Robin Wilson](https://blog.rtwilson.com/john-snows-famous-cholera-analysis-data-in-modern-gis-formats/) de la Universidad de Southampton, quien digitalizó los datos originales de John Snow y los georeferenció al sistema de coordenadas Ordnance Survey que nos permitirá analizarlos y superponerlos en mapas modernos de esa área.
