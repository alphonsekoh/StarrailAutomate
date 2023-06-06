import requests
import os

API = "https://sg-public-api.hoyolab.com/event/luna/os/sign?lang=en-us&act_id=e202303301540311"
# Please check your cookies setting to change this. 
LTUID = os.environ['LTUID']
LTOKEN = os.environ['LTOKEN']

def main():
    cookies = {
        'ltoken': f'{LTOKEN}',
        'ltuid': f'{LTUID}'
    }
    try:
        response = requests.post(API, cookies=cookies)
        response.raise_for_status()
        response_message = response.json()
        if response_message['retcode'] == 0 and response_message['message'] == 'OK':
            print("Honkai Star Rail Daily Check-in SUCCESS")
        elif response_message['retcode'] == -5003:
            print(response_message['message'])
        else:
            print("Please check your LTUID and LTOKEN")
    except requests.exceptions.RequestException as e:
        print("Request Error occured ", e)

if __name__ == "__main__":
    main()