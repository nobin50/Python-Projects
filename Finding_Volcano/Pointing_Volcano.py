import folium
import pandas as pd



df = pd.read_csv('Volcanoes.txt')

latmean = df['LAT'].mean()
lonmean = df['LON'].mean()

map1 = folium.Map(location=[latmean, lonmean], zoom_start=6, tiles="Stamen Terrain")

def color(elev):
    if elev in range(0, 1000):
        col = 'green'
    elif elev in range(1001, 1999):
        col = 'blue'
    elif elev in range(2000, 2999):
        col = 'orange'
    else:
        col = 'red'
    return col

for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']) :
    folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(color=color(elev), icon_color="purple", icon="cloud")).add_to(map1)
print(map1.save('test.html'))



# print(dir(folium))
# folium.Marker(location=[40.897934, -73.885948], popup="I am so lost", icon=folium.Icon(icon="cloud")).add_to(map1)
# folium.Marker(location=[40.8895439, -73.9015249], popup="I can see you", icon=folium.Icon(color="green")).add_to(map1)