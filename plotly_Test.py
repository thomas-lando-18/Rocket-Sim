import plotly.express as px
import geopandas as gpd

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

fig = px.choropleth(world,
                    geojson=world.geometry.__geo_interface__,
                    locations=world.index,
                    scope="world",
                    title='Natural Earth Countries')

fig.write_html("test.html")