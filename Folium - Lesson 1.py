#!/usr/bin/env python
# coding: utf-8

# In[52]:


pip install folium


# In[53]:


import folium


# In[54]:


import pandas as pd


# In[55]:


pip install xlrd


# In[56]:


df_suberbs = pd.read_excel('C:\\Users\\esaeri-1122\\waterwatch_clean2.xlsx', sheet_name = 'Sheet1')


# In[57]:


df_suberbs.head()


# In[58]:


df_suberbs.columns


# In[59]:


df_suberbs.shape


# In[60]:


df_suberbs.describe()


# In[61]:


map_osm = folium.Map(location = [-33.925, 18.625], zoom_start=10)
map_osm


# In[62]:


map_dark = folium.Map(location = [-33.925, 18.625], tiles='CartoDB dark_matter', zoom_start=10)
map_dark


# In[63]:


df_suberbs_locations = df_suberbs[['Latitude', 'Longitude']]
#df_suberbs_locations
suberbs_location_list = df_suberbs_locations.values.tolist()
suberbs_location_list_size = len(suberbs_location_list)
suberbs_location_list_size


# In[64]:


for point in range(0, suberbs_location_list_size):
    folium.Marker(suberbs_location_list[point]).add_to(map_osm)
    folium.Marker(suberbs_location_list[point]).add_to(map_dark)
    
map_osm


# In[65]:


map_dark


# In[66]:


for point in range(0, suberbs_location_list_size):
    folium.Marker(suberbs_location_list[point], popup=df_suberbs['Suburb'][point]).add_to(map_osm)
    folium.Marker(suberbs_location_list[point], popup=df_suberbs['Suburb'][point]).add_to(map_dark)
    
map_osm


# In[67]:


map_dark


# In[68]:


for point in range(0, suberbs_location_list_size):
    folium.Marker(suberbs_location_list[point], popup=df_suberbs['Suburb'][point], icon=folium.Icon(color='darkblue', icon_color='white', icon='tint', angle=0, prefix='fa')).add_to(map_osm)
    folium.Marker(suberbs_location_list[point], popup=df_suberbs['Suburb'][point], icon=folium.Icon(color='darkblue', icon_color='white', icon='tint', angle=0, prefix='fa')).add_to(map_dark)
    
map_osm


# In[ ]:




