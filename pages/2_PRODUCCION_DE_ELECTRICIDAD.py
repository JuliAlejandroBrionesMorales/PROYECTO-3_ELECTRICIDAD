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

# TITULO Y EXPLICACIÓN
custom_title = '''
    <div class="title">
        PRODUCCIÓN DE ELECTRICIDAD
    </div>
    '''
st.markdown(custom_title, unsafe_allow_html=True) 
st.write('Esta sección pretender mostrar diferentes gráficos comparativos de la producción de electricidad entre diferentes países del mundo. España se encuentra dentro de los datos de producción, por lo que, podrá ser interesante ver la situación de España frente a otras nacionales.')
st.write('Por otro lado, aclarar que los datos obtenidos sobre la producción de electricidad varían desde 2010 hasta la actualidad. Es por ello que, todos los datos/graficos son con referencia a este rango de fechas.')
st.write('')


# -------------------- PUNTO 1 --------------------
st.markdown('#### <span style="color:orange;">1. PAISES CON DATOS DE PRODUCCION</span>', unsafe_allow_html=True)
st.write('Los países de los que disponemos datos sobre la producción de electricidad son los que se muestran en la siguiente gráfica:')
# Leer el contenido del archivo HTML
with open('img_presentacion/4_balance_total_por_paises.html', 'r') as file:
    html_content = file.read()
# Renderizar el contenido HTML
st.components.v1.html(html_content, height=450, scrolling=True)
st.write('* OCDE: Organización para la Cooperación y el Desarrollo Económico es un foro y centro de conocimientos públicos.')
st.write('')



# -------------------- PUNTO 2 --------------------
st.markdown('#### <span style="color:orange;">2. PRODUCCION DE ELECTRICIDAD</span>', unsafe_allow_html=True)
st.write('La producción de electricidad de los diferentes países que se encuentran en el dataframe son los siguientes:')
with open('img_presentacion/4.2_electricidad_de_acuerdo_balance.html', 'r') as file:
    html_content = file.read()
components.html(html_content, height=800)
with st.expander('BREVE EXPLICACION'): 
    st.write('Esta gráfica pretende mostrar las producción total de acuerdo al balance teniendo el cuenta como se divide la producción de la electricidad. Es una manera diferente de poder mostrar las 2 gráficas anteriores.')
# ---------------------
# Centramos el siguiente gráfico
with open('img_presentacion/4.1_balance.html', 'r') as file:
    html_content = file.read()
# Envolver el contenido HTML en un <div> centrado
centered_html = f"""
<div style="display: flex; justify-content: center; align-items: center; height: 100%;">
    {html_content}
</div>
"""
# Mostrar el contenido HTML centrado en la aplicación de Streamlit
components.html(centered_html, height=400)
with st.expander('BREVE EXPLICACION'): 
    st.write('Esta gráfica del tipo pastel muestra como se divide la producción de electricidad es nuestro dataframe. En ella, podemos encontrar la producción neta, pérdidas de distribución, exportaciones...')
# ---------------------
st.write('Ahora vamos a mostrar comparaciones más especificas del balance para que podamos ver las diferentes que existen entre los diferentes países:')
with open('img_presentacion/4.3_comparacion_Exportaciones Totales.html', 'r') as file:
    html_content = file.read()
components.html(html_content, height=450)
with st.expander('BREVE EXPLICACION'): 
    st.write('Como bien se ha mencionado antes, la intencione de estas gráficas es poder mostrar detalles específicos de la división de la producción. Cabe destacar como Alemania, Francia y Canada sobresalen del resto en cuanto exportaciones de electricidad.')
with open('img_presentacion/4.4_comparacion_Importaciones Totales.html', 'r') as file:
    html_content = file.read()
components.html(html_content, height=450)
with st.expander('BREVE EXPLICACION'): 
    st.write('En esta gráfica se muestra como se dividen las importaciones en el mes de marzo de 2024. Estados Unidos otra vez vuelve a ponerse en lo más alto en las gráficas de electricidad.')
with open('img_presentacion/4.5_comparacion_Pérdidas de Distribución.html', 'r') as file:
    html_content = file.read()
components.html(html_content, height=450)
with st.expander('BREVE EXPLICACION'): 
    st.write('Esta gráfica muestra las perdidas de electricidad por la distribución de la misma. Se puede ver como Estados Unidos sobresale del resto de manera notable. Es necesario destacar que Estados Unidos es uno de los países más grandes y consumistas del mundo, es por ello que, siempre se encuentra en los primeros puestos de nuestro análisis.')
st.write('')


