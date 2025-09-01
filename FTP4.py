import streamlit as st
import folium
from streamlit_folium import st_folium

# ================= UI CONFIG =================
st.set_page_config(page_title="Flight Tracker", layout="wide")

# ================= THEMING & ACCESSIBILITY =================
st.sidebar.title("Ustawienia dostępności")

# Tryb jasny/ciemny
mode = st.sidebar.radio("Motyw interfejsu", ("Jasny", "Ciemny"))

# Powiększenie tekstu
text_size = st.sidebar.slider("Rozmiar tekstu", 12, 32, 16)

# Wysoki kontrast
high_contrast = st.sidebar.checkbox("Włącz wysoki kontrast")

# Narrator (symulacja)
narrator = st.sidebar.checkbox("Włącz narratora (symulacja)")

# Instrukcja dla użytkownika
st.sidebar.info("ℹ️ Możesz też zmienić motyw mapy bezpośrednio w folium (tiles=...) – np. 'CartoDB dark_matter' dla trybu ciemnego.")

# ================= STYLE HANDLING =================
background_color = "#ffffff" if mode == "Jasny" else "#0e1117"
text_color = "#000000" if mode == "Jasny" else "#ffffff"
if high_contrast:
    background_color = "#000000"
    text_color = "#ffff00"

custom_style = f"""
<style>
body {{
    background-color: {background_color};
    color: {text_color};
}}
.custom-text {{
    font-size: {text_size}px !important;
    color: {text_color} !important;
}}
</style>
"""

st.markdown(custom_style, unsafe_allow_html=True)

# ================= APP HEADER =================
st.markdown("<div class='custom-text'><h1>✈️ Flight Tracker UI Prototype</h1></div>", unsafe_allow_html=True)

if narrator:
    st.success("Narrator: aplikacja jest aktywna. Dane lotu zostaną odczytane.")

# ================= MOCK DATA =================
st.markdown("<div class='custom-text'><b>Numer lotu:</b> AMQ733</div>", unsafe_allow_html=True)
st.markdown("<div class='custom-text'><b>Samolot:</b> Airbus A321-111</div>", unsafe_allow_html=True)
st.markdown("<div class='custom-text'><b>Przewoźnik:</b> Air 001</div>", unsafe_allow_html=True)
st.markdown("<div class='custom-text'><b>Status:</b> Przewidywany odlot 02:20</div>", unsafe_allow_html=True)

# ================= IMAGES =================
st.subheader("Zdjęcia samolotu")
st.image("images/a321_plane.jpg", caption="Airbus A321-111 (Air001)", use_column_width=True)
st.image("images/a321_cabin.jpg", caption="Układ kabiny – Airbus A321", use_column_width=True)

# ================= MAP =================
st.subheader("Mapa trasy")
tile_style = "OpenStreetMap" if mode == "Jasny" else "CartoDB dark_matter"
fmap = folium.Map(location=[34, -110], zoom_start=3, tiles=tile_style)
folium.Marker(location=[35, -90], tooltip="Chania (CHQ)").add_to(fmap)
folium.Marker(location=[50, 19], tooltip="Katowice (KTW)").add_to(fmap)
st_folium(fmap, width=700, height=450)
