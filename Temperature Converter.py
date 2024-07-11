Temp = float(input("Enter your temperature: "))
Unit = input("Tell us  your current unit: ").lower()
while Unit not in ["celsius","kelvin","fahrenheit"]:
    Unit = input("Please write a valid value ").lower()
Unit_Conversion = input("Tell us what unit do you want to convert your current unit into: ").lower()
while Unit_Conversion not in ["celsius","kelvin","fahrenheit"]:
    Unit_Conversion = input("Please write a valid value ").lower()
if Unit == "celsius":
    if Unit_Conversion == "fahrenheit":
        conversion = (9 / 5 * Temp) + 32
if Unit == "fahrenheit":
    if Unit_Conversion == "celsius":
        conversion = (Temp - 32) * 5/9
if Unit == "celsius":
    if Unit_Conversion == "kelvin":
        conversion = Temp + 273.15
if Unit == "kelvin":
    if Unit_Conversion == "celsius":
        conversion = Temp - 273.15
if Unit == "fahrenheit":
    if Unit_Conversion == "kelvin":
        conversion = (Temp - 32) * 5 / 9 + 273.15
if Unit == "kelvin":
    if Unit_Conversion == "fahrenheit":
        conversion = (Temp - 273.15) * 1.8 + 32
print(f"{Temp} degrees {Unit} is equal to {conversion} degrees {Unit_Conversion}")
