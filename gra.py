import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

# Load the greenhouse gas emissions data
greenhouse_gas_path = "C:/Users/LoewllZoe/Desktop/온실배출 2.xlsx"
greenhouse_gas_df = pd.read_excel(greenhouse_gas_path)

# Extract country-specific greenhouse gas emissions columns
country_specific_gas_emissions = greenhouse_gas_df.drop(columns=['YEAR', '합계'])

# Load the natural disasters data and calculate the yearly count
natural_disasters_path = "C:/Users/LoewllZoe/Desktop/public_emdat_custom_request_2023-10-03_332be375-ca0b-4b95-a80f-25703e6911c1.xlsx"
natural_disasters_df = pd.read_excel(natural_disasters_path)
natural_disasters_count = natural_disasters_df.groupby('Start Year')['DisNo.'].count()

# Define the font path for Korean font
font_path = "C:/Users/LoewllZoe/Desktop/NanumGothicBold.ttf"
font_properties = font_manager.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_properties.get_name()

# Re-plot the graph with adjusted y-axis limit based on the maximum value of greenhouse gas emissions
plt.figure(figsize=(16, 8))

# Plot the original cumulative greenhouse gas emissions by country
plt.stackplot(greenhouse_gas_df['YEAR'], country_specific_gas_emissions.T, labels=country_specific_gas_emissions.columns, alpha=0.5)

# Calculate the maximum value of greenhouse gas emissions
max_gas_emission = country_specific_gas_emissions.sum(axis=1).max()

# Manually set the y-axis limit based on the maximum value of greenhouse gas emissions
plt.ylim(0, max_gas_emission * 1.5)  # Set the max y-value to 1.5 times the max value of greenhouse gas emissions

# Add natural disasters frequency on a secondary y-axis
ax2 = plt.gca().twinx()
ax2.plot(natural_disasters_count.index, natural_disasters_count.values, label='Natural Disasters', color='black', marker='o')
ax2.set_ylabel('Number of Natural Disasters', fontproperties=font_properties)

# Labels, titles, and legends
plt.xlabel('Year', fontproperties=font_properties)
plt.ylabel('Greenhouse Gas Emissions (MTCO2)', fontproperties=font_properties)
plt.title('Cumulative Greenhouse Gas Emissions by Country and Natural Disasters', fontproperties=font_properties)
plt.legend(loc='upper left', prop=font_properties, title='Greenhouse Gas Emissions')
ax2.legend(loc='upper right', prop=font_properties, title='Natural Disasters')

plt.grid(True)
plt.show()
