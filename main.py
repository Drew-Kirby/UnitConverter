from flask import Flask, render_template, request

app = Flask(__name__)

unit = 0
unitType = None
unitConvert = None
output = 0
chosenCategory = None

lengthUnits = ('mm', 'cm', 'm', 'km', 'in', 'ft', 'yd', 'mi', 'nm')
weightUnits = ('mg', 'g', 'kg', 't', 'oz', 'lb', 'st', 'ton')
volumeUnits = ('ml', 'l', 'm3', 'tsp', 'tbsp', 'fl oz', 'c', 'pt', 'qt', 'gal')
temperatureUnits = ('Celsius', 'Fahrenheit', 'Kelvin')
timeUnits = ('ms', 's', 'min', 'hr', 'days', 'weeks', 'months', 'years')
areaUnits = ('cm2', 'm2', 'km2', 'in2', 'ft2', 'acres', 'ha')
electricUnits = ('V', 'A', 'Ohm', 'W', 'kWh', 'T')
digitalUnits = ('b', 'B', 'KB', 'MB', 'GB', 'TB', 'PB')
measurementCategories = (lengthUnits, weightUnits, volumeUnits, temperatureUnits, timeUnits, areaUnits, electricUnits, digitalUnits)

def conversion(unit, unitType, unitConvert):
    chosenCategory = None

    for i in measurementCategories:
        if unitType in i:
            chosenCategory = i
            break
    if chosenCategory == None:
        print(f'{unitType} is not a valid unit type.')

    if unitConvert not in chosenCategory:
        return None, f"Cannot convert {unitType} to {unitConvert}."

    output = None

    if chosenCategory == temperatureUnits:
        if unitType == 'Celsius':
            base_val = unit
        elif unitType == 'Fahrenheit':
            base_val = (unit-32) * 5/9
        elif unitType == 'Kelvin':
            base_val = unit - 273.15
        
        if unitConvert == 'Celsius':
            output = base_val
        elif unitConvert == 'Fahrenheit':
            output = (base_val * 9/5) + 32
        elif unitConvert == 'Kelvin':
            output = base_val + 273.15
    elif chosenCategory == lengthUnits:
        length_to_m = {'mm': 0.001, 'cm': 0.01, 'm': 1.0, 'km': 1000.0, 'in': 0.0254, 'ft': 0.3048, 'yd': 0.9144, 'mi': 1609.344, 'nm': 1852.0}

        base_val = unit * length_to_m[unitType]
        output = base_val / length_to_m[unitConvert]
    elif chosenCategory == weightUnits:
        weight_to_g = {'mg': 0.001, 'g': 1.0, 'kg': 1000.0, 't': 1000000.0, 'oz': 28.3495, 'lb': 453.592, 'st': 6350.29, 'ton': 907184.74}

        base_val = unit * weight_to_g[unitType]
        output = base_val / weight_to_g[unitConvert]
    elif chosenCategory == volumeUnits:
        volume_to_l = {'ml': 0.001, 'l': 1.0, 'm3': 1000.0, 'tsp': 0.00492892, 'tbsp': 0.0147868, 'fl oz': 0.0295735, 'c': 0.236588, 'pt': 0.473176, 'qt': 0.946353, 'gal': 3.78541}

        base_val = unit * volume_to_l[unitType]
        output = base_val / volume_to_l[unitConvert]
    elif chosenCategory == timeUnits:
        time_to_s = {'ms': 0.001, 's': 1.0, 'min': 60.0, 'hr': 3600.0, 'days': 86400.0, 'weeks': 604800.0, 'months': 2628000.0, 'years': 31536000.0}

        base_val = unit * time_to_s[unitType]
        output = base_val / time_to_s[unitConvert]
    elif chosenCategory == areaUnits:
        area_to_m2 = {'cm2': 0.0001, 'm2': 1.0, 'km2': 1000000.0, 'in2': 0.00064516, 'ft2': 0.092903, 'acres': 4046.86, 'ha': 100000}

        base_val = unit * area_to_m2[unitType]
        output = base_val / area_to_m2[unitConvert]
    elif chosenCategory == electricUnits:
        if unitType == 'W' and unitConvert == 'kWh':
            output = unit / 1000
        elif unitType == 'kWh' and unitConvert == 'W':
            output = unit * 1000
        elif unitType == unitConvert:
            output = unit
        else:
            output = None
            print("Direct cross-conversion between these electrical properties requires more data.")
    elif chosenCategory == digitalUnits:
        digital_to_B = {'b': 0.125, 'B': 1.0, 'KB': 1024.0, 'MB': 1048576.0, 'GB': 1073741824.0, 'TB': 1099511627776.0, 'PB': 1125899906842624.0}

        base_val = unit * digital_to_B[unitType]
        output = base_val / digital_to_B[unitConvert]

    if output is not None:
        return output, None
    return None, "An error was encountered when converting."

@app.route("/", methods=["GET", "POST"])
def home():
    input_value = None
    from_unit = None
    to_unit = None
    output_value = None
    error_msg = None

    if request.method == "POST":
        input_value = float(request.form.get("user_value", 0))
        from_unit = request.form.get("from_unit")
        to_unit = request.form.get("to_unit")

        output_value, error_msg = conversion(input_value, from_unit, to_unit)

    return render_template(
        "index.html",
        input_value=input_value,
        from_unit=from_unit,
        to_unit=to_unit,
        output_value=output_value,
        error_msg=error_msg
    )

if __name__ == "__main__":
    app.run(debug=True)