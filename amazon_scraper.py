import requests
import time

class CryptoPriceMonitor:
    def __init__(self):
        # API الرسمي لمنصة Binance (لا يحتاج مفتاح سري للمعلومات العامة)
        self.base_url = "https://api.binance.com/api/v3/ticker/price"
        self.assets = ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT']

    def get_live_prices(self):
        print(f"--- Fetching Live Market Data ({time.strftime('%H:%M:%S')}) ---")
        try:
            for symbol in self.assets:
                params = {'symbol': symbol}
                response = requests.get(self.base_url, params=params)
                
                if response.status_code == 200:
                    data = response.json()
                    price = float(data['price'])
                    print(f"Symbol: {symbol} | Price: ${price:,.2f}")
                else:
                    print(f"Could not fetch {symbol}. Status: {response.status_code}")
                    
        except Exception as e:
            print(f"Connection Error: {e}")

    def start_alert_system(self, interval=10):
        # يقوم بتحديث الأسعار كل 10 ثوانٍ (كعرض تجريبي)
        try:
            for _ in range(5):
                self.get_live_prices()
                print("-" * 40)
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\nMonitoring stopped by user.")

if __name__ == "__main__":
    monitor = CryptoPriceMonitor()
    monitor.start_alert_system()

