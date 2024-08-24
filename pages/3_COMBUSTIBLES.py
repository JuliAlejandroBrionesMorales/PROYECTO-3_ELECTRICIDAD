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
        COMBUSTIBLES
    </div>
    '''
st.markdown(custom_title, unsafe_allow_html=True)
# -------- INTRODUCCION ----------------
st.write('En esta sección se van a mostrar diferentes gráficos comparativos y la evolución del diesel, gasolina y gasóleo para calefacción doméstica. También se va a poner un ejemplo comparativo para que podamos ver la diferencia que gasto que supone residir en un lugar u otro.')
st.write('Por otro lado, es importante resaltar que los datos estudiados constan desde 2015. A continuación, se muestran el estudio realizado.')


# -------------------- PUNTO 1 --------------------
st.markdown('#### <span style="color:orange;">1. PRECIO MEDIO DE COMBUSTIBLES </span>', unsafe_allow_html=True)
st.write('Las siguientes gráficas muestran el precio medio de los combustibles antes mecionado desde el año 2015.')
# Leer el contenido del archivo HTML
with open('img_presentacion/6_precio_medio_por_pais_y_producto.html', 'r') as file:
    html_content = file.read()
# Renderizar el contenido HTML
st.components.v1.html(html_content, height=450, scrolling=True)
with st.expander('BREVE EXPLICACION'): 
    st.write('Esta gráfica muestra el precio medio de los tres combustibles en una sola gráfica. Es decir, se puede ver el precio medio por país del diesel, gasolina y gasóleo para calefacción doméstica.')

with open('img_presentacion/6.1_precio_medio_por_pais_en_Gasolina_(unidad_litro).html', 'r') as file:
    html_content = file.read()
# Renderizar el contenido HTML
st.components.v1.html(html_content, height=450, scrolling=True)
with st.expander('BREVE EXPLICACION'): 
    st.write('Esta gráfica muetra el precio medio de la gasolina desde el 2015 de los diferentes países que componen nuestro dataframe.')

with open('img_presentacion/6.2_precio_medio_por_pais_en_Diesel_(unidad_litro).html', 'r') as file:
    html_content = file.read()
# Renderizar el contenido HTML
st.components.v1.html(html_content, height=450, scrolling=True)
with st.expander('BREVE EXPLICACION'): 
    st.write('Esta gráfica muetra el precio medio de la diesel desde el 2015 de los diferentes países que componen nuestro dataframe.')

with open('img_presentacion/6.3_precio_medio_por_pais_en_Gasóleo_para_calefacción_doméstica_(unidad_litro).html', 'r') as file:
    html_content = file.read()
# Renderizar el contenido HTML
st.components.v1.html(html_content, height=450, scrolling=True)
with st.expander('BREVE EXPLICACION'): 
    st.write('Esta gráfica muetra el precio medio de la gasóleo de calefacción doméstica desde el 2015 de los diferentes países que componen nuestro dataframe.')
st.write('')
st.markdown('##### <span style="color:orange;">EJEMPLO: comparaciones de gastos de combustibles </span>', unsafe_allow_html=True)
st.write('Vamos hacer una pequeña prueba del dinero gastado en los diferentes productos (diesel, gasolina y gasóleo) en función del país donde se viva. Para poder hacer esta pequeña comparación, vamos a comparar el país con el precio más alto y más bajo por producto con España.')
st.write('Es importante aclarar, que para este estudio hemos seleccionado el precio medio de los combustibles a lo largo del tiempo y hemos seleccionado el consumo medio en un año para los diferenntes combustibles.')
col1, col2, col3 = st.columns(3)
with col1:
    with st.expander('COMPARACION DIESEL'):
        st.markdown('* **Suecia (máx)**: 1.804779')
        st.markdown('* **Estados Unidos (min)**: 0.8584071')
        st.markdown('* **España**: 1.416161')
        st.markdown('*El dinero que te ahorras por vivir en España en vez de Suecia es de: **582.9269999999997***')
        st.markdown('*El dinero que te gastas de más por vivir en España en vez de Estados Unidos es de: **836.63085***')
with col2:
    with st.expander('COMPARACION GASOLINA'):
        st.markdown('* **Países Bajos (máx)**: 1.909292')
        st.markdown('* **Estados Unidos (min)**: 0.7402655')
        st.markdown('* **España**: 1.521161')
        st.markdown('*El dinero que te ahorras por vivir en España en vez de Paises Bajos es de: **291.09825***')
        st.markdown('*El dinero que te gastas de más por vivir en España en vez de Estados Unidos es de: **585.6716250000001***')
with col3:
    with st.expander('COMPARACION GASOLEO'):
        st.markdown('* **Dinamarca (máx)**: 1.607522')
        st.markdown('* **India (min)**: 0.4899107')
        st.markdown('* **España**: 0.8854464')
        st.markdown('*El dinero que te ahorras por vivir en España en vez de Dinamarca  es de: **1083.1134***')
        st.markdown('*El dinero que te gastas de más por vivir en España en vez de India  es de: **593.30355***')
st.write('')

# -------------------- PUNTO 2 --------------------
st.markdown('#### <span style="color:orange;">2. EVOLUCIÓN POR TIEMPO DE LOS COMBUSTIBLES </span>', unsafe_allow_html=True)
st.write('Las siguientes gráficas muestran la evolución del precio de los combustibles a lo largo de tiempo (meses/años).')
# Leer el contenido del archivo HTML
with open('img_presentacion/7_precio_medio_diesel_por_año.html', 'r') as file:
    html_content = file.read()
# Renderizar el contenido HTML
st.components.v1.html(html_content, height=450, scrolling=True)
with st.expander('BREVE EXPLICACION'): 
    st.write('Esta gráfica muestra la evolución del precio medio del diesel por año desde el 2015')

# Leer el contenido del archivo HTML
with open('img_presentacion/7.1_precio_medio_gasolina_por_año.html', 'r') as file:
    html_content = file.read()
# Renderizar el contenido HTML
st.components.v1.html(html_content, height=450, scrolling=True)
with st.expander('BREVE EXPLICACION'): 
    st.write('Esta gráfica muestra la evolución del precio medio de la gasolina por año desde el 2015')
    
# Leer el contenido del archivo HTML
with open('img_presentacion/7.2_precio_medio_gasoleo_por_año.html', 'r') as file:
    html_content = file.read()
# Renderizar el contenido HTML
st.components.v1.html(html_content, height=450, scrolling=True)
with st.expander('BREVE EXPLICACION'): 
    st.write('Esta gráfica muestra la evolución del precio del gasóleo para calefacción doméstica por año desde el 2015')

# Leer el contenido del archivo HTML
with open('img_presentacion/7.3_precio_medio_diesel_por_mes.html', 'r') as file:
    html_content = file.read()
# Renderizar el contenido HTML
st.components.v1.html(html_content, height=450, scrolling=True)
with st.expander('BREVE EXPLICACION'): 
    st.write('Esta gráfica muestra la evolución del precio medio del diesel a lo largo de los meses desde el 2015. De esta manera se puede ver de manera más detalla la evolución del precio medio del diesel a lo largo de tiempo.')
    
# Leer el contenido del archivo HTML
with open('img_presentacion/7.4_precio_medio_gasolina_por_mes.html', 'r') as file:
    html_content = file.read()
# Renderizar el contenido HTML
st.components.v1.html(html_content, height=450, scrolling=True)
with st.expander('BREVE EXPLICACION'): 
    st.write('Esta gráfica muestra la evolución del precio medio de la gasolina a lo largo de los meses desde el 2015. De esta manera se puede ver de manera más detalla la evolución del precio medio de la gasolina a lo largo de tiempo.')

# Leer el contenido del archivo HTML
with open('img_presentacion/7.5_precio_medio_gasoleo_por_mes.html', 'r') as file:
    html_content = file.read()
# Renderizar el contenido HTML
st.components.v1.html(html_content, height=450, scrolling=True)
with st.expander('BREVE EXPLICACION'): 
    st.write('Esta gráfica muestra la evolución del precio medio del gasóleo para calefacción doméstica a lo largo de los meses desde el 2015. De esta manera se puede ver de manera más detalla la evolución del precio medio del gasóleo para calefacción doméstica a lo largo de tiempo.')

# Leer el contenido del archivo HTML
with open('img_presentacion/7.6_precio_medio_productos_por_año.html', 'r') as file:
    html_content = file.read()
# Renderizar el contenido HTML
st.components.v1.html(html_content, height=450, scrolling=True)
with st.expander('BREVE EXPLICACION'): 
    st.write('Esta gráfica muestra la comparación a lo largo del tiempo de estos tres combustibles. Es importante resaltar como en el año 2022 el precio medio del diesel fue más alto que el precio medio de la gasolina. Este incremento del precio diesel se debió a un incremento de la demanda del diésel (especialmente para el transporte de mercancía en Europa),problemas de suministro por la invasión de Ucrania por parte de Rusia (Rusia es uno de los principales proveedores de diésel de Europa), entre otros factores.')




