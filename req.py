import os
import requests
import json

# These are the credentials passed by the 'port' context to your environment variables
CLIENT_ID = os.environ['PORT_CLIENT_ID']
CLIENT_SECRET = os.environ['PORT_CLIENT_SECRET']

credentials = {
    'clientId': CLIENT_ID,
    'clientSecret': CLIENT_SECRET
}
token_response = requests.post(f"{API_URL}/auth/access_token", json=credentials)
access_token = token_response.json()['accessToken']

headers = {
    'Authorization': f'Bearer {access_token}'
}

entity_json = {
        "identifier": "ex2",
        "properties": {
          "pull_requests_open": 1,
      }
}

# request url : {API_URL}/blueprints/<blueprint_id>/entities
create_response = requests.post(f'{API_URL}/blueprints/repository/entities?upsert=true', json=entity_json, headers=headers)
print(json.dumps(get_response.json(), indent=4))