# to run the app type 
# bokeh serve --show sync_two_dropdowns.py

import pandas as pd
import numpy as np

# Import figure from bokeh.plotting
from bokeh.plotting import figure, ColumnDataSource

# Import output_file and show from bokeh.io
from bokeh.io import output_notebook, show, curdoc

# import the HoverTool
from bokeh.models import HoverTool, CategoricalColorMapper, CDSView, GroupFilter, Slider, Select, Button, CheckboxGroup, RadioGroup, Toggle

from bokeh.layouts import row, column, gridplot, widgetbox

from bokeh.models.widgets import Tabs, Panel

# Create two dropdown Select widgets: select1, select2
select1 = Select(title='First', options=['A', 'B'], value='A')
select2 = Select(title='Second', options=['1', '2', '3'], value='1')

# Define a callback function: callback
def callback(attr, old, new):
    # If select1 is 'A' 
    if select1.value == 'A':
        # Set select2 options to ['1', '2', '3']
        select2.options = ['1', '2', '3']

        # Set select2 value to '1'
        select2.value = '1'
    else:
        # Set select2 options to ['100', '200', '300']
        select2.options = ['100', '200', '300']

        # Set select2 value to '100'
        select2.value = '100'

# Attach the callback to the 'value' property of select1
select1.on_change('value', callback)

# Create layout and add to current document
layout = widgetbox(select1, select2)
curdoc().add_root(layout)