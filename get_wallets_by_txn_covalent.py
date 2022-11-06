import requests
import os
from dotenv import load_dotenv
import argparse
import json

load_dotenv()  # take environment variables from .env.

COVALENT_API = os.environ['COVALENT_API_KEY']
BASE_URL = 'https://api.covalenthq.com/v1'

def get_connected_wallet_addres(address, save_json = True):
    endpoint = f'/1/address/{address}/transactions_v2/?key={COVALENT_API}'
    url = BASE_URL + endpoint
    result = requests.get(url).json()
    data = result["data"]
    from_addresses = set([d.get('from_address', '') for d in data['items']]) 
    to_addresses =  set([d.get('to_address', '') for d in data['items']])
    all_connected_addresses = from_addresses.union(to_addresses)
    if address in all_connected_addresses:
        all_connected_addresses.remove(address)
    all_connected_addresses = list(all_connected_addresses)

    if save_json:
        with open('connected_wallet_data.json', 'w', encoding='utf-8') as f:
            json.dump({'connected_addresses': all_connected_addresses}, f, ensure_ascii=False, indent=4)
    return all_connected_addresses


parser = argparse.ArgumentParser(description='Get the connected addresses from wallet')
parser.add_argument('--wallet', required=True, help='wallet address')
parser.add_argument('--save_json', required=False, default=True, help='wallet address')

if __name__ == '__main__':
    args = parser.parse_args()
    get_connected_wallet_addres(args.wallet, args.save_json)
