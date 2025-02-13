import streamlit as st

# Configurar el título de la aplicación
st.title("📊 Calculadora de Inversión Publicitaria")

# Sectores, plataformas y tipos de campaña disponibles
sectores = ["Ecommerce", "Turismo", "Inmobiliario"]
plataformas = ["Meta", "Google Ads", "TikTok"]
tipos_campaña = ["Conversión", "Tráfico", "Alcance"]

# Diccionario con métricas según sector, plataforma y tipo de campaña
metricas = {
    "Ecommerce": {
        "Meta": {"Conversión": {"CTR": 1.5, "CPC": 0.50, "Tasa Conversión": 2.5},
                 "Tráfico": {"CTR": 2.0, "CPC": 0.40, "CPM": 3.00, "Tasa Conversión": 1.5},
                 "Alcance": {"CTR": 0.8, "CPM": 1.50}},
        "Google Ads": {"Conversión": {"CTR": 3.0, "CPC": 0.80, "Tasa Conversión": 3.0},
                       "Tráfico": {"CTR": 3.5, "CPC": 0.70, "CPM": 5.00, "Tasa Conversión": 2.0},
                       "Alcance": {"CTR": 1.5, "CPM": 2.00}},
    },
    "Turismo": {
        "Meta": {"Conversión": {"CTR": 1.2, "CPC": 0.60, "Tasa Conversión": 1.8},
                 "Tráfico": {"CTR": 1.8, "CPC": 0.50, "CPM": 4.00, "Tasa Conversión": 1.2},
                 "Alcance": {"CTR": 0.7, "CPM": 2.50}},
        "TikTok": {"Conversión": {"CTR": 0.9, "CPC": 0.50, "Tasa Conversión": 1.5},
                   "Tráfico": {"CTR": 1.2, "CPC": 0.40, "CPM": 3.50, "Tasa Conversión": 1.0},
                   "Alcance": {"CTR": 0.5, "CPM": 2.00}},
    }
}

# Crear selectores en la app
sector = st.selectbox("Seleccione el sector:", sectores)
plataforma = st.selectbox("Seleccione la plataforma:", plataformas)
tipo_campaña = st.selectbox("Seleccione el tipo de campaña:", tipos_campaña)

# Ingreso de inversión
inversion = st.number_input("Ingrese la inversión en euros (€):", min_value=10, step=10)

# Botón para calcular
if st.button("Calcular"):
    if sector in metricas and plataforma in metricas[sector] and tipo_campaña in metricas[sector][plataforma]:
        valores = metricas[sector][plataforma][tipo_campaña]
        ctr = valores.get("CTR", 0)
        cpc = valores.get("CPC", 0)
        tasa_conversion = valores.get("Tasa Conversión", 0)
        cpm = valores.get("CPM", 0)

        # Cálculos generales
        clics = (inversion / cpc) if cpc > 0 else 0
        leads = clics * (tasa_conversion / 100) if tasa_conversion > 0 else 0
        cpl = inversion / leads if leads > 0 else 0
        impresiones = (inversion / (cpm / 1000)) if cpm > 0 else 0

        # Mostrar resultados dinámicamente según el tipo de campaña
        st.subheader("📊 Resultados Estimados")
        st.write(f"**💰 Inversión:** {inversion:.2f} €")
        
        if tipo_campaña == "Conversión":
            st.write(f"**🖱 Clics generados:** {clics:.0f}")
            st.write(f"**🔄 Leads/Ventas estimadas:** {leads:.0f}")
            st.write(f"**📉 CPL (Costo por Lead):** {cpl:.2f} €")

        elif tipo_campaña == "Tráfico":
            st.write(f"**📢 Impresiones generadas:** {impresiones:.0f}")
            st.write(f"**🖱 Clics generados:** {clics:.0f}")
            st.write(f"**💰 CPM (Costo por Mil Impresiones):** {cpm:.2f} €")
            st.write(f"**📉 CPC (Costo por Clic):** {cpc:.2f} €")

        elif tipo_campaña == "Alcance":
            st.write(f"**📢 Impresiones generadas:** {impresiones:.0f}")
            st.write(f"**💰 CPM (Costo por Mil Impresiones):** {cpm:.2f} €")

    else:
        st.error("⚠️ No hay datos para la selección hecha.")

