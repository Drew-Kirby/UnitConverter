unit = 0
unitType = None
unitConvert = None
output = 0

lengthUnits = ('mm', 'cm', 'm', 'km', 'in', 'ft', 'yd', 'mi', 'nm')
weightUnits = ('mg', 'g', 'kg', 't', 'oz', 'lb', 'st', 'ton')
volumeUnits = ('ml', 'l', 'm3', 'tsp', 'tbsp', 'fl oz', 'c', 'pt', 'qt', 'gal')
temperatureUnits = ('Celcius', 'Fahrenheit', 'Kelvin')
timeUnits = ('ms', 's', 'min', 'hr', 'days', 'weeks', 'months', 'years')
areaUnits = ('cm2', 'm2', 'km2', 'in2', 'ft2', 'acres', 'ha')
electricUnits = ('V', 'A', 'Ohm', 'W', 'kWh', 'T')
digitalUnits = ('b', 'B', 'KB', 'MB', 'GB', 'TB', 'PB')


print(f"Please enter the {unitType} to convert: ")
unit = float(input())
