import os
import requests
import json

# These are the credentials passed by the 'port' context to your environment variables
CLIENT_ID = os.environ['PORT_CLIENT_ID']
CLIENT_SECRET = os.environ['PORT_CLIENT_SECRET']
PR_REQUESTS = os.environ['PR_REQUESTS_OPEN']

credentials = {
    'clientId': CLIENT_ID,
    'clientSecret': CLIENT_SECRET
}
token_response = requests.post(f"https://api.getport.io/v1/auth/access_token", json=credentials)
access_token = token_response.json()['accessToken']

headers = {
    'Authorization': f'Bearer {access_token}'
}

entity_json = {
        "identifier": "ex2",
        "properties": {
          "pull_requests_open": PR_REQUESTS,
      }
}

# request url : {API_URL}/blueprints/<blueprint_id>/entities
create_response = requests.post(f'https://api.getport.io/v1/blueprints/repository/entities?upsert=true', json=entity_json, headers=headers)
print(json.dumps(token_response.json(), indent=4))