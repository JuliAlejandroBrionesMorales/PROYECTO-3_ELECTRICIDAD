# LIBRERIAS
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# CSS PARA CAMBIAR COLOR DE FONDO
page_bg_color = '''
<style>
    .stApp {
        background-color: #E0E0E0; /* Gris más oscuro */
    }
    .title {
        color: #ffffff;
        text-align: center;
        font-size: 60px;
        font-family: 'Arial', sans-serif;
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        padding: 20px;
        border-radius: 10px;
    }
    .content-box {
        background-color: #ffffff; /* Fondo blanco para el contenido */
        border: 2px solid #d1d1d1; /* Borde gris claro */
        border-radius: 10px; /* Bordes redondeados */
        padding: 20px; /* Espaciado interno */
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); /* Sombra sutil */
        font-family: 'Arial', sans-serif; /* Fuente consistente */
    }
    .highlight {
        color: #007bff; /* Color azul para resaltar puntos clave */
        font-weight: bold;
    }
    .section-title {
        font-size: 24px; /* Tamaño de fuente para los títulos de sección */
        border-bottom: 2px solid #007bff; /* Línea azul debajo del título */
        padding-bottom: 10px; /* Espaciado debajo del título */
        margin-bottom: 20px; /* Espaciado debajo del título */
    }
</style>
'''
st.markdown(page_bg_color, unsafe_allow_html=True)


custom_title = '''
    <div class="title">
        ELECTRICIDAD EN ESPAÑA
    </div>
    '''
st.markdown(custom_title, unsafe_allow_html=True)



# -------- INTRODUCCION ----------------
st.write('Esta sección se enfoca en poder mostrar el precio de la electricidad en España a lo largo del tiempo. Para ello, hemos seleccionado datos desde el 2019. ')



# -------------------- PUNTO 1 --------------------
st.markdown('#### <span style="color:orange;">1. PRECIO DE ELECTRICIDAD</span>', unsafe_allow_html=True)
st.write('Vamos a mostrar gráficas del precio promedio de la electricidad (€/MWh) por año, el precio promedio de los meses y la evolución del precio por horas.')
# Leer el contenido del archivo HTML
with open('img_presentacion/8_precio_medio_electricidad_año.html', 'r') as file:
    html_content = file.read()
# Renderizar el contenido HTML
st.components.v1.html(html_content, height=450, scrolling=True)
with st.expander('BREVE EXPLICACION'): 
    st.write('Esta gráfica muestra el precio promedio de la electricidad por año desde el año 2018 hasta el 2024. Es importante aclarar que el precio promedio de la electricidad del año 2018 y 2024 no son completos porque para ambos año no se obtuvieron todos los datos del año completo. Es importante resaltar el precio promedio del año 2022 debido al inicio del conflicto entre Ucrania y Rusia (Rusia es uno de los mayores proveedores de gas natural a Europa).')

# Leer el contenido del archivo HTML
with open('img_presentacion/8.1_evolucion_precio_durante_año.html', 'r') as file:
    html_content = file.read()
# Renderizar el contenido HTML
st.components.v1.html(html_content, height=450, scrolling=True)
with st.expander('BREVE EXPLICACION'): 
    st.write('Esta gráfica muestra el precio de la electricidad a lo largo de los meses. En esta gráfica se representa los diferentes años. Es importante resaltar como al final de 2021 el precio de la electricidad subio casi a los máximos del año 2022. Este aumento se debió principalmente al aumento de los precios del gas natural, incremento en los precios de los derechos de emisión de carbono, incremento de demanda por recuperación de economía tras COVID-19,...etc.')

# Leer el contenido del archivo HTML
with open('img_presentacion/8.2_precios_promedios_horas_años.html', 'r') as file:
    html_content = file.read()
# Renderizar el contenido HTML
st.components.v1.html(html_content, height=450, scrolling=True)
with st.expander('BREVE EXPLICACION'): 
    st.write('Esta gráfica muestra el precio promedio de las horas de un día normal de cada uno de los años que componen nuestro dataframe. En las gráficas podemos ver un patron similiar en cuanto a la hora con el precio más grande. El precio más alto suele ser frecuente a las 19:00 horas y entre las 06:00 y 07:00 horas.s')
