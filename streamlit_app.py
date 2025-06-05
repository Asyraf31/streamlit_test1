import streamlit as st
import pandas as pd
import datetime
import requests

st.set_page_config(page_title="Student Travel Planner", layout="centered")

# Supabase - Optional config (mocked here)
SAVE_TO_DATABASE = False  # Toggle True if Supabase is configured

# Google Maps Embed function
def show_map(destination):
    base_url = "https://www.google.com/maps/embed/v1/place"
    api_key = "YOUR_GOOGLE_MAPS_API_KEY"  # Replace with your key
    return f"{base_url}?key={api_key}&q={destination}"

# Packing list generator
def generate_packing_list(destination):
    general = ["🧥 Clothes", "🎧 Earphones", "🔌 Power bank", "🎫 Student ID"]
    beach_items = ["🩱 Swimsuit", "🧴 Sunscreen", "🕶 Sunglasses"]
    cold_items = ["🧤 Gloves", "🧣 Scarf", "🧥 Jacket"]

    if destination.lower() in ["langkawi", "penang"]:
        return general + beach_items
    elif destination.lower() in ["cameron highlands"]:
        return general + cold_items
    else:
        return general

# UI
st.title("🎒 Student Travel Planner")
st.subheader("Plan your next student adventure easily!")

destination = st.selectbox("🌍 Select Destination", ["Kuala Lumpur", "Langkawi", "Penang", "Singapore", "Cameron Highlands"])
days = st.slider("📅 Number of Days", 1, 14, 3)
start_date = st.date_input("📆 Start Date", datetime.date.today())
budget = st.number_input("💸 Enter your total budget (MYR)", value=500)

# Google Maps iframe
with st.expander("📍 Show Map"):
    if "YOUR_GOOGLE_MAPS_API_KEY" in show_map(destination):
        st.warning("<link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>

<div id="map" style="height: 400px;"></div>
<script>
  var map = L.map('map').setView([51.505, -0.09], 13);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
  }).addTo(map);
</script>
")
    else:
        st.components.v1.iframe(show_map(destination), height=400)

# Button
if st.button("✨ Generate Trip Plan"):
    daily_budget = budget / days
    end_date = start_date + datetime.timedelta(days=days - 1)

    st.success("✅ Trip Summary")
    st.write(f"📍 **Destination**: {destination}")
    st.write(f"📅 **From**: {start_date.strftime('%b %d, %Y')} to {end_date.strftime('%b %d, %Y')}")
    st.write(f"💸 **Daily Budget**: RM {daily_budget:.2f}")

    st.markdown("### 🧳 Packing List")
    for item in generate_packing_list(destination):
        st.write(f"- {item}")

    st.markdown("### 💡 Student Travel Tips")
    st.info("Use student ID for travel & museum discounts!")
    st.info("Book accommodations early for cheaper rates!")

    # Optional: Save to Supabase (mocked)
    if SAVE_TO_DATABASE:
        st.write("🛠 Saving trip to database... (Simulated)")

