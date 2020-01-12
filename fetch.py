import json
import twitter
import requests
import shutil

with open("creds.json", "r") as file:
    creds = json.load(file)

api = twitter.Api(
    consumer_key=creds['CONSUMER_KEY'],
    consumer_secret=creds['CONSUMER_SECRET'],
    access_token_key=creds['ACCESS_TOKEN'],
    access_token_secret=creds['ACCESS_SECRET'],
)

try:
    verify = api.VerifyCredentials()
    print("Authenticated id =", verify.id)
except:
    print('Auth error')
    exit(1)

user = api.GetUser(screen_name='NomesGarcom')
total = user.statuses_count
print('Total tweets on account =', total)

tweets = api.GetUserTimeline(screen_name='NomesGarcom', count=200)
remaining = total - 200

while remaining > 0:
    lastId = tweets[-1].id
    moreTweets = api.GetUserTimeline(
        screen_name='NomesGarcom', count=200, max_id=lastId-1)
    for t in moreTweets:
        tweets.append(t)
    remaining -= 200

print("Total tweets to process = ", len(tweets))

c = 0
for t in tweets:
    c += 1
    print("Fetching media {} of {}".format(c, total))

    try:
        tweet = api.GetStatus(status_id=t.id)
        url = tweet.media[0].media_url

        splitted = url.split("/")
        local_filename = 'images/{}'.format(splitted[len(splitted)-1])

        print("Downloading {} from {}".format(local_filename, url))

        resp = requests.get(url, stream=True)
        local_file = open(local_filename, 'wb')
        resp.raw.decode_content = True
        shutil.copyfileobj(resp.raw, local_file)

        print("Media {} ok!".format(c))

    except:
        print("Media {} failed!".format(c))
