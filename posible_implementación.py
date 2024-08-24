# LIBRERIAS
import streamlit as st
import joblib
import pandas as pd
import plotly.express as px
from sklearn.pipeline import Pipeline
from pycaret.time_series import predict_model  
import xgboost as xgb

#---------------------- EXPLICACION --------------------------------------
'''
Esta sección del trabajo pretende mostrar posibles predictores que se pueden utilizar en la presentación o en el trabajo.

Tenemos predictores para ver la producción de electricidad de diferentes países y para predecir el precio de combustibles en diferentes países. 

'''


# ------------------- PREDICTOR 1: PRODUCCION ELECTRICIDAD -------------------

# Mostrar la interfaz de Streamlit
st.markdown('## <span style="color:orange;">1. PREDICCION DE PRODUCCION DE ELECTRICIDAD</span>', unsafe_allow_html=True)
st.write('Selecciona los valores a continuación para hacer una predicción de producción de electricidad.')

# Cargar el pipeline y el modelo
pipeline = joblib.load('predictores_pkl/1_modelo_predicción_electricidad.pkl')

# Seleccionar el país
country = st.selectbox('Selecciona el país', [
    'Australia', 'Austria', 'Belgium', 'Canada', 'Chile', 'Colombia',
    'Costa Rica', 'Czech Republic', 'Denmark', 'Estonia', 'Finland',
    'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland',
    'Italy', 'Japan', 'Korea', 'Latvia', 'Lithuania', 'Luxembourg',
    'Mexico', 'Netherlands', 'New Zealand', 'Norway', 'Poland',
    'Portugal', 'Slovak Republic', 'Slovenia', 'Spain', 'Sweden',
    'Switzerland', 'Republic of Turkiye', 'United Kingdom',
    'United States', 'Argentina', 'Brazil', 'Bulgaria',
    "People's Republic of China", 'Croatia', 'Cyprus', 'India',
    'Malta', 'North Macedonia', 'Romania', 'Serbia'
])

# Seleccionar el balance
balance = st.selectbox('Selecciona el balance', [
    'Producción Neta de Electricidad', 'Usado para almacenamiento por bombeo',
    'Pérdidas de Distribución', 'Consumo Final (Calculado)', 'Importaciones Totales',
    'Exportaciones Totales'
])

# Seleccionar producto
product = st.selectbox('Selecciona el producto', [
    'Electricidad', 'Total de Combustibles', 'Carbón, Turba y Gases Manufacturados',
    'Petróleo y Productos Derivados', 'Gas Natural', 'Renovables Combustibles',
    'Hidráulica', 'Eólica', 'Solar', 'Total Renovables (Hidráulica, Geo, Solar, Eólica, Otros)',
    'Otros Combustibles No Renovables', 'Geotérmica', 'No Especificado', 'Nuclear', 'Otras Renovables'
])

# Seleccionar la fecha usando un date_input
selected_date = st.date_input("Selecciona la fecha", pd.to_datetime('2024-03-01'))
year, month, day = selected_date.year, selected_date.month, selected_date.day

# Seleccionar unidad
unit = st.selectbox('Selecciona la unidad', ['kWh'])  # Asegúrate de que estos valores están en tu dataset

# Crear DataFrame de entrada para la predicción
input_data = pd.DataFrame({
    'Time': [selected_date],
    'Country': [country],
    'Balance': [balance],
    'Product': [product],
    'Unit': [unit]
})

# Extraer 'Year', 'Month' y 'Day' de la columna 'Time'
input_data['Time'] = pd.to_datetime(input_data['Time'], utc=True)
input_data['Year'] = input_data['Time'].dt.year
input_data['Month'] = input_data['Time'].dt.month
input_data['Day'] = input_data['Time'].dt.day

