def main():
    degrees_fahrenheit : float = float(input("Enter the temperature in degrees Fahrenheit: "))
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0
    print(f"{degrees_fahrenheit} degrees Fahrenheit is {degrees_celsius} degrees Celsius")





# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()