import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

#Далайг хөх өнгөөр, нуурыг бүдэг хөх өнгөөр, голыг цэнхэр өнгөөр будав.
#Улсуудын хилийг улаан өнгөөр будсан болно.

fig = go.Figure(go.Scattergeo())
fig.update_geos(
    visible=True, resolution=50,
    showcountries=True, countrycolor="Red",
    showlakes=True, lakecolor="Blue",
    showland=True, landcolor="White",
    showocean=True, oceancolor="Blue",
    showrivers=True, rivercolor="Cyan",
)
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
fig.show()