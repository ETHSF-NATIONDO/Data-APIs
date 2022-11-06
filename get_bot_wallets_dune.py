from dune_query_utils import execute_query_with_params, get_query_status, get_query_results
import pandas as pd
import time

onchain_bot_wallets_query_id = '1534649'

def retrieve_bot_wallets_data(dune_query_id, save_json=True):
    execution_id = execute_query_with_params(dune_query_id, param_dict = {'Bot Threshold - Txs per Hour': 50})
    data = None
    while data is None:
        status_response = get_query_status(execution_id)
        if status_response.json()['state'] == 'QUERY_STATE_COMPLETED':
            query_result = get_query_results(dune_query_id)
            data = pd.DataFrame(query_result.json()['result']['rows'])
        time.wait(15)
    if save_json:
        data.to_json('bot_wallets_data.json', orient='table', indent=4)
    return data