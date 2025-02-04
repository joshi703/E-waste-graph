import matplotlib.pyplot as plt

# Years
years = [2017, 2018, 2019, 2020, 2021, 2022]
# E-waste generated in million metric tons
e_waste = [44.7, 49.3, 53.6, 57.4, 63.1, 68.1]

plt.figure(figsize=(10, 6))
plt.plot(years, e_waste, marker='o', linestyle='-')
plt.title('E-waste Generation Over Recent Years')
plt.xlabel('Year')
plt.ylabel('E-waste Generated (million metric tons)')
plt.grid(True)
plt.xticks(years)
plt.tight_layout()
plt.show()
