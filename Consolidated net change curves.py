import pandas as pd
import matplotlib.pyplot as plt

excel_file_path = r'C:\Users\a4011\OneDrive\桌面\side_project\Ubike\Data_collection\merged_result.xlsx'
data = pd.read_excel(excel_file_path)

categories = data['day_mode'].unique()

fig, ax = plt.subplots(figsize=(10, 6))

colors = ['red', 'blue', 'green', 'orange']

for i, category in enumerate(categories):
    category_data = data[data['day_mode'] == category]
    ax.plot(category_data['rent_time'], category_data['net_change'], marker='o', label=category, color=colors[i])

ax.set_xlabel('Period of time')
ax.set_ylabel('Number of Rent-Return')
ax.set_title('Cumulative change curves')
ax.tick_params(axis='y')
ax.legend()
ax.set_xticks(data['rent_time'])
ax.set_xticklabels(data['rent_time'], rotation=-90, ha='right')

plt.tight_layout()

plt.savefig('Consolidated net change curves.png')

plt.show()
