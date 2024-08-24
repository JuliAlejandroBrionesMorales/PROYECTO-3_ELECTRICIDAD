# LIBRERIAS
import streamlit as st
import pandas as pd
import time
import streamlit.components.v1 as components



# CONFIGURACION DE PÁGINA
st.set_page_config(page_title='ELECTRICIDAD', layout='wide', page_icon='🔌')
st.sidebar.success('Julio Alejandro Briones Morales')
st.sidebar.success('Upgrade - Data Analytics')


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
        color: #FFA500; /* Color naranja para resaltar puntos clave */
        font-weight: bold;
    }
    .section-title {
        font-size: 24px; /* Tamaño de fuente para los títulos de sección */
        border-bottom: 2px solid #FFA500; /* Línea naranja debajo del título */
        padding-bottom: 10px; /* Espaciado debajo del título */
        margin-bottom: 20px; /* Espaciado debajo del título */
    }
</style>
'''

st.markdown(page_bg_color, unsafe_allow_html=True)


custom_title = '''
    <div class="title">
        PRESENTACIÓN
    </div>
    '''
st.markdown(custom_title, unsafe_allow_html=True)
st.write('')
col1, col2 = st.columns(2)
with col1:
    st.image('img_presentacion/1_presentacion.jpeg')
with col2:
    st.markdown('''
            <div class="content-box">
                <h2 class="section-title">Bienvenidos</h2>
                <p>Bienvenidos a esta presentación sobre la electricidad en España. Exploraremos los siguientes puntos clave:</p>
                <ul>
                    <li><span class="highlight">Precios de la Electricidad por Años:</span> análisis de la variación de los precios en los últimos años.</li>
                    <li><span class="highlight">Evolución de los Precios:</span> Tendencias y cambios significativos.</li>
                    <li><span class="highlight">Comparativa del Uso de la Electricidad:</span> comparación del uso de electricidad en España frente a otros países europeos.</li>
                </ul>
                <p>Utilizaremos gráficos interactivos y análisis de datos para ofrecer una visión clara y concisa del mercado eléctrico en España. Esperamos que esta información sea útil para comprender el panorama eléctrico.</p>
                <p><strong>Gracias por acompañarnos.</strong></p>
            </div>
        ''', unsafe_allow_html=True)



st.markdown('#### DATAFRAMES')
col1, col2 = st.columns ([0.8, 0.5])
with col1:
    with st.expander('DF_PRODUCCION_ELECTRICIDAD'):
        df_produccion = pd.read_csv('img_presentacion/0_df_produccion.csv')
        df_produccion
    with st.expander('DF_COMBUSTIBLES'):
        df_combustibles = pd.read_csv('img_presentacion/0.1_df_combustibles.csv')    
        df_combustibles
    with st.expander('DF_ELECTRICIDAD_ESPAÑA'):
        df_electricidad_españa = pd.read_csv('img_presentacion/0.2_df_electricidad_españa.csv')
        df_electricidad_españa
with col2:
    st.write('')
        
    



















