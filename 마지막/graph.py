import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# 남극 및 북극 빙하 데이터 읽기
antarctic_data = pd.concat([pd.read_csv(
    f"마지막/south/S_{str(i).zfill(2)}_extent_v3.0.csv") for i in range(1, 13)])
arctic_data = pd.concat([pd.read_csv(
    f"마지막/north/N_{str(i).zfill(2)}_extent_v3.0.csv") for i in range(1, 13)])

# 남극 및 북극 빙하 데이터 열 이름 정리
antarctic_data.columns = antarctic_data.columns.str.strip()
arctic_data.columns = arctic_data.columns.str.strip()

# 남극 및 북극 빙하 데이터에서 불필요하거나 오류가 있는 데이터 제거
antarctic_data_cleaned = antarctic_data[(
    antarctic_data['extent'] != -9999) & (antarctic_data['area'] != -9999)]
arctic_data_cleaned = arctic_data[(
    arctic_data['extent'] != -9999) & (arctic_data['area'] != -9999)]

# 남극 및 북극 빙하 데이터를 1979년부터 2022년까지 시간별로 필터링
antarctic_data_filtered = antarctic_data_cleaned[(
    antarctic_data_cleaned['year'] >= 1979) & (antarctic_data_cleaned['year'] <= 2022)]
arctic_data_filtered = arctic_data_cleaned[(
    arctic_data_cleaned['year'] >= 1979) & (arctic_data_cleaned['year'] <= 2022)]

# 남극 및 북극 빙하 데이터에서 년도별 평균 Extent 계산
antarctic_yearly_avg = antarctic_data_filtered.groupby('year')['extent'].mean()
arctic_yearly_avg = arctic_data_filtered.groupby('year')['extent'].mean()

# CO2 발생량 데이터 읽기
new_co2_data = pd.read_excel("마지막/CO2.xlsx")

# CO2 발생량 데이터에서 'year' 열을 숫자 형태로 변환
new_co2_data['year'] = pd.to_numeric(new_co2_data['year'], errors='coerce')

# 숫자 형태로 변환된 'year' 열을 바탕으로 데이터 필터링
new_co2_data_filtered = new_co2_data[(
    new_co2_data['year'] >= 1979) & (new_co2_data['year'] <= 2022)]

# 선형 회귀 모델 정의
model = LinearRegression()

# 남극 빙하 Extent 선형 예측
X_antarctic = antarctic_yearly_avg.index.values.reshape(-1, 1)
y_antarctic = antarctic_yearly_avg.values
model.fit(X_antarctic, y_antarctic)
antarctic_pred_years = np.array(range(2023, 2041)).reshape(-1, 1)
antarctic_pred = model.predict(antarctic_pred_years)

# 북극 빙하 Extent 선형 예측
X_arctic = arctic_yearly_avg.index.values.reshape(-1, 1)
y_arctic = arctic_yearly_avg.values
model.fit(X_arctic, y_arctic)
arctic_pred_years = np.array(range(2023, 2041)).reshape(-1, 1)
arctic_pred = model.predict(arctic_pred_years)

# CO2 발생량 선형 예측
X_co2 = new_co2_data_filtered['year'].values.reshape(-1, 1)
y_co2 = new_co2_data_filtered['emissions(in billion metric tons)'].values
model.fit(X_co2, y_co2)
co2_pred_years = np.array(range(2023, 2041)).reshape(-1, 1)
co2_pred = model.predict(co2_pred_years)

# 그래프 색상 변경 및 생성
fig, ax1 = plt.subplots(figsize=(12, 6))

# 남극 빙하 Extent 그래프 (파란색)
ax1.plot(antarctic_yearly_avg.index, antarctic_yearly_avg.values,
         label='Antarctic Ice Extent (Yearly Avg)', color='blue')
ax1.plot(antarctic_pred_years.flatten(), antarctic_pred,
         label='Antarctic Ice Extent Prediction', linestyle='dashed', color='blue')

# 북극 빙하 Extent 그래프 (빨간색)
ax1.plot(arctic_yearly_avg.index, arctic_yearly_avg.values,
         label='Arctic Ice Extent (Yearly Avg)', color='red')
ax1.plot(arctic_pred_years.flatten(), arctic_pred,
         label='Arctic Ice Extent Prediction', linestyle='dashed', color='red')

ax1.set_xlabel('Year')
ax1.set_ylabel('Ice Extent (in million square kilometers)')
ax1.legend(loc='upper left')
ax1.grid(True)

# CO2 발생량 그래프에 대한 새로운 축 생성 (초록색)
ax2 = ax1.twinx()
ax2.plot(new_co2_data_filtered['year'], new_co2_data_filtered['emissions(in billion metric tons)'],
         label='CO2 Emissions (billion metric tons)', color='green')
ax2.plot(co2_pred_years.flatten(), co2_pred,
         label='CO2 Emissions Prediction', color='green', linestyle='dashed')
ax2.set_ylabel('CO2 Emissions (in billion metric tons)')
ax2.legend(loc='upper right')

plt.title('Yearly Average Antarctic and Arctic Ice Extent and CO2 Emissions with Predictions up to 2040')
plt.show()
