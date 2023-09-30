"""import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot(df, views):
    fig, axs = plt.subplots(1, 5, figsize=(15, 3), sharey=True)

    for i, ax in enumerate(axs):
        ax.plot(df[df['View'] == views[i]]['Response'])
        ax.set_title(views[i])

    plt.show()

# Example usage:
views = ['view1', 'view2', 'view3', 'view4', 'view5']

# Create synthetic data
data = {
    'View': np.repeat(views, 20),  # Repeat each view 20 times
    'Response': np.random.rand(100)  # 100 random numbers
}

df = pd.DataFrame(data)  # Create DataFrame from synthetic data
plot(df, views)"""


l = d = r = r = [1,2,3]

print(d)