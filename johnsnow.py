# -*- coding: utf-8 -*-
"""johnsnow.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ppkfmz0b2e8fp-Oz0om_6k9OBhdwXYr5

## 1. Dr. John Snow
<p><img style="float: left;margin:5px 20px 5px 1px" src="https://assets.datacamp.com/production/project_132/img/johnsnow_final1.png"></p>
<p>El Dr. John Snow (1813-1858) fue un famoso médico británico y es ampliamente reconocido como una figura legendaria en la historia de la salud pública y uno de los principales pioneros en el desarrollo de la anestesia. Algunos incluso dicen que es uno de los médicos más grandes de todos los tiempos.</p>
<p>Como defensor principal tanto de la anestesia como de las prácticas higiénicas en la medicina, no solo experimentó con éter y cloroformo, sino que también diseñó una máscara y un método para administrarlo. Personalmente administró cloroformo a la Reina Victoria durante los nacimientos de su octavo y noveno hijos, en 1853 y 1857, lo que aseguró una creciente aceptación pública del uso de anestésicos durante el parto.</p>
<p>Pero, como mostraremos más adelante, no toda su vida fue solo un éxito. John Snow ahora también es reconocido como uno de los fundadores de la epidemiología moderna <em>(algunos también lo consideran como el fundador de la visualización de datos, el análisis espacial, la ciencia de datos en general y muchos otros campos relacionados)</em> por su enfoque científico y bastante moderno en la recolección de datos para identificar la fuente de un brote de cólera en Soho, Londres, en 1854, pero no siempre fue así. De hecho, durante mucho tiempo fue simplemente ignorado por la comunidad científica y actualmente se mitifica con frecuencia.</p>
<p>En este cuaderno, no solo vamos a redescubrir su "historia de datos", sino también a analizar de nuevo los datos que recopiló en 1854 y recrear su famoso mapa (también conocido como El Mapa Fantasma).</p>
"""

#Descargar pandas
import pandas as pd

#Leer los datos
url = 'https://raw.githubusercontent.com/jdanifalcon/johnsnow/main/datasets/deaths.csv'

deaths = pd.read_csv(url,encoding = 'utf-8')

#Imprimir las primeras cinco filas
deaths.head()

#Imprimir el shape
print(deaths.shape)

"""## 2. ¡El Ataque del Cólera!
<p><img style="float: left;margin:5px 20px 5px 1px" src="https://assets.datacamp.com/production/project_132/img/johnsnow_cholera1.jpg"></p>
<p>Antes del descubrimiento de John Snow, el cólera era un visitante regular de las calles abarrotadas e insalubres de Londres. Durante la tercera epidemia de cólera, fue uno de los temas más estudiados (entre los años 1839-1856 se publicaron más de 700 estudios y ensayos solo en Londres) y casi todos los autores creían que los brotes se debían al miasma o al "aire malo".</p>
<p>Fue el trabajo pionero de John Snow con la anestesia y los gases lo que lo hizo dudar del modelo miasmático de la enfermedad. Originalmente formuló y publicó su teoría de que el cólera se propaga por el agua o los alimentos en un ensayo sobre el modo de comunicación del cólera (antes del brote de 1849). El ensayo recibió críticas negativas en The Lancet y en la London Medical Gazette.</p>
<p>Ahora sabemos que tenía razón, pero el dilema del Dr. Snow era cómo demostrarlo. Su primer paso para llegar allí fue verificar los datos. Nuestro conjunto de datos tiene 489 filas de datos en 3 columnas, pero para trabajar con él más fácilmente, primero haremos algunos cambios.</p>
"""

# Resumiendo el contenido de las muertes
deaths.info()

# Define los nuevos nombres de las columnas
newcols = {
    'Death': 'death_count',
    'X coordinate': 'x_latitude', 
    'Y coordinate': 'y_longitude' 
    }

# Renombralas
deaths.rename(columns=newcols, inplace=True)

