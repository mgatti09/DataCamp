# Updating plots from dropdowns
import pandas as pd

# Import figure from bokeh.plotting
from bokeh.plotting import figure, ColumnDataSource

# Import output_file and show from bokeh.io
from bokeh.io import output_notebook, show, curdoc

# import the HoverTool
from bokeh.models import HoverTool, CategoricalColorMapper, CDSView, GroupFilter, Slider, Select, Button, CheckboxGroup, RadioGroup, Toggle

from bokeh.layouts import row, column, gridplot, widgetbox

from bokeh.models.widgets import Tabs, Panel

df = pd.read_csv('../_datasets/literacy_birth_rate.csv')
df = df.fillna(df.mean())
df.columns = ['Country ', 'Continent', 'female_literacy', 'fertility', 'population']

# Create ColumnDataSource: source
source = ColumnDataSource(data={
    'x' : df.fertility,
    'y' : df.female_literacy
})

# Create a new plot: plot
plot = figure()

# Add circles to the plot
plot.circle('x', 'y', source=source)

# Define a callback function: update_plot
def update_plot(attr, old, new):
    # If the new Selection is 'female_literacy', update 'y' to female_literacy
    if new == 'female_literacy': 
        source.data = {
            'x' : df.fertility,
            'y' : df.female_literacy
        }
    # Else, update 'y' to population
    else:
        source.data = {
            'x' : df.fertility,
            'y' : df.population
        }

# Create a dropdown Select widget: select    
select = Select(title="distribution", options=['female_literacy', 'population'], value='female_literacy')

# Attach the update_plot callback to the 'value' property of select
select.on_change('value', update_plot)

# Create layout and add to current document
layout = row(select, plot)
curdoc().add_root(layout)