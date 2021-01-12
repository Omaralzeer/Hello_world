light_year = float(input())
speed_of_light =299792458
days=365.25
hour =24
min =60
s = 60

def time(light_year):
	return light_year *speed_of_light *days*hour*min*s

print(f"{light_year} light year = {time(light_year)} meter")