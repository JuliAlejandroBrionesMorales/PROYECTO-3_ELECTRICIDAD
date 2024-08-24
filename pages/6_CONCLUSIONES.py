# LIBRERIAS
import streamlit as st


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
        border-bottom: 2px solid #007bff; /* Línea azul debajo del título */
        padding-bottom: 10px; /* Espaciado debajo del título */
        margin-bottom: 20px; /* Espaciado debajo del título */
    }
</style>
'''
st.markdown(page_bg_color, unsafe_allow_html=True)


custom_title = '''
    <div class="title">
        CONCLUSIONES PROYECTO
    </div>
    '''
    
st.markdown(custom_title, unsafe_allow_html=True)
st.write('')
col1, col2, col3 = st.columns ([0.05,1,0.05])
with col2:
    st.markdown('''
            <div class="content-box">
                <div class="highlight">Punto 1:</div> Es fundamental elegir bien un tema y saber si se disponen de datos completos para poder llevar a cabo tu análisis.
                <div class="highlight">Punto 2</div> La electricidad es fundamentea en nuestra vida diaria, y saber de donde salen como salen y cual es el precio comparado con otros países.
                <div class="highlight">Punto 3</div> Resaltar el impacto que tienen los diferentes eventos sobre el precio de la electricidad/combustibles. Por ejemplo, el impacto que suponieron el COVID-19 y el inicio del enfrentamiento entre Ucrania y Rusia.
                <div class="highlight">Punto 4</div> Es importancia de conocer cuando son las mejores y peores horas para poder poner los electrodomésticos para poder ahorrar dinero (19:00 y 14:00 LT).
                <div class="highlight">Punto 5</div> Por último, resaltar la importancia de conocer bien los parámetros que son necesarios para poder hacer predicciones con Pycaret.
                <div Muchas gracias por escucharme y espero haberte ennseñador algo durante la presentación.<p>
            </div>
        ''', unsafe_allow_html=True)


