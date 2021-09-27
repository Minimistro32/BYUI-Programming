from math import pi

width = float(input("Enter the width of the tire in mm (ex 205): "))
aspectRatio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

approxVolume = (pi * (width ** 2) * aspectRatio * ((width * aspectRatio) + (2540 * diameter)))/10000000000

print(f"The apporximate volume is {approxVolume:.2f} liters")