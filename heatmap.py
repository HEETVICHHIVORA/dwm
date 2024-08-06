import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
# Example: Heatmap
data = np.random.rand(10, 12)
sns.heatmap(data, cmap='viridis')
# plt.title('Heatmap Example')
plt.show()
