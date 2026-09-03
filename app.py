import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 1. Configuración de la página y Estética Visual
st.set_page_config(page_title="Desafío Inversionista", page_icon="🏆", layout="centered")

# Estilos personalizados mejorados
# Estilos personalizados: Tema "Dashboard Empresarial"
st.markdown("""
    <style>
    /* 1. Fondo principal: Degradado muy sutil y elegante (Gris/Azul claro) */
    .stApp {
        background: linear-gradient(to bottom right, #f8fafc, #e2e8f0);
    }
    
    /* 2. Panel lateral (Sidebar): Blanco puro con sombra para separarlo del fondo */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        box-shadow: 4px 0 15px rgba(0,0,0,0.03);
    }
    
    /* 3. Título principal con tipografía corporativa más sobria */
    h1 { 
        color: #0f172a; 
        text-align: center; 
        font-weight: 800; 
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        letter-spacing: -0.5px;
    }
    
    /* 4. Subtítulos y textos generales más elegantes */
    h3 { color: #1e293b !important; }
    p { color: #475569; }
    
    /* 5. Tarjetas estilo Widget Financiero: Blancas, con sombras suaves y bordes de colores institucionales */
    .card-tec { background-color: #ffffff; padding: 22px; border-radius: 8px; border-left: 6px solid #2563eb; margin-bottom: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.05), 0 1px 3px rgba(0,0,0,0.1); }
    .card-dpf { background-color: #ffffff; padding: 22px; border-radius: 8px; border-left: 6px solid #16a34a; margin-bottom: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.05), 0 1px 3px rgba(0,0,0,0.1); }
    .card-div { background-color: #ffffff; padding: 22px; border-radius: 8px; border-left: 6px solid #d97706; margin-bottom: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.05), 0 1px 3px rgba(0,0,0,0.1); }
    
    /* 6. Mejorar la apariencia de los Radio buttons (Opciones de inversión) */
    .stRadio > label { font-weight: 600; font-size: 16px; color: #0f172a; }
    
    /* 7. Mejorar el bloque de Métricas (Resultados finales) para que parezcan botones financieros */
    [data-testid="stMetricValue"] {
        color: #0f172a;
        font-weight: bold;
       
    }
    </style>
""", unsafe_allow_html=True)
st.title("🏆 ¡El Gran Juego del Dinero!")
st.markdown("<p style='text-align: center; font-size: 18px; color: #4B5563;'>Conviértete en Ingeniero Financiero. Toma decisiones estratégicas y descubre tu futuro económico.</p>", unsafe_allow_html=True)
st.divider()

# 2. Configuración Inicial del Participante en un Expander para limpieza visual
with st.sidebar:
    st.header("🚀 Tu Punto de Partida")
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135673.png", width=100) # Ícono decorativo
    capital_inicial = st.number_input("💰 Capital Inicial (Bs)", min_value=100, value=50000, step=1000, help="El dinero con el que empiezas el juego.")
    meses = st.slider("📅 Horizonte de Inversión (Meses)", min_value=1, max_value=60, value=12, help="¿Por cuánto tiempo dejarás tu dinero invertido?")

# 3. Selección Exclusiva de Opción
st.subheader("🎯 Elige tu Estrategia de Inversión")
opcion_elegida = st.radio(
    "Selecciona un camino para simular tu futuro:",
    ["A: Acciones Tecnológicas 🚀 (Alto Riesgo)", "B: Plazo Fijo en Banco 🏦 (Cero Riesgo)", "C: Portafolio Diversificado ⚖️ (Riesgo Moderado)"],
    index=0,
    horizontal=False
)

st.divider()
st.markdown("### ⚙️ Sala de Control del Mercado")

# Variables iniciales para el motor
historial = [capital_inicial]
color_grafico = "#000000"
nombre_columna = "Patrimonio"

