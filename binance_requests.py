import requests


class Binance:
    def __init__(self):
        self.data_file_name = 'Binance_BTCUSDT.csv'
        self.symbol = 'BTCUSDT'  # Пара
        self.interval = '1d'  # Период свечи
        self.limit = 1000  # Количество свечей
        self.data = list()

    def get_candles(self):
        """Make the API request to get particular pair klines - """
        response = requests.get(f'https://api.binance.com/api/v3/klines?' 
                                f'symbol={self.symbol}'
                                f'&interval={self.interval}'
                                f'&limit={self.limit}')
        # Convert the response data to a list of lists
        self.data = [[int(d[0]),     # Open time (in milliseconds) \\ Время открытия
                      float(d[1]),   # Open price
                      float(d[2]),   # High price
                      float(d[3]),   # Low price
                      float(d[4]),   # Close price
                      float(d[5]),   # Volume
                      int(d[6]),     # Close time (in milliseconds)
                      float(d[7]),   # Quote asset volume \\ Объем квотируемой валюты
                      int(d[8]),     # Number of trades \\ Кол-во сделок
                      float(d[9]),   # Taker buy base asset volume
                      float(d[10]),  # Taker buy quote asset volume
                      float(d[11])]  # Ignore
                     for d in response.json()]

    def record_data(self):
        t_header = "Open time;Open price;" \
                   "High price;Low price;Close price;" \
                   "Volume;Close time;Quote asset volume;" \
                   "Number of trades;Taker buy base asset volume;" \
                   "Taker buy quote asset volume;Ignore \n"
        with open(self.data_file_name, 'w') as f:
            f.write(t_header)
            [f.write(';'.join([str(item) for item in record])+'\n') for record in self.data]


if __name__ == '__main__':
    binan = Binance()
    binan.get_candles()
    binan.record_data()
