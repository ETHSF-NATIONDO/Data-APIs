from dune_query_utils import execute_query, get_query_status, get_query_results
import pandas as pd
import time

onchain_bad_actors_query_id = '1531478'

def retrieve_bad_actors_data(dune_query_id, save_json=True):
    execution_id = execute_query(dune_query_id)
    data = None
    while data is None:
        status_response = get_query_status(execution_id)
        if status_response.json()['state'] == 'QUERY_STATE_COMPLETED':
            query_result = get_query_results(dune_query_id)
            data = pd.DataFrame(query_result.json()['result']['rows'])
        time.wait(15)
    if save_json:
        data.to_json('bad_actors_data.json', orient='table', indent=4)
    return data


if __name__ == '__main__':
    retrieve_bad_actors_data(onchain_bad_actors_query_id) 