import streamlit as st
import pandas as pd
import numpy as np

# 1. Configuración de la página y Estética Visual "Gamificada" (Estudiantes)
st.set_page_config(page_title="🏆 Desafío Inversionista", page_icon="💰", layout="centered")

# Estilos personalizados para colores llamativos y cajas interactivas
st.markdown("""
    <style>
    .main { background-color: #f7f9fc; }
    h1 { color: #2E4053; text-align: center; font-family: 'Comic Sans MS', sans-serif; }
    .card-tec { background-color: #EBF5FB; padding: 20px; border-radius: 15px; border-left: 8px solid #3498DB; margin-bottom: 15px; }
    .card-dpf { background-color: #EAFAF1; padding: 20px; border-radius: 15px; border-left: 8px solid #2ECC71; margin-bottom: 15px; }
    .card-div { background-color: #FEF9E7; padding: 20px; border-radius: 15px; border-left: 8px solid #F1C40F; margin-bottom: 15px; }
    .resultado-box { background-color: #2C3E50; color: white; padding: 25px; border-radius: 15px; text-align: center; font-size: 24px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("🏆 ¡El Gran Juego del Dinero!")
st.markdown("<p style='text-align: center; font-size: 18px;'>Conviértete en Ingeniero Financiero. Toma una decisión y descubre tu futuro económico.</p>", unsafe_allow_html=True)
st.markdown("---")

# 2. Configuración Inicial del Participante
st.sidebar.header("🚀 Tu Configuración Base")
capital_inicial = st.sidebar.number_input("💰 ¿Con cuánto dinero empiezas? (Bs)", min_value=100, value=50000, step=1000)
meses = st.sidebar.slider("📅 ¿Cuántos meses vas a jugar?", min_value=1, max_value=24, value=12)

# 3. Selección Exclusiva de Opción (Radio Buttons Interactivos)
st.subheader("🎯 Elige tu Camino de Inversión")
opcion_elegida = st.radio(
    "Selecciona una sola estrategia para ver su simulación:",
    ["Opción A: Acciones Tecnológicas 🚀", "Opción B: Guardar en DPF (Banco) 🏦", "Opción C: Portafolio Diversificado ⚖️"],
    index=0
)

# 4. Parámetros Modificables dinámicamente según la opción elegida
st.markdown("### ⚙️ Modificar Ajustes del Mercado (Rendimientos y Riesgos)")

# Estructuras lógicas que cambian según el botón presionado
if "Opción A" in opcion_elegida:
    st.markdown('<div class="card-tec"><h3>💥 Modo: Alta Volatilidad (Acciones Tec)</h3><p>Estás invirtiendo en empresas tecnológicas nuevas. ¡Puedes volverte millonario o perderlo todo!</p></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        rendimiento_a = st.slider("📈 Rendimiento si el mes es BUENO (%)", min_value=5, max_value=50, value=20) / 100
    with col2:
        riesgo_a = st.slider("⚠️ Probabilidad de CAÍDA en el mes (%)", min_value=10, max_value=90, value=40) / 100
    
    perdida_a = st.slider("📉 Cuánto capital pierdes si el mes es MALO (%)", min_value=10, max_value=90, value=50) / 100

    # Ejecución del Motor para la Opción A
    historial = [capital_inicial]
    for m in range(1, meses + 1):
        dado = np.random.rand()
        if dado <= riesgo_a:
            nuevo_valor = historial[-1] * (1 - perdida_a) # Ciclo alcista negativo / pérdida
        else:
            nuevo_valor = historial[-1] * (1 + rendimiento_a) # Ganancia mensual
        historial.append(nuevo_valor)
        
    color_grafico = ["#3498DB"]
    nombre_columna = "Tu Dinero en Acciones Tec"

elif "Opción B" in opcion_elegida:
    st.markdown('<div class="card-dpf"><h3>🏦 Modo: Ultra-Conservador (Plazo Fijo)</h3><p>Tu dinero está seguro en una bóveda bancaria. No hay riesgo de pérdida, pero crece muy despacio.</p></div>', unsafe_allow_html=True)
    
    rendimiento_b = st.slider("📈 Rendimiento Fijo Mensual (%)", min_value=0.1, max_value=5.0, value=0.4, step=0.1) / 100
    
    st.info("⚠️ Recordatorio para la clase: El riesgo aquí es del 0%, pero la inflación se comerá tu poder de compra en el mundo real.")

    # Ejecución del Motor para la Opción B
    historial = [capital_inicial]
    for m in range(1, meses + 1):
        nuevo_valor = historial[-1] * (1 + rendimiento_b)
        historial.append(nuevo_valor)
        
    color_grafico = ["#2ECC71"]
    nombre_columna = "Tu Dinero en el Banco (DPF)"

else:
    st.markdown('<div class="card-div"><h3>⚖️ Modo: Ingeniero Financiero (Diversificado)</h3><p>Distribuyes inteligentemente: 40% Bienes Raíces (alquileres), 40% Acciones estables y 20% Fondo de Emergencia.</p></div>', unsafe_allow_html=True)
    
    rendimiento_c = st.slider("📈 Rendimiento Combinado Seguro (%)", min_value=1.0, max_value=15.0, value=7.5, step=0.5) / 100
    
    st.success("💡 Consejo pro: Al estar diversificado, tienes un flujo de caja constante libre de sustos extremos.")

    # Ejecución del Motor para la Opción C
    historial = [capital_inicial]
    for m in range(1, meses + 1):
        nuevo_valor = historial[-1] * (1 + rendimiento_c)
        historial.append(nuevo_valor)
        
    color_grafico = ["#F1C40F"]
    nombre_columna = "Tu Dinero Diversificado"

# 5. Renderizado Exclusivo de Gráficos y Resultados de la Opción Seleccionada
st.markdown("---")
st.subheader("📊 Línea de Tiempo de tu Patrimonio")

# Crear DataFrame con el nombre específico de la opción
df_simulado = pd.DataFrame({"Mes": list(range(meses + 1)), nombre_columna: historial}).set_index("Mes")

# Mostrar solo el gráfico de la opción elegida
st.line_chart(df_simulado, color=color_grafico[0])

# Mostrar Tarjeta de Resultado Final Impactante
patrimonio_final = historial[-1]
ganancia_neta = patrimonio_final - capital_inicial

st.markdown(f"""
    <div class="resultado-box">
        💰 PATRIMONIO FINAL: Bs {patrimonio_final:,.2f}<br>
        <span style='font-size: 16px; color: #BDC3C7;'>
            Resultado neto: {'🎉 Ganaste' if ganancia_neta >= 0 else '🚨 Perdiste'} Bs {abs(ganancia_neta):,.2f}
        </span>
    </div>
""", unsafe_allow_html=True)

# Botón interactivo para repetir el escenario
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🎲 ¡Volver a lanzar el destino! (Re-simular)"):
    st.rerun()