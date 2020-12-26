# Operator Hitung Program Koversi Temperatur

print("\nProgram Konversi Temperatur\n")

# Celcius = float(input("Masukan Suhu dalam Celcius : "))
# print("Suhu dalam Celcius adalah ",Celcius,"Celcius")

# #reamur
# reamur =  (4 / 5) * Celcius
# print("Suhu dalam reamur adalah ",reamur,"Reamur")

# # fahrenheit
# fahrenheit = (( 9 / 5) * Celcius) + 32
# print("Suhu dalam Fahrenheit adalah ",fahrenheit,"Fahrenheit")

# # Kelvin
# Kelvin = Celcius + 273
# print("Suhu dalam Kelvin adalah = ",Kelvin,"Kelvin")

# Kelvin -> Fahrenheit = (9 / 5 (k-273))+32
# Kelvin = float(input("Masukan Suhu dalam Celcius : "))
# print("Suhu dalam Kelvin adalah ",Kelvin,"K")

# Fahrenheit = (1.8*(Kelvin - 273))+32
# print("Suhu dalam Kelvin adlah : ",Fahrenheit,"F")

# Fahrenheit -> Kelvin = (5 / 9 * (F-32))+273
fahrenheit = float(input("Masukan Suhu : ",))
print("Suhu dalam Kelvin adalah : ",fahrenheit,"F")

Kelvin = (5 / 9 * (fahrenheit-32))+273
print("Suhu dalam Kelvin adalah : ",Kelvin,"K")