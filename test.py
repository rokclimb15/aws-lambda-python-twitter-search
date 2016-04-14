from twitter import *

def handler(event, context):
    t = Twitter(
    auth=OAuth(token, token_key, con_secret, con_secret_key))

    topic = event.get("topic", "#pycon")
    count = event.get("count", "30")

    # Search for the latest tweets about #pycon
    tweets = t.search.tweets(q=topic,count=count)

    response = 'Found %d tweets about %s in %s seconds' % (tweets['search_metadata']['count'], topic, tweets['search_metadata']['completed_in'])

    return '{"message": "%s"}' % response