# Describe los datos
deaths.describe()

"""## 3. ¡Usted no sabe nada, John Snow!
<p><img style="float: left;margin:5px 20px 5px 1px" src="https://assets.datacamp.com/production/project_132/img/johnsnow_cholera_king2.png"></p>
<p>De alguna manera era impensable que un solo hombre pudiera desacreditar la teoría del miasma y demostrar que todos los demás estaban equivocados, por lo que su trabajo fue en su mayoría ignorado. Sus colegas médicos simplemente decían: "¡No sabes nada, John Snow!"</p>
<p>Como ya se mencionó, el primer intento de John Snow por desacreditar la teoría del "miasma" terminó con críticas negativas. Sin embargo, un crítico hizo una sugerencia útil en términos de qué evidencia sería convincente: el experimento natural crucial sería encontrar personas que vivieran juntas con estilos de vida similares en todos los aspectos excepto en la fuente de agua. El brote de cólera en Soho, Londres, en 1854 le dio a Snow la oportunidad no solo de salvar vidas en esta ocasión, sino también de probar y mejorar aún más su teoría. Pero ¿qué pasa con la prueba final de que tenía razón?</p>
<p>Ahora sabemos cómo lo hizo John Snow, así que primero obtengamos los datos correctos.</p>
"""

#Cree 'ubicaciones' creando subconjuntos solo de Latitud y Longitud del conjunto de datos 
locations = deaths[['x_latitude', 'y_longitude']]

# Cree `deaths_list` transformando el DataFrame en una lista de listas
deaths_list = locations.values.tolist()

# Comprobar la longitud de la lista
len(deaths_list)

"""## 4. El Mapa Fantasma
<p><img style="float: left;margin:5px 20px 5px 1px" src="https://assets.datacamp.com/production/project_132/img/johnsnow_original.jpg"> </p>
<p>Desafortunadamente, su mapa original no está disponible (podría incluso nunca haber existido). Sin embargo, podemos ver el famoso que dibujó aproximadamente un año después en 1855, y se muestra en esta celda. Debido a que el mapa representa y visualiza las muertes, a veces también se le llama <strong>El Mapa Fantasma</strong>.</p>
<p>Ahora sabemos cómo lo hizo John Snow y también tenemos los datos, así que recreemos su mapa utilizando técnicas modernas.</p>
"""

# Trace los datos en el mapa (se proporciona la ubicación del mapa) usando folium y for loop para trazar todos los puntos
import folium

map = folium.Map(location=[51.5132119,-0.13666], tiles='Stamen Toner', zoom_start=17)
for point in range(0, len(deaths_list)):
    folium.CircleMarker(deaths_list[point], radius=8, color='red', fill=True, fill_color='red', opacity = 0.4).add_to(map)
map

"""## 5. ¡Es la bomba de agua!
<p><img style="float: left;margin:5px 20px 5px 1px" src="https://assets.datacamp.com/production/project_132/img/johnsnow_caricature1.jpg"></p>
<p>Después de marcar las muertes en el mapa, lo que John Snow vio no fue un patrón aleatorio (esto lo vimos también en nuestra recreación de The Ghost Map). La mayoría de las muertes se concentraban en la esquina de Broad Street (ahora Broadwick Street) y Cambridge Street (ahora Lexington Street). Un grupo de muertes alrededor de la intersección de estas calles fue el epicentro del brote, pero ¿qué había allí? Sí, una bomba de agua.</p>
<p>En ese momento, John Snow ya tenía desarrollada una teoría de que el cólera se propagaba a través del agua, por lo que para probar esto, también marcó en el mapa las ubicaciones de las bombas de agua cercanas. Y ahí estaba, todo el panorama.</p>
<p>Al combinar la ubicación de las muertes relacionadas con el cólera con las ubicaciones de las bombas de agua, Snow pudo demostrar que la mayoría estaban agrupadas alrededor de una bomba pública de agua en Broad Street, Soho. Finalmente, tenía la prueba que necesitaba.</p>
<p>Ahora haremos lo mismo y agregaremos las ubicaciones de las bombas a nuestra recreación de The Ghost Map.</p>
"""

