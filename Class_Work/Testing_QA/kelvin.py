#!/usr/bin/python3

def KelvinToFahrenheit(Temperature):
    
    if Temperature < 0:
        raise ValueError("Colder than absolute zero!")
        
    return ((Temperature-273)*1.8)+32

# for i in range(1, 1000, 30):
#     print(f'''       self.assertEqual(k.KelvinToFahrenheit({i}, {((i-273)*1.8)+32})''')