st.write('')


# -------------------- PUNTO 2 --------------------
st.markdown('#### <span style="color:orange;">2. ANALISIS DE PRECIO POR HORAS POR AÑO</span>', unsafe_allow_html=True)
st.write('A continuación, se muestra el precio promedio por horas para cada uno de los años de nuestro dataframe, para que podemos identificar las horas con los precio más altos.')
# Leer el contenido del archivo HTML
with open('img_presentacion/9_grafico_2019.html', 'r') as file:
    html_content = file.read()
# Renderizar el contenido HTML
st.components.v1.html(html_content, height=450, scrolling=True)

# Leer el contenido del archivo HTML
with open('img_presentacion/9.1_grafico_2020.html', 'r') as file:
    html_content = file.read()
# Renderizar el contenido HTML
st.components.v1.html(html_content, height=450, scrolling=True)

# Leer el contenido del archivo HTML
with open('img_presentacion/9.2_grafico_2021.html', 'r') as file:
    html_content = file.read()
# Renderizar el contenido HTML
st.components.v1.html(html_content, height=450, scrolling=True)

# Leer el contenido del archivo HTML
with open('img_presentacion/9.3_grafico_2022.html', 'r') as file:
    html_content = file.read()
# Renderizar el contenido HTML
st.components.v1.html(html_content, height=450, scrolling=True)

# Leer el contenido del archivo HTML
with open('img_presentacion/9.4_grafico_2023.html', 'r') as file:
    html_content = file.read()
# Renderizar el contenido HTML
st.components.v1.html(html_content, height=450, scrolling=True)

# Leer el contenido del archivo HTML
with open('img_presentacion/9.5_grafico_2024.html', 'r') as file:
    html_content = file.read()
# Renderizar el contenido HTML
st.components.v1.html(html_content, height=450, scrolling=True)
with st.expander('BREVE EXPLICACION'): 
    st.write('Como hemos visto en las gráficas anteriores, el precio promedio por horas cambia de un año para otro por diversos motivos. Pero hay ciertas horas que siempre se mantienen en lo más alto en comparación con las otras horas, y son las 18:00-19:00-20:00 como las horas con los precios más elevados debido a la alta demanda de electricidad a esas horas. Por otro lado, las horas de la madrugada suelen contener los precios más bajo, pero cabe resaltar las 14:00 horas como un precio relativamente bajo en comparación con las otras horas (recomendamos esas horas para poder utilizar los aparatos en caso debido al precio promedio general que suele presentar.)')
st.write('')



# -------------------- PUNTO 3 --------------------
st.markdown('#### <span style="color:orange;">3. COMPARACION MESES</span>', unsafe_allow_html=True)
st.write('Esta última sección pretende mostrar el mes con el precio más alto y más bajo por año para que podamos si existen patrones de meses en las subidas y bajadas de precio de la electricidad. ')
# Leer el contenido del archivo HTML
with open('img_presentacion/10_grafico_maximos_bar.html', 'r') as file:
    html_content = file.read()
# Renderizar el contenido HTML
st.components.v1.html(html_content, height=450, scrolling=True)
with open('img_presentacion/10.1_grafico_minimos_bar.html', 'r') as file:
    html_content = file.read()
# Renderizar el contenido HTML
st.components.v1.html(html_content, height=450, scrolling=True)
with st.expander('BREVE EXPLICACION'): 
    st.write('No se puede encontrar un tendencia clara en cuanto los meses con los precios más altos y bajos de cada uno de los años, pero si podemos decir que los meses finales de los años suelen tener los precio más bajos y los primeros meses de los años suelen tener los precios más elevado debido a la alta demanda. Es importante recalcar, que hay cierto años que tienen los datos de la electricidad borrosos debido a la acontecimiento ocurridos en esos año como pueden ser el año del COVID-19 o el inicio del conflicto entre Rusia y Ucrania.')