#Importar los datos
url = 'https://raw.githubusercontent.com/jdanifalcon/johnsnow/main/datasets/pumps.csv'

pumps = pd.read_csv(url,encoding = 'utf-8')

# Importar datos
#pumps = pd.read_csv('datasets/pumps.csv')

# Cree `locations_pumps` creando subconjuntos solo de Latitud y Longitud del conjunto de datos
locations_pumps = pumps[['X coordinate', 'Y coordinate']]

# Cree `pumps_list` transformando el DataFrame en una lista de listas
pumps_list = locations_pumps.values.tolist()

# Cree un bucle for y trace los datos usando folium (use el mapa anterior + agregue otra capa)
map1 = map
for point in range(0, len(pumps_list)):
    folium.Marker(pumps_list[point], popup=pumps['Pump Name'][point]).add_to(map1)
map1

"""## 6.  ¡No sabes nada, John Snow! (de nuevo)
<p><img style="float: left;margin:5px 20px 5px 1px" src="https://assets.datacamp.com/production/project_132/img/johnsnow_map1.jpg"></p>
<p>Entonces, John Snow finalmente tuvo su prueba de que había una conexión entre las muertes como consecuencia del brote de cólera y la bomba de agua pública que probablemente estaba contaminada. Pero no se detuvo allí y siguió investigando.</p>
<p>Ahora estaba buscando anomalías (ahora diríamos "valores atípicos en los datos") y encontró dos en realidad donde no hubo muertes. La primera fue una cervecería justo en Broad Street, así que fue allí y descubrió que bebían principalmente cerveza (en otras palabras, no el agua de la bomba local, lo que confirma su teoría de que la bomba es la fuente del brote). El segundo edificio sin muertes fue una casa de trabajo cerca de Poland Street, donde descubrió que su fuente de agua no era la bomba de Broad Street (confirmación nuevamente). Las ubicaciones de ambos edificios también se visualizan en el mapa de la izquierda.</p>
<p>Ahora estaba seguro, y aunque los funcionarios no confiaban en él ni en su teoría, quitaron la manija de la bomba al día siguiente, el 8 de septiembre de 1854. John Snow luego recopiló y publicó en su famoso libro todos los datos sobre las muertes en orden cronológico, antes y después del pico del brote, y ahora analizaremos y compararemos el efecto cuando se quitó la manija.</p>
"""

# # Importar los datos de la manera correcta

url = 'https://raw.githubusercontent.com/jdanifalcon/johnsnow/main/datasets/dates.csv'

dates = pd.read_csv(url, parse_dates=['date'], encoding='utf-8')

# Establezca la fecha en que se retiró el mango (8 de septiembre de 1854)
handle_removed = pd.to_datetime('1854/9/8')

# Crear una nueva columna `day_name` en `dates` DataFrame con nombres del día 
dates['day_name'] = dates.date.dt.day_name()

# Cree una nueva columna `manejador` en el marco de datos de `fechas` basado en una fecha en la que se eliminó el mango
dates['handle'] = dates.date > handle_removed

# Comprobar el conjunto de datos y los tipos de datos
dates.info()

## Cree una comparación de cuántas muertes y ataques de cólera hubo antes y después de que se quitara el asa
dates.groupby(['handle']).sum()