# -------------------- PUNTO 3 --------------------
st.markdown('#### <span style="color:orange;">3. PRODUCTOS</span>', unsafe_allow_html=True)
st.write('A continuación, se muestran los productos que componen la producción de la electricidad:')
with open('img_presentacion/5_productos_paises.html', 'r') as file:
    html_content = file.read()
components.html(html_content, height=800)
with st.expander('BREVE EXPLICACION'): 
    st.write('Esta gráfica muestra el cantidad total de producción electricidad (medidos en gigavatios-hora) teniendo en cuenta los productos que componene las producción total. De esta manera, se puede ver fácilmente los productos que componen las producción de electricidad de cada uno de los países.')
# ---------------------
# Centramos el siguiente gráfico
with open('img_presentacion/5.1_porcentaje_productos.html', 'r') as file:
    html_content = file.read()
# Envolver el contenido HTML en un <div> centrado
centered_html = f"""
<div style="display: flex; justify-content: center; align-items: center; height: 100%;">
    {html_content}
</div>
"""
# Mostrar el contenido HTML centrado en la aplicación de Streamlit
components.html(centered_html, height=400)
with st.expander('BREVE EXPLICACION'): 
    st.write('Esta gráfica tipo pastel muestra los porcentajes en los que se divide la producción total de electricidad de acuerdo a los productos que componen a la misma.')
# ---------------------
st.write('Ahora vamos a mostrar comparaciones más especificas de los productos para que podamos ver las diferencias que existen entre los diferentes países:')
with open('img_presentacion/5.2_comparacion_Electricidad.html', 'r') as file:
    html_content = file.read()
components.html(html_content, height=450)
with st.expander('BREVE EXPLICACION'): 
    st.write('Aquí se muestra la electricidad neta de cada uno de los países, y como bien se ha mencionado antes Estados Unidos y China al ser naciones tan grandes y con tanto consumo se encuentran en las posiciones más elevadas del ranking.')
with open('img_presentacion/5.3_comparacion_Eólica.html', 'r') as file:
    html_content = file.read()
components.html(html_content, height=450)
with st.expander('BREVE EXPLICACION'): 
    st.write('Esta gráfica muestra la comparación eólica. Resalta como España se encuentre en los países con mayor producción de este tipo de energía junta a Alemania como representaciones europeas.')
with open('img_presentacion/5.4_comparacion_Nuclear.html', 'r') as file:
    html_content = file.read()
components.html(html_content, height=450)
with st.expander('BREVE EXPLICACION'): 
    st.write('Esta gráfica muestra la producción nuclear de los diferentes países que componen nuestro dataframe del mes de marzo. Resalta el puesto de Francia, debido a que siempre ha contado con un gran número de centrales nucleares. Este puede ser un factor importante por el cual los precios de la electricidad siempre suelen estar más bajo que los precios que nos podemos encontrar en España.')
with open('img_presentacion/5.5_comparacion_Hidráulica.html', 'r') as file:
    html_content = file.read()
components.html(html_content, height=450)
with st.expander('BREVE EXPLICACION'): 
    st.write('Esta gráfica muestra de forma comparativa la producción de electricidad de manera hidráulica. Resalta el puesto de Brasil, como siendo un país con tantas personas y tales magnitudes no lo hemos encontrado en puesto tan avanzados en los otros tipos de producción de electricidad.')
st.write('')
    

# -------------------- PUNTO 4 --------------------
st.markdown('#### <span style="color:orange;">4. PRODUCCION ESPAÑA</span>', unsafe_allow_html=True)
st.write('Esta sección muestra datos de España en cuanto a la producción de electricidad desde el año 2010.')
with open('img_presentacion/5.6_Evolucion_produccion_spain.html', 'r') as file:
    html_content = file.read()
components.html(html_content, height=400)
with st.expander('BREVE EXPLICACION'): 
    st.write('Esta gráfica muestra el evolución de la electricidad a lo largo del tiempo. Para ser exactos, muestra la evolución desde el 2010 hasta la actualidad (marzo-2024). Es importante resaltar, el impacto del covid sobre la producción de electricidad.')
# ---------------------
with open('img_presentacion/5.7_balance_totales_spain.html', 'r') as file:
    html_content = file.read()
components.html(html_content, height=400)
with st.expander('BREVE EXPLICACION'): 
    st.write('Esta gráfica muestra los valores que nos encontramos en el balance en España. Se muestra el porcentaje que representan cada uno de los valores de balances sobre el total de producción.')
# ---------------------
with open('img_presentacion/5.8_product_totales_spain.html', 'r') as file:
    html_content = file.read()
components.html(html_content, height=400)
with st.expander('BREVE EXPLICACION'): 
    st.write('Esta gráfica muestra los productos que componen las producción en España y también el porcentaje que representa sobre el total de producción.')
# ---------------------