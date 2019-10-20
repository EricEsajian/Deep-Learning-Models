#!/usr/bin/env python
# coding: utf-8

# ### Folium Introduction. First we will install the necessary libraries, then import them. We will also upload the required dataset. The goal for this lesson is to analyize the different water consumption habits of Cape Town South Africa

# In[52]:


pip install folium


# In[53]:


import folium


# In[54]:


import pandas as pd


# In[55]:


pip install xlrd


# In[79]:


df_suburbs = pd.read_excel('C:\\Users\\esaeri-1122\\waterwatch_clean2.xlsx', sheet_name = 'Sheet1')


# In[80]:


df_suburbs.head()


# In[81]:


df_suburbs.columns


# In[82]:


df_suburbs.shape


# In[83]:


df_suburbs.describe()


# In[84]:


map_osm = folium.Map(location = [-33.925, 18.625], zoom_start=10)
map_osm


# In[85]:


map_dark = folium.Map(location = [-33.925, 18.625], tiles='CartoDB dark_matter', zoom_start=10)
map_dark


# In[86]:


df_suburbs_locations = df_suburbs[['Latitude', 'Longitude']]
#df_suberbs_locations
suburbs_location_list = df_suburbs_locations.values.tolist()
suburbs_location_list_size = len(suburbs_location_list)
suburbs_location_list_size


# In[87]:


for point in range(0, suburbs_location_list_size):
    folium.Marker(suburbs_location_list[point]).add_to(map_osm)
    folium.Marker(suburbs_location_list[point]).add_to(map_dark)
    
map_osm


# In[65]:


map_dark


# In[88]:


for point in range(0, suburbs_location_list_size):
    folium.Marker(suburbs_location_list[point], popup=df_suburbs['Suburb'][point]).add_to(map_osm)
    folium.Marker(suburbs_location_list[point], popup=df_suburbs['Suburb'][point]).add_to(map_dark)
    
map_osm


# In[89]:


map_dark


# In[90]:


for point in range(0, suberbs_location_list_size):
    folium.Marker(suburbs_location_list[point], popup=df_suburbs['Suburb'][point], icon=folium.Icon(color='darkblue', icon_color='white', icon='tint', angle=0, prefix='fa')).add_to(map_osm)
    folium.Marker(suburbs_location_list[point], popup=df_suburbs['Suburb'][point], icon=folium.Icon(color='darkblue', icon_color='white', icon='tint', angle=0, prefix='fa')).add_to(map_dark)
    
map_osm


# In[91]:


map_dark = folium.Map(location=[-33.925, 18.625], tiles = 'CartoDB dark_matter', zoom_start=10)
map_dark


# In[92]:


df_suburbs_locations = df_suberbs[['Latitude', 'Longitude']]
#df_suburbs_locations - number of locations we will plot
suburbs_location_list = df_suburbs_locations.values.tolist()
suburbs_location_list_size = len(suburbs_location_list)
suburbs_location_list_size


# In[94]:


for point in range(0, suburbs_location_list_size):
    folium.Marker(suburbs_location_list[point]).add_to(map_osm)
    folium.Marker(suburbs_location_list[point]).add_to(map_dark)
    
map_osm


# In[95]:


map_dark


# In[96]:


for point in range(0, suburbs_location_list_size):
    folium.Marker(suburbs_location_list[point], popup=df_suburbs['Suburb'][point]).add_to(map_osm)
    folium.Marker(suburbs_location_list[point], popup=df_suburbs['Suburb'][point]).add_to(map_dark)

#This function allows you to click on the marker and see what suburb the point is on

map_osm


# In[97]:


map_dark


# In[101]:


# change styling of marker to a darker blue and added a little droplette to the marker

for point in range(0, suburbs_location_list_size):
    folium.Marker(suburbs_location_list[point], popup=df_suburbs['Suburb'][point], icon=folium.Icon(color='darkblue', icon_color='white', icon='tint', angle=0, prefix='fa')).add_to(map_osm)
    folium.Marker(suburbs_location_list[point], popup=df_suburbs['Suburb'][point], icon=folium.Icon(color='darkblue', icon_color='white', icon='plus', angle=0, prefix='fa')).add_to(map_dark)
    
map_osm


# In[102]:


map_dark


# In[110]:


# Classification of markers. If the suburb location used less than 5 kiloleters of water, they get a thumbsup in green. Outliers are in red
# and between 5 and 8 kiloleters are in blue with a thumbsup. At the time this data was created, Cape Town South Africa was in as serious 
# water crisis.

for point in range(0, suburbs_location_list_size):
    if df_suburbs['Oct 2017\nkl/month'][point] < 5:
        folium.Marker(suburbs_location_list[point], 
                     popup=df_suburbs['Suburb'][point], 
                     icon=folium.Icon(color='green', icon_color='w', icon='thumbs-up', angle=0, prefix='fa')).add_to(map_osm)
        folium.Marker(suburbs_location_list[point], 
                     popup=df_suburbs['Suburb'][point], 
                     icon=folium.Icon(color='green', icon_color='w', icon='thumbs-up', angle=0, prefix='fa')).add_to(map_dark)
    elif df_suburbs['Oct 2017\nkl/month'][point] > 5 and df_suburbs['Oct 2017\nkl/month'][point] <= 8:
        folium.Marker(suburbs_location_list[point], 
                     popup=df_suburbs['Suburb'][point], 
                     icon=folium.Icon(color='blue', icon_color='w', icon='thumbs-up', angle=0, prefix='fa')).add_to(map_osm)
        folium.Marker(suburbs_location_list[point], 
                     popup=df_suburbs['Suburb'][point], 
                     icon=folium.Icon(color='blue', icon_color='w', icon='thumbs-up', angle=0, prefix='fa')).add_to(map_dark)
    else:
        folium.Marker(suburbs_location_list[point], 
                     popup=df_suburbs['Suburb'][point], 
                     icon=folium.Icon(color='red', icon_color='w', icon='thumbs-down', angle=0, prefix='fa')).add_to(map_osm)
        folium.Marker(suburbs_location_list[point], 
                     popup=df_suburbs['Suburb'][point], 
                     icon=folium.Icon(color='red', icon_color='w', icon='thumbs-down', angle=0, prefix='fa')).add_to(map_dark)
        
map_osm


# In[111]:


map_dark


# In[118]:


# Look at the point of view of a radius around the point. We multiply the value by 100 to scale it visually

map_points = folium.Map(location=[-33.925, 18.625], tiles='CartoDB dark_matter', zoom_start=10)

for point in range(0, suburbs_location_list_size):
    folium.Circle(
        location=suburbs_location_list[point],
        popup=df_suburbs['Suburb'][point] + ': ' + str(df_suburbs['Oct 2017\nkl/month'][point]) + ' kL',
        radius=str(df_suburbs['Oct 2017\nkl/month'][point] * 100),
        color='17cbef',
        fill=True,
        opacity=0.8,
        fill_color='#17cbef',
        stroke=True,
        weight=1.0
    ).add_to(map_points)
        
map_points


# In[119]:


# Adding Classification - displayed the suburbs based on their kiloliters. The markers are clickable. Those that 
# consume the most water are in red. 

map_points = folium.Map(location=[-33.925, 18.625], tiles='CartoDB dark_matter', zoom_start=10)

for point in range(0, suburbs_location_list_size):
    # Classify by usage
    if df_suburbs['Oct 2017\nkl/month'][point] <= 8 and df_suburbs['Oct 2017\nkl/month'][point] > 0:
        usage_color = 'green'
    if df_suburbs['Oct 2017\nkl/month'][point] > 8 and df_suburbs['Oct 2017\nkl/month'][point] <= 10:
        usage_color = '#17cbef'
    elif df_suburbs['Oct 2017\nkl/month'][point] > 10:
        usage_color = 'red'
    else: # Outliers
        usage_color = 'orange'
        
    folium.Circle(
        location=suburbs_location_list[point],
        popup=df_suburbs['Suburb'][point] + ': ' + str(df_suburbs['Oct 2017\nkl/month'][point]) + ' kL',
        radius=str(df_suburbs['Oct 2017\nkl/month'][point] * 100),
        color=usage_color,
        fill=True,
        opacity=0.8,
        fill_color=usage_color,
        stroke=True,
        weight=1.0
    ).add_to(map_points)
    
map_points


# In[123]:


# Building a choropleth Map

df_world_countries = pd.read_json('C:\\Users\\esaeri-1122\\world-countries.json')
df_unemployment = pd.read_csv('C:\\Users\\esaeri-1122\\unemployment.csv', skiprows=4, delimiter=',')

df_world_countries


# In[124]:


df_unemployment


# In[126]:


df_unemployment_2018 = df_unemployment[['Country Name', 'Country Code', '2018']]
df_unemployment_2018.head(10)


# In[127]:


# Remove nulls

df_unemployment_2018_clean = df_unemployment_2018.dropna()
df_unemployment_2018_clean.head(10)


# In[129]:


df_unemployment_2018_clean.shape


# In[130]:


# prepare data for our map
legendTitle = 'Unemployement rate per country in 2018 %'

# Data to plot country code and value
data_unemployment = df_unemployment_2018_clean[['Country Code', '2018']]

data_unemployment.head()


# In[136]:


# Setup the Map

map_unemployment = folium.Map(location=[8.7832, 34.5085], zoom_start = 3)

map_unemployment.choropleth(geo_data='C:\\Users\\esaeri-1122\\world-countries.json',
                            data=data_unemployment,
                            columns=['Country Code', '2018'],
                            key_on='feature.id',
                            fill_color='YlGn',
                            fill_opacity='0.7',
                            line_opacity='0.2',
                            legend_name=legendTitle)

map_unemployment


# In[137]:


# Measuring Boundaries

df_damLevels = pd.read_csv('https://raw.githubusercontent.com/EBISYS/Mapping-Dam-Levels/master/DamLevels.txt', delimiter=',')

