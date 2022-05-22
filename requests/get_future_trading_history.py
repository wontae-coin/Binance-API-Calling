from binance.client import Client
import json
import os

current_path = os.path.abspath(__file__) # /Users/bbrick/Workspace/Binance_python_api/requests/get_future_trading_history.py
requests_directory = os.path.dirname(current_path) # /Users/bbrick/Workspace/Binance_python_api/requests
mother_directory = os.path.dirname(requests_directory) # /Users/bbrick/Workspace/Binance_python_api

api_key_filename =  os.path.join(mother_directory, 'keys', "10012(main_1)/api_key.txt" )
api_secret_filename =  os.path.join(mother_directory, 'keys', "10012(main_1)/api_secret.txt" )

with open(api_key_filename, 'r') as file:
    api_key_10012_main_1 = file.readline()

with open(api_secret_filename, 'r') as file:
    api_secret_10012_main_1 = file.readline()

client = Client(api_key_10012_main_1, api_secret_10012_main_1)
server_time = client.get_server_time()


orderbook_tickers = client.get_orderbook_tickers()
with open(os.path.join(requests_directory, 'downloads', "orderbook_history.json" ), 'w', encoding="utf-8") as file:
    json.dump(orderbook_tickers, file)

