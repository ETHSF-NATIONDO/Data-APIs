from requests import get, post
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv() 

BASE_URL = "https://api.dune.com/api/v1/"
DUNE_API_KEY = os.environ['DUNE_API_KEY']
HEADER = {"x-dune-api-key" : DUNE_API_KEY}

def make_api_url(module, action, ID):
    """
    We shall use this function to generate a URL to call the API.
    """
    url = BASE_URL + module + "/" + ID + "/" + action
    return url

def execute_query(query_id):
    """
    Takes in the query ID.
    Calls the API to execute the query.
    Returns the execution ID of the instance which is executing the query.
    """

    url = make_api_url("query", "execute", query_id)
    response = post(url, headers=HEADER)
    execution_id = response.json()['execution_id']

    return execution_id


def get_query_status(execution_id):
    """
    Takes in an execution ID.
    Fetches the status of query execution using the API
    Returns the status response object
    """

    url = make_api_url("execution", "status", execution_id)
    response = get(url, headers=HEADER)

    return response


def get_query_results(execution_id):
    """
    Takes in an execution ID.
    Fetches the results returned from the query using the API
    Returns the results response object
    """

    url = make_api_url("execution", "results", execution_id)
    response = get(url, headers=HEADER)

    return response


def cancel_query_execution(execution_id):
    """
    Takes in an execution ID.
    Cancels the ongoing execution of the query.
    Returns the response object.
    """

    url = make_api_url("execution", "cancel", execution_id)
    response = get(url, headers=HEADER)

    return response

def execute_query_with_params(query_id, param_dict):
    """
    Takes in the query ID. And a dictionary containing parameter values.
    Calls the API to execute the query.
    Returns the execution ID of the instance which is executing the query.
    """

    url = make_api_url("query", "execute", query_id)
    response = post(url, headers=HEADER, json={"query_parameters" : param_dict})
    execution_id = response.json()['execution_id']

    return execution_id