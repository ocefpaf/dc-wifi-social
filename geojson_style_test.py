
# coding: utf-8

# In[1]:


import ipyleaflet as ipyl


# In[34]:


import urllib.request
import json
url = 'https://raw.githubusercontent.com/rsignell-usgs/dc-wifi-social/master/bars.geojson'
req = urllib.request.Request(url)
r = urllib.request.urlopen(req).read()
data = json.loads(r.decode('utf-8'))

center = [38.9, -77.05]
zoom = 12

map = ipyl.Map(center=center, zoom=zoom)
feature_layer = ipyl.GeoJSON(data=data)

map.layers = [map.layers[0], feature_layer]

map

