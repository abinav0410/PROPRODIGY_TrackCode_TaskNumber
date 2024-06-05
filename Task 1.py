import matplotlib.pyplot as plt

ages = [18, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]

plt.hist(ages, bins=5, color='Red', edgecolor='Black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Ages')
plt.show()
