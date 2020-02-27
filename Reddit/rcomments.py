from pprint import pprint
import requests
import plac


def main(): 
    fname = getPostFullName(subreddit="r/wallstreetbets",category="hot",limitnum=1)
    comments = getComments(fullname=fname,subreddit="r/wallstreetbets",limitnum=100)
    for c in comments:
        print(str(comments.index(c) + 1) + ' | ' + c)



# This method returns the fullname/s for a sub reddit post. 
# Category determines which grouping of posts to return, optionally
# you can specify a limit of items returned.

def getPostFullName(subreddit: str, category: str, limitnum: int):

    if limitnum is None:
        limitnum=1

    my_headers = {'User-agent' : 'MyUserAgent'}
    my_filtercriteria = {'limit':limitnum}

    url = f"http://www.reddit.com/{subreddit}/{category}/.json"

    try:
        r = requests.get(url,headers= my_headers,params=my_filtercriteria)
        r.raise_for_status()
        data = r.json()

        return(data['data']['children'][0]['data']['name'])
        
    except Exception as e:
        print('Unable to get latest reddit post due to:\n' + str(e))


#  This method returns comments as a list from a subreddit post.
#  It requires that a full name be included in the method,
#  optionally you can specify a limit of items returned.

def getComments(fullname: str, subreddit: str, limitnum: int):
    
    if limitnum is None:
        limitnum=1

    my_headers = {'User-agent' : 'MyUserAgent'}
    my_filtercriteria = {'article':fullname, 'limit': limitnum}

    url = f"http://www.reddit.com/{subreddit}/comments/.json"

    try:
        r = requests.get(url,headers= my_headers,params=my_filtercriteria)
        r.raise_for_status()
        
        data = r.json()
        comments = []
        for child in data['data']['children']:
            comments.append(str(child['data']['body']))

        return comments
        
        
    except Exception as e:
        print('Unable to get sub reddit comments due to:\n' + str(e))


if __name__ == "__main__":
    plac.call(main)
    

