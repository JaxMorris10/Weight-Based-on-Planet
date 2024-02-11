def calculate_weight(mass, planet):
    # Dictionary containing the gravitational acceleration of different planets (in m/s^2)
    gravitational_acceleration = {
        "Mercury": 3.7,
        "Venus": 8.87,
        "Earth": 9.81,
        "Mars": 3.71,
        "Jupiter": 24.79,
        "Saturn": 10.44,
        "Uranus": 8.69,
        "Neptune": 11.15
    }
    
    # Check if the provided planet is in the dictionary
    if planet in gravitational_acceleration:
        # Calculate weight using the formula: weight = mass * gravitational_acceleration
        weight = mass * gravitational_acceleration[planet]
        return weight
    else:
        return "Invalid planet name. Please enter a valid planet."

# Example usage:
mass = 75  # in kilograms
planet = "Earth"
weight_on_earth = calculate_weight(mass, planet)
print(f"Your weight on {planet} is {weight_on_earth} Newtons.")

# Calculate weight on Mars
planet = "Mars"
weight_on_mars = calculate_weight(mass, planet)
print(f"Your weight on {planet} is {weight_on_mars} Newtons.")

