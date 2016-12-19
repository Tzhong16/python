####################################################################
#Bokeh package
####################################################################



from bokeh.plotting import figure

# Import output_file and show from bokeh.io
from bokeh.io import output_file, show 

# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add a circle glyph to the figure p
p.circle(fertility, female_literacy)

# Call the output_file() function and specify the name of the file
output_file('fert_lit.html')

show(p)

