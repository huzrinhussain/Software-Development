print('Select your choice')
print('enter ‘1’ if you want to convert from Celsius to Fahrenheit')
print('enter ‘2’ if you want to convert from Fahrenheit to Celsius')

choice = int(input('Enter your choice: '))

if choice == 1:
    celsius = int(input('Enter Celsius: '))
    celciusToFah = (celsius * 1.8) + 32
    print(celsius, 'converted to fahrenheit is: ',celciusToFah)
elif choice == 2:
    fahrenheit = int(input('Enter fahrenheit: '))
    fahToCelcius = (fahrenheit - 32) / 1.8
    print(fahrenheit, 'converted to celsius is: ',fahToCelcius)
else:
    print('Please select your choice 1 or 2')