# 4. Lógica y Entorno según la selección
if "A:" in opcion_elegida:
    st.markdown('<div class="card-tec"><h3>💥 Modo: Alta Volatilidad (Acciones Tec)</h3><p>Inviertes en startups y tecnología. El potencial de ganancia es brutal, pero el riesgo de perder gran parte de tu dinero es muy real.</p></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        rendimiento_a = st.number_input("📈 Retorno Mes Bueno (%)", value=20.0, step=1.0) / 100
    with col2:
        perdida_a = st.number_input("📉 Caída Mes Malo (%)", value=15.0, step=1.0) / 100
    with col3:
        riesgo_a = st.slider("⚠️ Probabilidad de Caída", min_value=0, max_value=100, value=40, format="%d%%") / 100

    # Motor de cálculo
    for m in range(1, meses + 1):
        if np.random.rand() <= riesgo_a:
            historial.append(historial[-1] * (1 - perdida_a))
        else:
            historial.append(historial[-1] * (1 + rendimiento_a))
            
    color_grafico = "#0284C7"
    nombre_columna = "Acciones Tecnológicas"

elif "B:" in opcion_elegida:
    st.markdown('<div class="card-dpf"><h3>🏦 Modo: Ultra-Conservador (Plazo Fijo)</h3><p>Tu dinero está en una bóveda bancaria. Crece lento, pero seguro.</p></div>', unsafe_allow_html=True)
    
    rendimiento_b = st.slider("📈 Tasa de Interés Mensual Fija (%)", min_value=0.1, max_value=2.0, value=0.4, step=0.1, help="En la vida real, los bancos dan rendimientos anuales, aquí lo vemos mensualizado.") / 100
    inflacion = st.slider("🔥 Inflación Mensual Estimada (%)", min_value=0.0, max_value=2.0, value=0.2, step=0.1) / 100
    
    if rendimiento_b <= inflacion:
        st.warning("⚠️ Cuidado: Tu rendimiento es menor o igual a la inflación. Estás perdiendo poder adquisitivo real.")

    # Motor de cálculo
    for m in range(1, meses + 1):
        historial.append(historial[-1] * (1 + rendimiento_b))
        
    color_grafico = "#16A34A"
    nombre_columna = "Depósito a Plazo Fijo"

else:
    st.markdown('<div class="card-div"><h3>⚖️ Modo: Ingeniero Financiero (Diversificado)</h3><p>40% Bienes Raíces, 40% Acciones y 20% Renta Fija. Tienes un crecimiento constante con pequeños sustos del mercado.</p></div>', unsafe_allow_html=True)
    
    rendimiento_c = st.slider("📈 Rendimiento Esperado Mensual (%)", min_value=1.0, max_value=10.0, value=3.0, step=0.5) / 100
    volatilidad = st.slider("🎢 Nivel de Volatilidad (Ruido del mercado)", min_value=1.0, max_value=5.0, value=2.0, step=0.5) / 100

    # Motor de cálculo (Rendimiento base + un factor de ruido aleatorio normal)
    for m in range(1, meses + 1):
        ruido = np.random.normal(0, volatilidad)
        retorno_real = rendimiento_c + ruido
        historial.append(historial[-1] * (1 + retorno_real))
        
    color_grafico = "#CA8A04"
    nombre_columna = "Portafolio Diversificado"

# 5. Renderizado de Gráficos Interactivos (Plotly)
st.divider()
st.subheader("📊 Simulación de tu Patrimonio en el Tiempo")

# Preparar DataFrame
df_simulado = pd.DataFrame({
    "Mes": list(range(meses + 1)), 
    "Capital (Bs)": historial
})

# Crear gráfico interactivo
fig = px.area(
    df_simulado, 
    x="Mes", 
    y="Capital (Bs)", 
    markers=True,
    color_discrete_sequence=[color_grafico],
    title=f"Evolución de Inversión: {nombre_columna}"
)
fig.update_layout(xaxis_title="Meses Transcurridos", yaxis_title="Dinero Acumulado (Bs)", hovermode="x unified")
st.plotly_chart(fig, use_container_width=True)

# 6. Tablero de Resultados Finales
st.markdown("### 🏆 Resultado de tu Decisión")
patrimonio_final = historial[-1]
ganancia_neta = patrimonio_final - capital_inicial
porcentaje_retorno = (ganancia_neta / capital_inicial) * 100

col_res1, col_res2, col_res3 = st.columns(3)
with col_res1:
    st.metric(label="Capital Inicial", value=f"Bs {capital_inicial:,.2f}")
with col_res2:
    st.metric(label="Patrimonio Final", value=f"Bs {patrimonio_final:,.2f}", delta=f"{porcentaje_retorno:.2f}%")
with col_res3:
    st.metric(label="Ganancia/Pérdida Neta", value=f"Bs {ganancia_neta:,.2f}", delta=float(ganancia_neta))

# Feedback dinámico
if ganancia_neta > (capital_inicial * 0.5):
    st.success("🌟 ¡Increíble! Eres un genio de las finanzas. Has hecho crecer tu patrimonio de forma masiva.")
    st.balloons()
elif ganancia_neta > 0:
    st.info("👍 Buen trabajo. Lograste vencer al tiempo y sumar ganancias.")
else:
    st.error("🚨 ¡Bancarrota técnica o pérdidas graves! El mercado te ha dado una dura lección.")

# 7. Botón de Re-simulación
# 7. Botón de Re-simulación con Feedback Visual
st.markdown("<br>", unsafe_allow_html=True)
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])

with col_btn2:
    if st.button("🎲 El mercado es incierto: ¡Volver a Simular!", use_container_width=True):
        import time
        # Muestra un mensaje de carga temporal para que el usuario note el click
        with st.spinner("Lanzando los dados del mercado... 🎲"):
            time.sleep(2) # Pausa de medio segundo para el suspenso
        
        st.rerun() # Reinicia la aplicación con los nuevos números