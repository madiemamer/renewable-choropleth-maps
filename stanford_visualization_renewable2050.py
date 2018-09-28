
# coding: utf-8

# ## This notebook is a visualization of a Stanford study on how each state in the United States can go completely renewable by 2050.
#     This notebook is running on a python kernel
#     This notebook utilizes the plotly module to show each renewable energy form on a choropleth map
#     The Stanford study can be further read up on by following this link: 
#         https://energy.stanford.edu/news/100-renewable-2050 

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

from pandas import DataFrame
data = pd.read_csv("/Users/madelinemamer/Desktop/2050 renewable energy percent.csv")
get_ipython().system('pip install --upgrade pip')
get_ipython().system('pip install plotly')
import plotly as pyt
import plotly.plotly as py


# In[2]:



for col in data.columns:
    data[col] = data[col].astype(str)
    
scl = [ [0.0, 'rgb(255,235,205)'],[0.2,'rgb(255,211,155)'],[0.4, 'rgb(255,215,0)'],[0.6,'rgb(255,185,15)'],[0.8,'rgb(255,165,79)'],[1.0,'rgb(255,128,0)'],      ]

data['text']= data['state']+':'+'Residential Solar PV '+data["r_solar"]+', '+'Solar PV Plants '+data['plants_solar']+', '+ 'CSP plants '+ data['csp_solar']+', '+ 'Commercial & Government ' +data["gov_solar"]


df = [dict(
    type='choropleth',colorscale = scl, autocolorscale=False,locations=data['code'], z=data['r_solar'].astype(float)+data['plants_solar'].astype(float)+data['csp_solar'].astype(float)+data["gov_solar"].astype(float),
            locationmode='USA-states',text=data['text'], marker=dict(line = dict(color = 'rgb(255,255,255)',width = 2)),
            colorbar = dict( title = "Percentage"))]
layout = dict (
    title = "Percentage of Solar",
    geo= dict(
    scope='usa',
    projection=dict(type='albers usa'),
    showlakes = True,
    lakecolor= 'rgb(255,255,255)',
    
    )
)
pyt.tools.set_credentials_file(username="madelinemamer",api_key="zW00QN06lN8NXrBqxGJ8")
fig = dict(data=df, layout=layout)
py.iplot(fig, filename='solar_pv_map')


# In[20]:



for col in data.columns:
    data[col] = data[col].astype(str)
    
scl = [[0.0, 'rgb(204,255,204)'],[0.2, 'rgb(163,214,163)'],[0.4, 'rgb(122,173,122)'],[0.6, 'rgb(82,133,82)'],[0.8,'rgb(41,92,41)'],[1.0,'rgb(0,51,0)']]
data['text']= data['state']+':'+'Land Wind Power '+data["land_wind"]+', '+'Offshore Wind Power '+data['ocean_wind']

df = [dict(
    type='choropleth',colorscale = scl, autocolorscale=False,locations=data['code'], z=data['land_wind'].astype(float)+data['ocean_wind'].astype(float),
            locationmode='USA-states',text=data['text'], marker=dict(line = dict(color = 'rgb(255,255,255)',width = 2)),
            colorbar = dict( title = "Percentage"))]
layout = dict (
    title = "Percentage of Wind",
    geo= dict(
    scope='usa',
    projection=dict(type='albers usa'),
    showlakes = True,
    lakecolor= 'rgb(255,255,255)',
    
    )
)
pyt.tools.set_credentials_file(username="madelinemamer",api_key="zW00QN06lN8NXrBqxGJ8")
fig = dict(data=df, layout=layout)
py.iplot(fig, filename='wind_map')


# In[21]:



for col in data.columns:
    data[col] = data[col].astype(str)
    
scl = [[0.0, 'rgb(204,255,255)'],[0.2, 'rgb(163,204,235)'],[0.4, 'rgb(122,153,214)'],[0.6, 'rgb(82,102,194)'],[0.8,'rgb(41,51,173)'],[1.0,'rgb(0,0,153)']]
data['text']= data['state']+':'+'Hydroelectric Power '+data["hydro"]
df = [dict(
    type='choropleth',colorscale = scl, autocolorscale=False,locations=data['code'], z=data['hydro'].astype(float),
            locationmode='USA-states',text=data['text'], marker=dict(line = dict(color = 'rgb(255,255,255)',width = 2)),
            colorbar = dict( title = "Percentage"))]
layout = dict (
    title = "Percentage of Hydroelectricity",
    geo= dict(
    scope='usa',
    projection=dict(type='albers usa'),
    showlakes = True,
    lakecolor= 'rgb(255,255,255)',
    
    )
)
pyt.tools.set_credentials_file(username="madelinemamer",api_key="zW00QN06lN8NXrBqxGJ8")
fig = dict(data=df, layout=layout)
py.iplot(fig, filename='hydro_map')


# In[22]:


for col in data.columns:
    data[col] = data[col].astype(str)
    
scl = [[0.0, 'rgb(255,204,255)'],[0.2, 'rgb(224,163,224)'],[0.4, 'rgb(194,122,194)'],[0.6, 'rgb(163,82,163)'],[0.8,'rgb(133,41,133)'],[1.0,'rgb(102,0,102)']]
data['text']= data['state']+':'+'Geothermal Power '+data["geo"]
df = [dict(
    type='choropleth',colorscale = scl, autocolorscale=False,locations=data['code'], z=data['geo'].astype(float),
            locationmode='USA-states',text=data['text'], marker=dict(line = dict(color = 'rgb(255,255,255)',width = 2)),
            colorbar = dict( title = "Percentage"))]
layout = dict (
    title = "Percentage of Geothermal",
    geo= dict(
    scope='usa',
    projection=dict(type='albers usa'),
    showlakes = True,
    lakecolor= 'rgb(255,255,255)',
    
    )
)
pyt.tools.set_credentials_file(username="madelinemamer",api_key="zW00QN06lN8NXrBqxGJ8")
fig = dict(data=df, layout=layout)
py.iplot(fig, filename='geo_map')