df_damLevels.head()


# In[138]:


df_location = pd.read_csv('https://raw.githubusercontent.com/EBISYS/Mapping-Dam-Levels/master/damLocations.txt', delimiter=',')

df_location.head()


# In[139]:


# Now we join the two dataframes to index Dam

df_damData = pd.merge(df_damLevels, df_location, on='Dam', how='left')

df_damData.head()


# In[140]:


# Prepare data to plot and display GPS coordinates for each dam

df_dams_locations = df_damData[['Latitude', 'Longitude']]
dams_location_list = df_dams_locations.values.tolist()
dams_location_list_size = len(dams_location_list)
dams_location_list


# In[141]:


# We will iterate 6 times:

dams_location_list_size


# In[142]:


map_dams = folium.Map(location=[-33.925, 18.625], zoom_start=10)
for point in range(0, dams_location_list_size):
    folium.Marker(dams_location_list[point], popup=df_damData['Dam'][point]).add_to(map_dams)
    
map_dams


# In[145]:


# Plot markers on our new map

map_url = folium.Map(location=[-34.078100, 19.289200],
                    tiles='http://services.arcgisonline.com/arcgis/rest/services/world_imagery/mapserver/tile/{z}/{y}/{x}',
                    zoom_start=12,
                    attr='TIles & copy,etc.')

for point in range(0, dams_location_list_size):
    folium.Marker(dams_location_list[point], popup=df_damData['Dam'][point]).add_to(map_url)

map_url


# In[146]:


# Now add a measure control to measure the boundries of the dams. We can measure the area of a surface and 
# keep it within the marker popup

from folium.plugins import MeasureControl

map_url.add_child(MeasureControl())

map_url


# In[156]:


# Add Layer Control

map_layers = map_points

add = '/mapserver/tile/{z}/{y}/{x}'
ESRI = dict(World_Ocean_Base='http://services.arcgisonline.com/arcgis/rest/services/Ocean/World_Ocean_Base',
            World_Navigation_Charts='http://services.arcgisonline.com/arcgis/rest/services/specialty/world_navigation_charts',
            NatGeo_World_Map='http://services.arcgisonline.com/arcgis/rest/services/NatGeo_World_Map/MapServer/0',
            World_Imagery='http://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer',
            World_Physical_Map='http://services.arcgisonline.com/arcgis/rest/services/World_Physical_Map/MapServer',
            World_Shaded_Relief='http://services.arcgisonline.com/arcgis/rest/services/World_Shaded_Relief/MapServer',
            World_Street_Map='http://services.arcgisonline.com/arcgis/rest/services/World_Street_Map/MapServer')
            #World_Terrain_Base='http://services.arcgisonline.com/arcgis/rest/services/World_Terrain_Base/MapServer',
            #World_Topo_Map='http://services.arcgisonline.com/arcgis/rest/services/World_Topo_Map/MapServer'

for tile_name, tile_url in ESRI.items():
    tile_url += add
    folium.TileLayer(tile_url,
                    name=tile_name,
                    attr='Tiles & copy,etc.').add_to(map_points)
    
folium.LayerControl().add_to(map_layers)

map_layers


# In[158]:


# Creating a heatmap

from folium.plugins import HeatMap

# Create our point map object

map_heat = folium.Map(location=[-33.925, 18.625], tiles='CartoDB dark_matter', zoom_start=10)

for point in range(0, suburbs_location_list_size):
    folium.Circle(
        location=suburbs_location_list[point],
        popup=df_suburbs['Suburb'][point] + ': ' + str(df_suburbs['Oct 2017\nkl/month'][point]) + 'kL',
        radius='15',
        color='#17cbef',
        fill=True,
        opacity=0.8,
        fill_color='#17cbef',
        stroke=True,
        weight=1.0
    ).add_to(map_heat)
    
# Convert to array format for our heatmap
suburbsArray = df_suburbs[['Latitude', 'Longitude']].values

# Plot Heatmap - 
map_heat.add_child(HeatMap(suburbsArray))

map_heat


# In[ ]:


# Sharing and exporting maps to either images of webapps. To do this we need selenium


# In[159]:


pip install selenium


# In[160]:


# Allows us to interact with the local file system, save the image and add a five second delay

import os
import time
from selenium import webdriver


# In[166]:


delay = 5

heat = 'map_heat.html'
unemployment = 'map_unemployment.html'

def export_maps(map_file, map_image, map_obj):
    browser = webdriver.Chrome('C:\\Users\\esaeri-1122\\Downloads\\chromedriver_win32\\chromedriver.exe')
    tmpUrl = 'file://{path}/{mapfile}'.format(path=os.getcwd(), mapfile=map_file)
    map_obj.save(map_file)
    browser.get(tmpUrl)
    time.sleep(delay)
    browser.save_screenshot(map_image)
    browser.quit()
    
export_maps(heat, 'map_heat.png', map_heat)


# In[167]:


# Unemployment Map of the African Continnent

export_maps(unemployment, 'map_unemployment.png', map_unemployment)


# In[ ]:




