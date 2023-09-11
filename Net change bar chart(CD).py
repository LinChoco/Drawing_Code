import pandas as pd
import matplotlib.pyplot as plt

excel_file_path = r'C:\Users\a4011\OneDrive\桌面\side_project\Ubike\Data_collection\merged_result.xlsx'
data = pd.read_excel(excel_file_path)

condition = data['day_mode'] == 'C_HS'
filtered_data = data[condition]

time_periods = filtered_data['rent_time']
net_changes = filtered_data['net_change']

fig, ax1 = plt.subplots()

ax1.axhline(0, color='black', linewidth=1.0)

ax1.bar(time_periods, net_changes, alpha=1.0, color='green')
ax1.set_xlabel('Period Of Time')
ax1.set_ylabel('Number Of Rent-Return', color='black')
ax1.set_title('Net Change(C_HS)')
ax1.tick_params(axis='y', labelcolor='black')

ax1.set_xticks(time_periods)  
ax1.set_xticklabels(time_periods, rotation=-90, ha='right')  

ax1.set_ylim(130, -30)

ax1.invert_yaxis()

plt.tight_layout()  

plt.savefig('Net chnage bar chart(C_HS).png')

plt.show()
