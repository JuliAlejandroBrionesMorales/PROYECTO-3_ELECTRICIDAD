# LIBRERIAS
import streamlit as st
import joblib
import pandas as pd
import plotly.express as px
from sklearn.pipeline import Pipeline
from pycaret.time_series import predict_model  
import xgboost as xgb


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
        PREDICTOR ELECTRICIDAD ESPAÑA
    </div>
    '''
st.markdown(custom_title, unsafe_allow_html=True)



# -----------------INTRODDUCCION------------------
st.write('')
st.write('Esta sección se enfoca en mostrar 1 de los 3 predictores realizados durante este proyecto. Para ser concretamos vamos a mostrar el predictor del precio de la Electricidad en España.')
st.write('----------------------------------------------------------------------------------------------------------------------------')
st.write('Seleccione el tiempo para el cual desea predecir el precio de la electricidad en España.')

# Cargar el modelo guardado
model2 = joblib.load('predictores_pkl/3_modelo_predictor_electricidad_dias_españa.pkl')

# Solicitar el número de días en el futuro a predecir
fh = st.number_input('Ingrese el número de días en el futuro que desea predecir a partir del 01-07-2024', min_value=1, max_value=365, value=60)

# Realizar predicción al presionar el botón
if st.button('Predictor'):
    try:
        # Realizar la predicción
        future_predictions = model2.predict(fh=fh)
        
        # Mostrar las predicciones
        st.write('Predicciones para los próximos días:')
        st.write(future_predictions)
        
        # Cargamos el dataframe de electricidad
        df_electricidad_españa = pd.read_csv('data/datos_limpios/3_df_electricidad_España.csv')
        df_electricidad_españa['date']=pd.to_datetime(df_electricidad_españa['date'], format='mixed')
        df_electricidad_españa  = df_electricidad_españa.groupby(['date'])['Value(€/MWh)'].mean().reset_index()
        fig = px.line(df_electricidad_españa, x= 'date', y='Value(€/MWh)', title='Evolución del precio de electricidad en España')
        st.plotly_chart(fig)
      
        
    except Exception as e:
        st.error(f'Ocurrió un error durante la predicción: {e}')
