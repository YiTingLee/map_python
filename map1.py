import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])

map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name = "My Map")

for lt,ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup = "Hi I am a Marker", icon = folium.Icon(color='blue')))

map.add_child(fg)

map.save("Map1.html")