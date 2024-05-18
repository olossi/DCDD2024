# Importar Streamlit y otros módulos necesarios
import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Cargar los modelos entrenados
model_diabetes = joblib.load('Modelos/diabetes_model.pkl')
model_hipertension = joblib.load('Modelos/hipertension_model.pkl')
model_cardio = joblib.load('Modelos/ecv_model.pkl')
model_multi = joblib.load('Modelos/multi_label_model.pkl')

# Definir la aplicación Streamlit
def main():
    st.title('Aplicación de Predicción de Enfermedades Crónicas')

# Sidebar para la entrada de datos del usuario
    st.sidebar.header('Ingresa tus datos:')
    st.write('\n\n')
    
# Medidas Corporales
    st.sidebar.subheader('Medidas Corporales')
    sexo = st.sidebar.selectbox('Sexo', ['Hombre', 'Mujer'])
    edad_str = st.sidebar.text_input('Edad (años cumplidos)', value='18')
    try:
        edad = int(edad_str)
        if edad < 18 or edad > 100:
            st.sidebar.error('Por favor, ingresa una edad válida entre 18 y 100.')
    except ValueError:
            st.sidebar.error('Por favor, ingresa un número válido para la edad.')
    peso_str = st.sidebar.text_input('Peso (en kg)', value='30.0')
    try:
        peso = float(peso_str)
        if peso < 30.0 or peso > 300.0:
            st.sidebar.error('Por favor, ingresa un peso válido entre 30.0 y 300.0 kg.')
    except ValueError:
        st.sidebar.error('Por favor, ingresa un número válido para el peso.')

    altura_str = st.sidebar.text_input('Altura (en cm)', value='100')
    try:
        altura = int(altura_str)
        if altura < 100 or altura > 250:
            st.sidebar.error('Por favor, ingresa una altura válida entre 100 y 250 cm.')
    except ValueError:
        st.sidebar.error('Por favor, ingresa un número válido para la altura.')
    
    # Calcular el IMC
    imc = 0  # Inicializar imc
    if peso and altura:
        imc = np.round(peso / ((altura / 100) ** 2), 2)
        st.write('\n\n')
        # Determinar el color a mostrar basado en el valor del IMC
    if imc is not None:
        if imc < 18.5:
            color = 'yellow'
            nivel_peso = 'Bajo peso'
        elif imc < 25:
            color = 'green'
            nivel_peso = 'Normal'
        elif imc < 30:
            color = 'orange'
            nivel_peso = 'Sobrepeso'
        else:
            color = 'red'
            nivel_peso = 'Obesidad'
        # Mostrar el IMC con el color correspondiente
        st.markdown(f'<p style="font-size:20px;">Tu Índice de Masa Corporal es <span style="color:{color};">{imc} ({nivel_peso}) </span> </p>', unsafe_allow_html=True)
        st.write('\n\n')
    
    circunferencia_cintura_str = st.sidebar.text_input('Circunferencia de cintura (en cm)', value='30')
    try:
        circunferencia_cintura = int(circunferencia_cintura_str)
        if circunferencia_cintura < 30 or circunferencia_cintura > 150:
            st.sidebar.error('Por favor, ingresa una circunferencia de cintura válida entre 30 y 150 cm.')
    except ValueError:
        st.sidebar.error('Por favor, ingresa un número válido para la circunferencia de cintura.')

    circunferencia_cadera_str = st.sidebar.text_input('Circunferencia de cadera (en cm)', value='30')
    try:
        circunferencia_cadera = int(circunferencia_cadera_str)
        if circunferencia_cadera < 30 or circunferencia_cadera > 150:
            st.sidebar.error('Por favor, ingresa una circunferencia de cadera válida entre 30 y 150 cm.')
    except ValueError:
        st.sidebar.error('Por favor, ingresa un número válido para la circunferencia de cadera.')

#Estilo de vida saludable =                              
    st.sidebar.subheader('Estilo de Vida')
    consumo_agua_diario = st.sidebar.number_input('¿Cuánta agua consumes al día? (L)', min_value=0.5, max_value=2.0, step=0.5)
    consumo_frutas_verduras = st.sidebar.number_input('¿Cuántas porciones de frutas y verduras comes diariamente? (1 porción es aprox. 150 g)', min_value=0, max_value=10, step=1)
    horas_sueño_noche = st.sidebar.number_input('¿Cuánto tiempo sueles dormir por noche?', min_value=0, max_value=12, step=1)
    nivel_actividad_fisica = st.sidebar.selectbox('¿Cómo describirías tu nivel de actividad física?', ['Principalmente inactivo (poco o ningún ejercicio, trabajo de oficina)',
                                                                                                       'Ligeramente activo (ejercicio ligero 1-3 días/semana)',
                                                                                                       'Moderadamente activo (ejercicio moderado 3-5 días/semana)',
                                                                                                       'Muy activo (ejercicio duro 6-7 días a la semana)'])
    habitos_alimenticios = st.sidebar.selectbox("¿Qué tipo de dieta llevas?", ['Vegetariana', 'Omnívora', 'Vegana', 'Pescetariana', 'Keto', 'Paleo'])

# Hábitos Nocivos
    st.sidebar.subheader('Habitos Nocivos')
    consumo_alcohol = st.sidebar.checkbox('¿Consumes alcohol?')
    consumo_tabaco = st.sidebar.checkbox('¿Consumes productos de tabaco (como cigarrillos, puros/habanos, pipa, tabaco de mascar, vapeadores, etc.)?')
    consumo_cafeina = st.sidebar.checkbox('¿Consumes productos con cafeína (como café, té, bebidas energéticas, etc.)?')
    
    if consumo_alcohol or consumo_tabaco or consumo_cafeina:
        st.subheader('Hábitos Nocivos')

    if consumo_alcohol:
        consumo_alcohol_opcion = st.selectbox('Nivel de consumo de alcohol', ['Hasta 2 cervezas, 1 copa de vino o 1 trago de licor fuerte a la semana', 
                                                                          'Hasta 5 cervezas, 3 copas de vino o 3 tragos de licor fuerte a la semana', 
                                                                          'Hasta 8 cervezas, 4 copas de vino o 4 tragos de licor fuerte a la semana', 
                                                                          'Más de 8 cervezas o 4 copas de vino o 4 tragos de licor a la semana'])
        if consumo_alcohol_opcion == 'Hasta 2 cervezas, 1 copa de vino o 1 trago de licor fuerte a la semana':
            consumo_alcohol = 2
        elif consumo_alcohol_opcion == 'Hasta 5 cervezas, 3 copas de vino o 3 tragos de licor fuerte a la semana':
            consumo_alcohol = 5
        elif consumo_alcohol_opcion == 'Hasta 8 cervezas, 4 copas de vino o 4 tragos de licor fuerte a la semana':
            consumo_alcohol = 8
        else: # 'Más de 8 cervezas o 4 copas de vino o 4 tragos de licor a la semana'
            consumo_alcohol = 11 
    
    if consumo_tabaco:
        consumo_tabaco_opcion = st.selectbox('Nivel de consumo de Tabaco', ['Hasta 3 cigarrillos por día, o su equivalente en otros productos', 
                                                                            'Hasta 5 cigarrillos por día, o su equivalente en otros productos', 
                                                                            'Hasta 7 cigarrillos por día, o su equivalente en otros productos', 
                                                                            '9 o más cigarrillos por día o su equivalente en otros productos'])
        if consumo_tabaco_opcion == 'Hasta 3 cigarrillos por día, o su equivalente en otros productos':
            consumo_tabaco = 3
        elif consumo_tabaco_opcion == 'Hasta 5 cigarrillos por día, o su equivalente en otros productos':
            consumo_tabaco = 5
        elif consumo_tabaco_opcion == 'Hasta 7 cigarrillos por día, o su equivalente en otros productos':
            consumo_tabaco = 7
        else:  # 'Hasta 9 cigarrillos por día, o su equivalente en otros productos'
            consumo_tabaco = 9
    
    if consumo_cafeina:
        consumo_cafeina_opcion = st.selectbox('Nivel de consumo de Cafeína', ['1 a 2 tazas de café por día, o equivalente en otros productos con cafeína', 
                                                                              '2 a 3 tazas de café por día, o equivalente en otros productos con cafeína', 
                                                                              '3 a 4 tazas de café por día, o equivalente en otros productos con cafeína',
                                                                              'Más de 4 tazas de café por día, o equivalente en otros productos con cafeína'])
        if consumo_cafeina_opcion == '1 a 2 tazas de café por día, o equivalente en otros productos con cafeína':
            consumo_cafeina = 100
        elif consumo_cafeina_opcion == '2 a 3 tazas de café por día, o equivalente en otros productos con cafeína':
            consumo_cafeina = 200
        elif consumo_cafeina_opcion == '3 a 4 tazas de café por día, o equivalente en otros productos con cafeína':
            consumo_cafeina = 300
        else: # 'Más de 4 tazas de café por día, o equivalente en otros productos con cafeína'
            consumo_cafeina = 400 

    nivel_estres_percibido = st.sidebar.number_input('En una escala del 1 al 10, ¿cómo calificaría su nivel de estrés habitual, siendo 1 muy poco estrés y 10 extremadamente estresado?', min_value=1, max_value=10, step=1)                         

    #Indicadores Sanguíneos
    st.sidebar.subheader('Indicadores Sanguíneos (Opcional)')
    if st.sidebar.checkbox('Tengo datos de indicadores sanguíneos'):
        st.markdown('### Niveles de Colesterol')
        hdl_str = st.text_input('HDL (mg/dL)', value='0.1')
        try:
            hdl = float(hdl_str)
            if hdl < 0.1 or hdl > 300.0:
                st.error('Por favor, ingresa un valor válido para HDL entre 0.1 y 300.0 mg/dL.')
        except ValueError:
            st.error('Por favor, ingresa un número válido para HDL.')

        ldl_str = st.text_input('LDL (mg/dL)', value='0.1')
        try:
            ldl = float(ldl_str)
            if ldl < 0.1 or ldl > 300.0:
                st.error('Por favor, ingresa un valor válido para LDL entre 0.1 y 300.0 mg/dL.')
        except ValueError:
            st.error('Por favor, ingresa un número válido para LDL.')

        trigliceridos_str = st.text_input('Triglicéridos (mg/dL)', value='0.1')
        try:
            trigliceridos = float(trigliceridos_str)
            if trigliceridos < 0.1 or trigliceridos > 600.0:
                st.error('Por favor, ingresa un valor válido para los triglicéridos entre 0.1 y 600.0 mg/dL.')
        except ValueError:
            st.error('Por favor, ingresa un número válido para los triglicéridos.')
        
        st.markdown('### Glucosa en Sangre')
        ayunas_str = st.text_input('En ayunas (mg/dL)', value='0.1')
        try:
            ayunas = float(ayunas_str)
            if ayunas < 0.1 or ayunas > 300.0:
                st.error('Por favor, ingresa un valor válido para la glucosa en sangre en ayunas entre 0.1 y 300.0 mg/dL.')
        except ValueError:
            st.error('Por favor, ingresa un número válido para la glucosa en sangre en ayunas.')

        postprandial_str = st.text_input('Después de comer (mg/dL)', value='0.1')
        try:
            postprandial = float(postprandial_str)
            if postprandial < 0.1 or postprandial > 300.0:
                st.error('Por favor, ingresa un valor válido para la glucosa en sangre postcomida entre 0.1 y 30000.0 mg/dL.')
        except ValueError:
            st.error('Por favor, ingresa un número válido para la glucosa en sangre postcomida.')

    # Predecir la enfermedad si se ingresan todos los datos
    if st.sidebar.button('Predecir Enfermedad'):
        # Verificar si se han ingresado todos los datos necesarios
        if (edad is not None and peso is not None and altura is not None and imc is not None and circunferencia_cintura is not None and circunferencia_cadera is not None and 
            consumo_agua_diario is not None and consumo_frutas_verduras is not None and horas_sueño_noche is not None and nivel_actividad_fisica is not None and 
            habitos_alimenticios is not None and consumo_alcohol is not None and consumo_tabaco is not None and consumo_cafeina is not None and
            nivel_estres_percibido is not None):
        
        # Convertir el nivel de actividad física en una codificación one-hot
            actividad_fisica_encoded = np.zeros(4) # 4 categorías: 'Sedentario', 'Ligero', 'Moderado', 'Intenso'
            actividad_fisica_encoded[['Principalmente inactivo (poco o ningún ejercicio, trabajo de oficina)','Ligeramente activo (ejercicio ligero 1-3 días/semana)',
                                      'Moderadamente activo (ejercicio moderado 3-5 días/semana)', 'Muy activo (ejercicio duro 6-7 días a la semana)'].index(nivel_actividad_fisica)] = 1

        # Convertir los hábitos alimenticios en una codificación one-hot
            habitos_alimenticios_encoded = np.zeros(6)  # 6 categorías: 'Vegetariana', 'Omnívora', 'Vegana', 'Pescetariana', 'Keto', 'Paleo' 
            habitos_alimenticios_encoded[['Vegetariana', 'Omnívora', 'Vegana', 'Pescetariana', 'Keto', 'Paleo'].index(habitos_alimenticios)] = 1

        # Preparar los datos para la predicción
            input_data = pd.DataFrame({
                'IMC': [imc],
                'Edad': [edad],
                'Altura': [altura],
                'Peso': [peso],
                'Circunferencia de cintura': [circunferencia_cintura],
                'Circunferencia de cadera': [circunferencia_cadera],
                'Consumo de agua diario': [consumo_agua_diario],
                'Consumo de alcohol': [consumo_alcohol],
                'Consumo de tabaco': [consumo_tabaco],
                'Consumo de cafeína': [consumo_cafeina],
                'Consumo de frutas y verduras': [consumo_frutas_verduras],
                'Horas de sueño por noche': [horas_sueño_noche],
                'Niveles de colesterol (LDL)': [ldl],
                'Niveles de colesterol (HDL)': [hdl],
                'Niveles de colesterol (Triglicéridos)': [trigliceridos],
                'Niveles de glucosa en sangre (Ayunas)': [ayunas],
                'Niveles de glucosa en sangre (Postprandial)': [postprandial],
                'Nivel de estrés percibido': [nivel_estres_percibido],
                'Nivel de actividad física_Intenso': [actividad_fisica_encoded[3]],
                'Nivel de actividad física_Ligero': [actividad_fisica_encoded[1]],
                'Nivel de actividad física_Moderado': [actividad_fisica_encoded[2]],
                'Nivel de actividad física_Sedentario': [actividad_fisica_encoded[0]],
                'Hábitos alimenticios_Keto': [habitos_alimenticios_encoded[4]],
                'Hábitos alimenticios_Omnívora': [habitos_alimenticios_encoded[1]],
                'Hábitos alimenticios_Paleo': [habitos_alimenticios_encoded[5]],
                'Hábitos alimenticios_Pescetariana': [habitos_alimenticios_encoded[3]],
                'Hábitos alimenticios_Vegana': [habitos_alimenticios_encoded[2]],
                'Hábitos alimenticios_Vegetariana': [habitos_alimenticios_encoded[0]],
            })

            # Calcular el ICC
            if circunferencia_cintura and circunferencia_cadera:
                icc = circunferencia_cintura / circunferencia_cadera
                # Determinar el nivel de riesgo basado en el valor del ICC y el sexo
                if sexo == 'Hombre':
                    if icc <= 0.78:
                        color = 'yellow'
                        nivel_riesgo = 'Sindrome Ginecoide: mayor riesgo de que el paciente sufra problemas en las piernas, como varices, hinchazón, problemas circulatorios y cansancio excesivo.\
                        Los órganos que se ven más afectados son los riñones, el útero y la vejiga.'
                    elif icc >= 0.93:
                        color = 'red'
                        nivel_riesgo = 'Sindrome Androide: Mayor riesgo de padecer enfermedades coronarias, colesterol alto y problemas del corazón, pulmones, el hígado y los riñones por acumulación\
                        de gasa en la parte superior del cuerpo. La probabilidad de sufrir diabetes también es mayor.'
                    else:
                        color = 'green'
                        nivel_riesgo = 'Normal (Sin Riesgo)'
                else:  # Mujer
                    if icc <= 0.75:
                        color = 'yellow'
                        nivel_riesgo = 'Sindrome Ginecoide: mayor riesgo de que el paciente sufra problemas en las piernas, como varices, hinchazón, problemas circulatorios y cansancio excesivo.\
                        Los órganos que se ven más afectados son los riñones, el útero y la vejiga.'
                    elif icc >= 0.84:
                        color = 'red'
                        nivel_riesgo = 'Sindrome Androide: Mayor riesgo de padecer enfermedades coronarias, colesterol alto y problemas del corazón, pulmones, el hígado y los riñones por acumulación\
                        de gasa en la parte superior del cuerpo. La probabilidad de sufrir diabetes también es mayor.'
                    else:
                        color = 'green'
                        nivel_riesgo = 'Normal (Sin Riesgo)'
                # Mostrar el ICC con el color correspondiente
                st.markdown(f'<p style="font-size:20px;">Tu Índice de Cintura-Cadera es <span style="color:{color};">{icc:.2f} ({nivel_riesgo})</span></p>', unsafe_allow_html=True)
                
        # Realizar la predicción con cada uno de los modelos
        enfermedad_pred_diabetes = model_diabetes.predict(input_data)
        enfermedad_pred_hipertension = model_hipertension.predict(input_data)
        enfermedad_pred_ecv = model_cardio.predict(input_data)
        enfermedad_pred_cancer = model_multi.predict(input_data)
        enfermedad_pred_pulmonar = model_multi.predict(input_data)
        enfermedad_pred_renal = model_multi.predict(input_data)

        #Mostrar el resultado de la predicción
        st.success(f'La predicción de Diabetes es: {"Riesgo Alto" if enfermedad_pred_diabetes[0] == 1 else "Bajo Riesgo"}')
        st.success(f'La predicción de Hipertensión es: {"Riesgo Alto" if enfermedad_pred_hipertension[0] == 1 else "Bajo Riesgo"}')
        st.success(f'La predicción de Enfermedad Cardiovascular es: {"Riesgo Alto" if enfermedad_pred_ecv[0] == 1 else "Bajo Riesgo"}')
        st.success(f'La predicción de desarrollar Cáncer es: {"Riesgo Alto" if any (enfermedad_pred_cancer[0] == 1) else "Bajo Riesgo"}')
        st.success(f'La predicción de desarrollar Enfermedad Pulmonar Crónica es: {"Riesgo Alto" if any (enfermedad_pred_pulmonar[0] == 1) else "Bajo Riesgo"}')
        st.success(f'La predicción de desarrollar Enfermedad Renal Crónica es: {"Riesgo Alto" if any (enfermedad_pred_renal[0] == 1) else "Bajo Riesgo"}')
    else:
        # Mostrar un mensaje de error si no se han ingresado todos los datos necesarios
        st.sidebar.error('Por favor, complete todos los campos.')

# Ejecutar la aplicación
if __name__ == '__main__':
    main()