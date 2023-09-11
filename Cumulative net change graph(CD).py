import pandas as pd
import matplotlib.pyplot as plt

excel_file_path = r'C:\Users\a4011\OneDrive\桌面\side_project\Ubike\Data_collection\merged_result.xlsx'
data = pd.read_excel(excel_file_path)

a_ws_data = data[data['day_mode'] == 'C_HS']

cumulative_changes = a_ws_data['net_change'].cumsum()

fig, ax1 = plt.subplots()

ax1.plot(a_ws_data['rent_time'], cumulative_changes, marker='o', color='green')
ax1.set_xlabel('Period Of Time')
ax1.set_ylabel('Cumulative Number Of Rent-Return', color='black')
ax1.set_title('Cumulative Net Change (C_HS)')
ax1.tick_params(axis='y', labelcolor='black')

ax1.set_xticks(a_ws_data['rent_time'])  
ax1.set_xticklabels(a_ws_data['rent_time'], rotation=-90, ha='right')


ax1.set_ylim(160, -110)
ax1.invert_yaxis()
plt.tight_layout()
plt.savefig('Cumulative net change graph(C_HS).png')
plt.show()
