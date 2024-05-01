import numpy as np
import matplotlib.pyplot as plt

# Reactor parameters
length = 0.5  # Reactor length (m)
diameter = 0.1  # Reactor diameter (m)
oil_flow = 10  # Oil flow rate (kg/s)
inlet_oil_temp = 800  # Inlet oil temperature (°C)
inlet_ethylbenzene_flow = 4240  # Ethylbenzene inlet flow (kg/h)
inlet_steam_flow = 1160  # Steam flow (kg/h)

# Conversion factors
kg_to_kmol = 1000 / 106.168  # Conversion factor from kg to kmol

# Calculate molar flow rates
inlet_ethylbenzene_flow_kmole = inlet_ethylbenzene_flow * kg_to_kmol
inlet_steam_flow_kmole = inlet_steam_flow * kg_to_kmol

# Constants
R = 8.314  # Gas constant (J/(mol K))

# Reaction rate parameters
k1 = 1.51286  # Rate constant for reaction 1
k2 = 5.6197  # Rate constant for reaction 2
k3 = 1.344  # Rate constant for reaction 3
k4 = 9.30016  # Rate constant for reaction 4
k5 = 0.53163  # Rate constant for reaction 5
k6 = 1.6769 * 10**10  # Rate constant for reaction 6

# Reaction enthalpy coefficients
reaction_enthalpy_coeffs = {
    1: (-120737, -4.56),
    2: (-108802, 7.95),
    3: (53171, 13.19),
    4: (-82054, -8.83),
    5: (-211979, -16.58),
    6: (45217, -10.46)
}

# Lists to store results
lengths = []
temperatures = []
ethylbenzene_flows = []
steam_flows = []
co_flows = []

# Simulation parameters
delta_x = 0.01  # Step size for reactor length
num_points = int(length / delta_x) + 1  # Number of points to simulate

# Initial conditions
temp = inlet_oil_temp
ethylbenzene_flow = inlet_ethylbenzene_flow_kmole
steam_flow = inlet_steam_flow_kmole
co_flow = 0.0

# Simulation loop
for _ in range(num_points):
    # Calculate reaction rates
    p_ethylbenzene = ethylbenzene_flow / (oil_flow * kg_to_kmol)
    p_steam = steam_flow / (oil_flow * kg_to_kmol)
    pt = p_ethylbenzene + p_steam

    r1 = k1 * (p_ethylbenzene - (p_steam * co_flow)) * (1 - pt / 0.4)
    r2 = k2 * p_ethylbenzene
    r3 = k3 * p_ethylbenzene * p_steam
    r4 = k4 * ethylbenzene_flow * steam_flow
    r5 = k5 * ethylbenzene_flow * steam_flow
    r6 = k6 * (pt / temp**3) * steam_flow * co_flow
    
    # Update the molar flow rates
    ethylbenzene_flow -= (r1 + r2 + r3) * delta_x
    co_flow += (r4 + r5 - r6) * delta_x

    # Convert the reaction rates and coefficients to numpy arrays
    rates = np.array([r1, r2, r3, r4, r5, r6])
    reaction_enthalpy_coeffs = np.array(list(reaction_enthalpy_coeffs.values()))

    # Reshape the reaction_enthalpy_coeffs array
    reaction_enthalpy_coeffs = reaction_enthalpy_coeffs.reshape(-1)

    # Update the temperature
    delta_temp = (-np.sum(rates * reaction_enthalpy_coeffs)) / (oil_flow * 4186)
    temp += delta_temp

    # Store the results
    lengths.append(_ * delta_x)
    temperatures.append(temp)
    ethylbenzene_flows.append(ethylbenzene_flow)
    steam_flows.append(steam_flow)
    co_flows.append(co_flow)

# Plot the results
plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1)
plt.plot(lengths, temperatures)
plt.xlabel('Reactor Length (m)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Profile')

plt.subplot(2, 2, 2)
plt.plot(lengths, ethylbenzene_flows)
plt.xlabel('Reactor Length (m)')
plt.ylabel('Ethylbenzene Flow (kmol/s)')
plt.title('Ethylbenzene Flow Profile')

plt.subplot(2, 2, 3)
plt.plot(lengths, steam_flows)
plt.xlabel('Reactor Length (m)')
plt.ylabel('Steam Flow (kmol/s)')
plt.title('Steam Flow Profile')

plt.subplot(2, 2, 4)
plt.plot(lengths, co_flows)
plt.xlabel('Reactor Length (m)')
plt.ylabel('CO Flow (kmol/s)')
plt.title('CO Flow Profile')

plt.tight_layout()
plt.show()
