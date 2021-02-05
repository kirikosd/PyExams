import tweepy
import re

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
all_words = []
biggest = ["","","","",""]
smallest = ["","","","",""]

def tweets_pull(api,username,all_words):
    items = tweepy.Cursor(api.user_timeline, id = username , tweet_mode = "extended").items(10)
    for status in items:
        try:
            text = status.retweeted_status.full_text
        except AttributeError:  # Not a Retweet
            text = status.full_text
        print(text,"\n ---")
        text = re.sub(r'http\S+', '', text)
        text = re.sub(r'@\S+', '', text)
        text = re.sub(r'#\S+', '', text)
        text = re.sub(r' \d+', '', text)
        text = re.sub(r'[^\w\s]', '', text)
        for word in text.split():
            all_words.append(word)

def find_biggest(biggest,words):
    max1 = -1
    max2 = -1
    max3 = -1
    max4 = -1
    max5 = -1
    for word in words:
        if word in biggest:
            continue
        length = len(word)
        if length > max1 :
            biggest[0] = word
            max1 = length
        elif length > max2 :
            biggest[1] = word
            max2 = length
        elif length > max3 :
            biggest[2] = word
            max3 = length
        elif length > max4 :
            biggest[3] = word
            max4 = length
        elif length > max5 :
            biggest[4] = word
            max5 = length
    print("Top 5 biggest words are:")
    for word in biggest :
        print(word)
    print("\n")

def find_smallest(smallest,words):
    min1 = 200
    min2 = 200
    min3 = 200
    min4 = 200
    min5 = 200
    for word in words:
        if word in smallest :
            continue
        length = len(word)
        if length < min1 :
            smallest[0] = word
            min1 = length
        elif length < min2 :
            smallest[1] = word
            min2 = length
        elif length < min3 :
            smallest[2] = word
            min3 = length
        elif length < min4 :
            smallest[3] = word
            min4 = length
        elif length < min5 :
            smallest[4] = word
            min5 = length
    print("Top 5 smallest words are:")
    for word in smallest :
        print(word)
    print("\n")
        

tweets_pull(api,'user_id_here',all_words)
#print(all_words)
find_biggest(biggest,all_words)
find_smallest(smallest,all_words)
