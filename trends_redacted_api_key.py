from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.sectorperformance import SectorPerformances
import matplotlib.pyplot as plt


ts = TimeSeries(key='', output_format='pandas')

data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
data['4. close'].plot()
plt.title('Intraday Times Series for the MSFT stock (1 min)')
plt.show()


# Get json object with the intraday data and another with  the call's metadata
'''
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
print(data.head(2))

print("\n\nWelcome to my stock market analysis program.\n\n")

sp = SectorPerformances(key='', output_format='pandas')
data, meta_data = sp.get_sector()
data['Rank A: Real-Time Performance'].plot(kind='bar')
plt.title('Real Time Performance (%) per Sector')
plt.tight_layout()
plt.grid()
plt.show()
'''
