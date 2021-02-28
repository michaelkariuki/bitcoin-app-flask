from app import app
from flask import render_template
import requests
from requests.exceptions import HTTPError
from app.misc.keys import API_KEY



def get_data(url):
    try:
        response  = requests.get(url)
        response.raise_for_status() # If the response was successful, no Exception will be raised
    except HTTPError as e:
        print(f'HTTP error occurred: {e}')
        response = "Error occurred"
    except Exception as e:
        print(f'Other error occurred: {e}')
        response = "Error occurred"
    else:
        print('success!')
    finally:
        return response

@app.route('/')
@app.route('/index')
def index():
    url = f'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR,GPB,USDC&api_key={API_KEY} '
    message = "BITCOIN TRACKER"
    response = get_data(url)

    return render_template('index.jinja', title="Home", data=response.json(), msg=message)