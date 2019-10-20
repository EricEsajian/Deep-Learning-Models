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


# In[ ]:




