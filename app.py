import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Conversor de Temperaturas", page_icon="🌡️")

def convertir_temperatura(valor, origen, destino):
    """
    Función que realiza las conversiones matemáticas entre unidades de temperatura.
    """
    if origen == destino:
        return valor
    
    # Desde Celsius
    if origen == "Celsius":
        if destino == "Fahrenheit":
            return (valor * 9/5) + 32
        elif destino == "Kelvin":
            return valor + 273.15
            
    # Desde Fahrenheit
    elif origen == "Fahrenheit":
        if destino == "Celsius":
            return (valor - 32) * 5/9
        elif destino == "Kelvin":
            return (valor - 32) * 5/9 + 273.15
            
    # Desde Kelvin
    elif origen == "Kelvin":
        if destino == "Celsius":
            return valor - 273.15
        elif destino == "Fahrenheit":
            return (valor - 273.15) * 9/5 + 32

# Interfaz de usuario con Streamlit
st.title("🌡️ Conversor de Temperaturas")
st.write("Ingresa un valor y selecciona las unidades para realizar la conversión.")

# Entrada del valor numérico
valor_input = st.number_input("Valor de la temperatura:", value=0.0, format="%.2f")

# Columnas para organizar los selectores
col1, col2 = st.columns(2)

unidades = ["Celsius", "Fahrenheit", "Kelvin"]

with col1:
    unidad_origen = st.selectbox("Convertir de:", unidades)

with col2:
    unidad_destino = st.selectbox("Convertir a:", unidades)

# Botón para ejecutar la conversión
if st.button("Convertir", type="primary"):
    # Validación simple de cero absoluto
    if unidad_origen == "Kelvin" and valor_input < 0:
        st.error("Error: La temperatura en Kelvin no puede ser menor a 0 (Cero Absoluto).")
    elif unidad_origen == "Celsius" and valor_input < -273.15:
        st.error("Error: La temperatura no puede ser menor al cero absoluto (-273.15 °C).")
    elif unidad_origen == "Fahrenheit" and valor_input < -459.67:
        st.error("Error: La temperatura no puede ser menor al cero absoluto (-459.67 °F).")
    else:
        # Calcular resultado
        resultado = convertir_temperatura(valor_input, unidad_origen, unidad_destino)
        
        # Mostrar el resultado con un diseño agradable
        st.success(f"**Resultado:** {valor_input} {unidad_origen} equivale a **{resultado:.2f} {unidad_destino}**")