import pandas as pd
import matplotlib.pyplot as plt

# Create a 2D array of the table given above
data = [['E001', 'M', 34, 123, 'Normal', 350],
        ['E002', 'F', 40, 114, 'Overweight', 450],
        ['E003', 'F', 37, 135, 'Obesity', 169],
        ['E004', 'M', 30, 139, 'Underweight', 189],
        ['E005', 'F', 44, 117, 'Underweight', 183],
        ['E006', 'M', 36, 121, 'Normal', 80],
        ['E007', 'M', 32, 133, 'Obesity', 166],
        ['E008', 'F', 26, 140, 'Normal', 120],
        ['E009', 'M', 32, 133, 'Normal', 75],
        ['E010', 'M', 36, 133, 'Underweight', 40]]

# Create a DataFrame with the above data array
df = pd.DataFrame(data, columns=['EMPID', 'Gender', 
                                 'Age', 'Sales',
                                 'BMI', 'Income'])

# Scatter plot between Income and Age
plt.scatter(df['Income'], df['Age'])
plt.xlabel('Income')
plt.ylabel('Age')
plt.title('Scatter plot between Income and Age')
plt.show()
