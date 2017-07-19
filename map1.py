import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_porducer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name = "My Map")

# for lt, ln, el in zip(lat, lon, elev):
#     fg.add_child(folium.Marker(location=[lt, ln], popup = str(el) + " m", icon = folium.Icon(color=color_porducer(el))))

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+ " m", fill_color=color_porducer(el), color='grey', fill_opacity=0.7))

fg.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig'))))

map.add_child(fg)
map.save("Map1.html")