# Import numpy
import numpy as np

weight_lb = [180,
             215,
             210,
             210,
             188,
             176,
             209,
             200,
             231,
             180,
             188,
             180,
             185,
             160,
             180,
             185,
             189,
             185,
             219,
             230,
             205,
             230,
             195,
             180,
             192,
             225,
             203,
             195,
             182,
             188,
             200]
height_in = [74, 72, 72, 73,
             69,
             69,
             71,
             76,
             71,
             73,
             73,
             74,
             74,
             69,
             70,
             73,
             75,
             78,
             79,
             76,
             74,
             76,
             72,
             71,
             75,
             77,
             74,
             73,
             74,
             78,
             73]

# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg / np_height_m ** 2

# Print out bmi
print(bmi)
