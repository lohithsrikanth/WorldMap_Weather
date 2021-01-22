import json
import pygal
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
from country_codes import get_country_code

# Load the data into a list
filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)
	
# Build a dictionary for population data
cc_population = {}	
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		code = get_country_code(country)
		if code:
			cc_population[code] = population

cc_pop1, cc_pop2, cc_pop3 = {}, {}, {}
for cc, pop in cc_population.items():
	if pop < 10000000:
		cc_pop1[cc] = pop
	elif pop < 1000000000:
		cc_pop2[cc] = pop
	else:
		cc_pop3[cc] = pop

# See how many countries are in each level
print(len(cc_pop1), len(cc_pop2), len(cc_pop3))

wm_style = RS('#336699', base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = "World Population in 2010, by Country"
wm.add('0-10m', cc_pop1)
wm.add('10m-1bn', cc_pop2)
wm.add('>1bn', cc_pop3)

wm.render_to_file('world_population.svg')
			
