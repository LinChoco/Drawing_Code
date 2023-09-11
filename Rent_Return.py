import pandas as pd
import os

df=pd.read_csv(r'C:\Users\a4011\OneDrive\桌面\side_project\Ubike\Data_collection\202305_YouBike2.0.csv',encoding_errors='ignore')
filtered_data = df[df['return_station'] == 'Gongguan Station Exit No.2']
pathh = r'C:\Users\a4011\OneDrive\桌面\side_project\Ubike\Data_collection'
csv_filename = 'Return_Gongguan Station Exit No.2.csv'
filtered_data.to_csv(os.path.join(pathh, csv_filename), sep=',', index=False, header=True, encoding='utf-8-sig')