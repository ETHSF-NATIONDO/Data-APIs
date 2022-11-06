import requests
import os
from dotenv import load_dotenv
import argparse
import json

load_dotenv()  # take environment variables from .env.

COVALENT_API = os.environ['COVALENT_API_KEY']
BASE_URL = 'https://api.covalenthq.com/v1'

def get_nfts_in_wallet(address):
    endpoint = f'/1/address/{address}/balances_v2/?key={COVALENT_API}?nft=true'
    url = BASE_URL + endpoint
    result = requests.get(url).json()
    data = result["data"]
    nft_data = data['items'].get('nft_data')
    return nft_data