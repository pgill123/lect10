# This is the simplified version. Only represents Step 4 if the account is public

from requests_oauthlib import OAuth1Session
import secrets
import json

client_key = secrets.client_key
client_secret = secrets.client_secret

resource_owner_key = secrets.access_token
resource_owner_secret = secrets.access_token_secret

protected_url = 'https://api.twitter.com/1.1/account/settings.json'

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food'}
get_twitter_data = oauth.get(protected_url, params=params)
# print(get_twitter_data.text)
dict_twitter = json.loads(get_twitter_data.text)
print(dict_twitter)
# print("**twitter dumps***\n",json.dumps(dict_twitter, indent=4))

for i in dict_twitter["statuses"]:
    print(i["user"]["screen_name"] +":" + i["user"]["description"] )

# f = open("lect6.json", 'w')
# f.write(json.dumps(dict_twitter))
# f.close()
