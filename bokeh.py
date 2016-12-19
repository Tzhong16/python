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



#############################
#Multiple plot in one graph
############################

# Create the figure: p
p = figure(x_axis_label='fertility', y_axis_label='female_literacy (% population)')

# Add a circle glyph to the figure p
p.circle(fertility_latinamerica, female_literacy_latinamerica)

# Add an x glyph to the figure p
p.x(fertility_africa, female_literacy_africa)

# Specify the name of the file
output_file('fert_lit_separate.html')

# Display the plot
show(p)



############################
#Size, color, alpha
##############################

# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add a blue circle glyph to the figure p
p.circle(fertility_latinamerica, female_literacy_latinamerica, color = 'blue' , size = 10 , alpha = 0.8)

# Add a red circle glyph to the figure p
p.circle(fertility_africa, female_literacy_africa, color = 'red', size = 10, alpha = 0.8)

# Specify the name of the file
output_file('fert_lit_separate_colors.html')

# Display the plot
show(p)

