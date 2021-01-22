from pygal.maps.world import COUNTRIES

excluded_countries = {'Vietnam': 'vn', 'Bolivia': 'bo', 'Congo, Dem. Rep.': 'cd', 
	'Egypt, Arab Rep.': 'eg', 'Gambia, The': 'gm', 'Hong Kong SAR, China': 'hk',
	'Iran, Islamic Rep.': 'ir', 'Korea, Dem. Rep.': 'kp', 'Korea, Rep.': 'kr',
	'Kyrgyz Republic': 'kg', 'Lao PDR': 'la', 'Libya': 'ly', 'Macao SAR, China': 'mo',
	'Macedonia, FYR': 'mk', 'Tanzania': 'tz', 'Venezuela, RB': 've', 'Yemen, Rep.': 'ye'}
	
def get_country_code(country_name):
	"""Get the respective country code for the country name given in the argument."""
	for code, country in COUNTRIES.items():
		if country.lower() == country_name.lower():
			return code
		elif country_name in excluded_countries.keys():
			return excluded_countries[country_name]
					
	# If no code is found, return none.
	return None

 

''' 
filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)


countries = []
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		countries.append(pop_dict['Country Name'])
		
excluded_countries = []

for country in countries:
	if country not in COUNTRIES.values():
		excluded_countries.append(country)
		
for country in excluded_countries:
	print(country)
'''
