# Program by: Shervin Marco Mangulabnan
# Date of Creation: September 26, 2024
# Purpose: this program calculates Voltage, Current, or Resistance using Ohm's Law.

# Display the available calculation choices to the user
print("What would you like to calculate?")
print("1. Voltage (V)")
print("2. Current (I)")
print("3. Resistance (R)")

try:
    # Ask the user for their choice
    choice = int(input("Enter the number of your choice (1/2/3): "))
    
    # Calculate Voltage (V = I * R)
    if choice == 1:
        current = float(input("Enter current (in amperes): "))
        resistance = float(input("Enter resistance (in ohms): "))
        voltage = current * resistance
        print(f"The calculated voltage is: {voltage:.2f} volts")
        
    # Calculate Current (I = V / R)
    elif choice == 2:
        voltage = float(input("Enter voltage (in volts): "))
        resistance = float(input("Enter resistance (in ohms): "))
        if resistance == 0:
            print("Error: Resistance cannot be zero.")
        else:
            current = voltage / resistance
            print(f"The calculated current is: {current:.2f} amperes")
            
# Calculate Resistance (R = V / I)
# Handle any input that isn't a valid number
# End of the program
