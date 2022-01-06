import requests
import json

# STRAVA Account information
STRAVA_CLIENT_ID = 123456
STRAVA_CLIENT_SECRET = 'YYYYYYYYYYYY'
STRAVA_AUTH_CODE = 'ZZZZZZZZZZZZ'

# Make Strava auth API call with your 
# client_code, client_secret and code
response = requests.post(
                    url = 'https://www.strava.com/oauth/token',
                    data = {
                            'client_id': STRAVA_CLIENT_ID,
                            'client_secret': STRAVA_CLIENT_SECRET,
                            'code': STRAVA_AUTH_CODE,
                            'grant_type': 'authorization_code'
                            }
                )
#Save json response as a variable
strava_tokens = response.json()
# Save tokens to file
with open('strava_tokens.json', 'w') as outfile:
    json.dump(strava_tokens, outfile)
# Open JSON file and print the file contents 
# to check it's worked properly
with open('strava_tokens.json') as check:
  data = json.load(check)
print(data)