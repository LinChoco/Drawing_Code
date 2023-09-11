import pandas as pd
import matplotlib.pyplot as plt

excel_file = r'C:\Users\a4011\OneDrive\桌面\side_project\Ubike\Data_collection\merged_result.xlsx'
df = pd.read_excel(excel_file)

grouped_data = df.groupby('day_mode')[['avg_rent', 'avg_return']].sum()


selected_modes = ['A_WS', 'B_WR', 'C_HS', 'D_HR']
selected_data = grouped_data[grouped_data.index.isin(selected_modes)]

fig, ax = plt.subplots()

bar_width = 0.3
x_pos = range(len(selected_data.index))

ax.bar(x_pos, selected_data['avg_rent'], width=bar_width, align='center', label='Rent', color='blue')
ax.bar(x_pos, selected_data['avg_return'], width=-bar_width, align='center', label='Return', color='red')

ax.set_ylabel('Number')
ax.set_xlabel('Category')
ax.set_title('Rent & Return(Day)')
ax.set_xticks([i for i in x_pos])
ax.set_xticklabels(selected_data.index)

ax.legend()

plt.xticks(rotation=0, ha='right')

plt.tight_layout()
plt.savefig('Rent_Return bar chart.png')
plt.show()
