import streamlit as st
import folium
from streamlit_folium import st_folium


# ================= UI CONFIG =================
st.set_page_config(page_title="Flight Tracker", layout="wide")


# ================= THEMING OPTIONS =================
st.sidebar.title("Ustawienia dostępności")


# Tryb jasny/ciemny
mode = st.sidebar.radio("Motyw interfejsu", ("Jasny", "Ciemny"))


# Powiększenie tekstu
text_size = st.sidebar.slider("Rozmiar tekstu", 12, 32, 16)


# Wysoki kontrast
high_contrast = st.sidebar.checkbox("Włącz wysoki kontrast")


# Narrator (symulacja)
narrator = st.sidebar.checkbox("Włącz narratora (symulacja)")


# ================= STYLE HANDLING =================
background_color = "#ffffff" if mode == "Jasny" else "#0e1117"
text_color = "#000000" if mode == "Jasny" else "#ffffff"

custom_style = f"""
<style>
body {{
background-color: {background_color};
color: {text_color};
font-size: {text_size}px;
}}
</style>
"""
st.markdown(custom_style, unsafe_allow_html=True)


# ================= APP HEADER =================
st.title("✈️ Flight Tracker UI Prototype")
st.write("Tryb dostępności: narrator = {}".format("ON" if narrator else "OFF"))


# ================= MOCK DATA =================
st.subheader("Lot przykładowy")
st.write("**Numer lotu:** AMQ733")
st.write("**Samolot:** Airbus A321-111")
st.write("**Przewoźnik:** Air 001")
st.write("**Status:** Przewidywany odlot 02:20")


# ================= IMAGES =================
st.image("images/a321_plane.jpg", caption="Airbus A321-111 (Air001)", use_column_width=True)
st.image("images/a321_cabin.jpg", caption="Układ kabiny – Airbus A321", use_column_width=True)


# ================= MAP =================
st.subheader("Mapa trasy")
fmap = folium.Map(location=[34, -110], zoom_start=3)
folium.Marker(location=[35, -90], tooltip="Chania (CHQ)").add_to(fmap)
folium.Marker(location=[50, 19], tooltip="Katowice (KTW)").add_to(fmap)
st_folium(fmap, width=700, height=450)