# Predictor
if st.button('Predictor 1'):
    try:
        # Realizar predicción
        predictions = predict_model(pipeline, input_data)
        
        # Obtener el nombre correcto de la columna de predicción
        pred_col = 'prediction_label'  
        if pred_col in predictions.columns:
            prediction_value = predictions[pred_col].values[0]
            st.write(f'La predicción de producción de electricidad es: {prediction_value:,.2f} GWh')
            
            # Crear nueva fila con la predicción
            nueva_fila = pd.DataFrame({
                'Time': [pd.Timestamp(f'{year}-{month:02d}-{day:02d}').tz_localize('UTC')],
                'Value': [prediction_value]
            })
        
            df_filtrado = pd.read_csv('data/datos_limpios/1_df_produccion_electricidad.csv')
            # Creamos dataframe con todas las columnas peros seleccionando el country y balance seleccionado
            df_filtrado = df_filtrado[df_filtrado['Country'] == country]
            df_filtrado = df_filtrado[df_filtrado['Balance'] == balance]
            df_filtrado['Time'] = pd.to_datetime(df_filtrado['Time'], format='mixed')

            # Creamos grafico de evolución
            value_month = df_filtrado.groupby('Time')['Value'].sum().reset_index()
            fig = px.line(value_month, x='Time', y='Value', title=f'Evolución de la {balance} en {country}')
            # Mostrar la gráfica en Streamlit
            st.plotly_chart(fig)
            
        else:
            st.error(f"La columna '{pred_col}' no se encuentra en el DataFrame de predicciones.")
    except Exception as e:
        st.error(f"Ocurrió un error: {e}")
        
        

# ------------------- PREDICTOR 2: PRECIO DE COMBUSTIBLES -------------------
st.markdown('## <span style="color:orange;">2. PREDICTOR PRECIO DE COMBUSTIBLES</span>', unsafe_allow_html=True)
st.write('Selecciona los valores necesarios para poder hacer una predicción del precio del combustible deseado.')

# Cargar el pipeline y el modelo
model1 = joblib.load('predictores_pkl/2_modelo_prediccion_valor_combustible.pkl')

# Seleccionar COUNTRY
country = st.selectbox('Selecciona el país', [
    'Austria', 'Belgium', 'Bulgaria', 'Canada', 'Croatia', 'Cyprus',
    'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France',
    'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Japan',
    'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands',
    'Poland', 'Portugal', 'Romania', 'Slovak Republic', 'Slovenia',
    'Spain', 'Sweden', 'United Kingdom', 'United States', 'Brazil',
    'India'
])

# Seleccionar PRODUCT
product = st.selectbox('Selecciona el combustible', [
    'Gasolina (unidad/litro)', 'Diesel (unidad/litro)',
    'Gasóleo para calefacción doméstica (unidad/litro)'
])

# Seleccionar FLOW
flow = st.selectbox('Selecciona el flujo', ['Precio total'])

# Seleccionar UNIT
unit = st.selectbox('Selecciona la unidad', ['Dolar Estadounidense'])

# Seleccionar TIME usando un date_input
selected_date = st.date_input("Selecciona la fecha", pd.to_datetime('2024-08-15'))
year, month = selected_date.year, selected_date.month

# Crear el DataFrame de entrada para la predicción
input_data = pd.DataFrame({
    'TIME': [selected_date],
    'COUNTRY': [country],
    'PRODUCT': [product],
    'FLOW': [flow],
    'UNIT': [unit],
    'YEAR': [year],
    'MONTH': [month]
})

# Si no necesitas 'TIME' para la predicción, puedes excluirla
#input_data = input_data.drop(columns=['TIME'])

# Reordenar las columnas en el orden que espera el modelo
ordered_columns = ['YEAR', 'MONTH', 'COUNTRY', 'PRODUCT', 'FLOW', 'UNIT', 'TIME']
input_data = input_data[ordered_columns]

# Predictor
if st.button('Predector 2'):
    try:
        # Transformar los datos usando el pipeline del modelo
        transformed_data = model1[:-1].transform(input_data)
        
        # Realizar la predicción usando el modelo final
        predictions = model1.named_steps['final_model'].predict(transformed_data)

        # La salida debería tener una columna 'prediction_label'
        prediction_value = predictions[0]
        st.write(f'La predicción del precio del {product} es: {prediction_value:,.2f} $/l')

        # Crear nueva fila con la predicción
        nueva_fila = pd.DataFrame({
            'TIME': [pd.Timestamp(f'{year}-{month:02d}-01').tz_localize('UTC')],
            'VALUE': [prediction_value]
        })

        df_combustible = pd.read_csv('data/datos_limpios/2_df_petroleo.csv')
        df_combustible = df_combustible[(df_combustible['COUNTRY'] == country) & (df_combustible['PRODUCT'] == product)]
        df_combustible['TIME'] = pd.to_datetime(df_combustible['TIME'], format='mixed')

        # Crear gráfico de evolución
        value_month = df_combustible.groupby('TIME')['VALUE'].sum().reset_index()
        fig = px.line(value_month, x='TIME', y='VALUE', title=f'Evolución de la {product} en {country}')
        st.plotly_chart(fig)

    except Exception as e:
        st.error(f"Ocurrió un error: {e}")