"""## 7. La imagen vale más que mil palabras
<p><img style="float: left;margin:5px 20px 5px 1px" src="https://assets.datacamp.com/production/project_132/img/johnsnow_pump1.jpg"> </p>
<p>Al retirar la manija de la bomba, se evitó que se recogiera más agua infectada. Más tarde se descubrió que el manantial debajo de la bomba había sido contaminado con aguas residuales. Este acto fue reconocido más tarde como un ejemplo temprano de epidemiología, medicina de salud pública y la aplicación de la ciencia (la teoría germinal de las enfermedades) en una crisis real.</p>
<p>Una réplica de la bomba, junto con una placa explicativa y conmemorativa y sin una manija, fue erigida en 1992 cerca de la ubicación del original, cerca de la pared trasera de lo que hoy es el pub John Snow. El sitio está sutilmente marcado con un bordillo de granito rosa frente a una pequeña placa de pared.</p>
<p>Podemos aprender mucho de los datos de John Snow. Podemos echar un vistazo a los recuentos absolutos, pero esta observación podría llevarnos a una conclusión equivocada, así que tomemos una mirada diferente a los datos usando Bokeh.</p>
<p>Gracias a John Snow, tenemos los datos en orden cronológico (es decir, como datos de series temporales), por lo que la mejor manera de ver todo el panorama es visualizarlo y mirarlo de la manera en que él lo vio mientras escribía <em> Sobre el Modo de Comunicación del Cólera (1855)</em>.</p>
"""

import bokeh
from bokeh.plotting import output_notebook, figure, show
output_notebook(bokeh.resources.INLINE)

#Configurar la figura
p = figure(plot_width=900, plot_height=450, x_axis_type='datetime', tools='lasso_select, box_zoom, save, reset, wheel_zoom',
          toolbar_location='above', x_axis_label='Date', y_axis_label='Number of Deaths/Attacks', 
          title='Number of Cholera Deaths/Attacks before and after 8th of September 1854 (removing the pump handle)')

# Trazar
p.line(dates['date'], dates['deaths'], color='red', alpha=1, line_width=3, legend='Cholera Deaths')
p.circle(dates['date'], dates['deaths'], color='black', nonselection_fill_alpha=0.2, nonselection_fill_color='grey')
p.line(dates['date'], dates['attacks'], color='black', alpha=1, line_width=2, legend='Cholera Attacks')

show(p)

"""## 8. El mito de John Snow y... ¿Aprendimos algo?
<p><img style="float: left;margin:5px 20px 5px 1px" src="https://assets.datacamp.com/production/project_132/img/johnsnow_water1.jpg"> </p>
<p>A partir de la visualización interactiva anterior, podemos ver claramente que el pico del brote de cólera ocurrió antes de que se quitara la manivela y ya estaba en declive (trayectoria descendente) antes del 8 de septiembre de 1854.</p>
<p>Esta vista diferente de los datos es muy importante porque si comparamos solo números absolutos, esto podría llevarnos a la conclusión errónea de que la eliminación de la manivela de la bomba de Broad Street detuvo el brote, lo cual no es cierto (seguramente ayudó pero no detuvo el brote) y John Snow era consciente de esto (simplemente hizo lo que debía hacer y nunca aspiró a convertirse en un héroe).</p>
<p>Pero a la gente le encantan las historias sobre héroes y otros mitos (definitivamente más que la ciencia o la ciencia de datos). Según el mito de John Snow, era el superhéroe que en dos días desafió a sus iguales al proponer que el cólera era una enfermedad transmitida por el agua. A pesar de que nadie lo escuchaba, continuó valientemente dibujando su mapa, convenció a las autoridades locales para que retiraran la manivela de la bomba de agua infectada con sus hallazgos y detuvo el brote. John Snow salvó la vida de muchos londinenses.</p>
<p>Si observamos mejor detrás de esta historia, también podemos encontrar al verdadero John Snow, quien luchaba contra la enfermedad con herramientas limitadas y quería obtener pruebas de que tenía razón y "sabía algo" sobre el cólera. Simplemente hizo lo que pudo con el tiempo limitado que tenía y siempre hervía su agua antes de beberla.</p>
"""

# Según el mapa de John Snow y los datos que John Snow recolectó, ¿qué dirías?
#john_snow_knows_nothing = False