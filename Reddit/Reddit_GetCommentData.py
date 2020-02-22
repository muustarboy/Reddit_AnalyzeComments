from pprint import pprint
import requests
import plac


def main(): 
    fullname = getPostFullName(subreddit="r/wallstreetbets",category="hot",limitnum=1)
    comments = getComments(fullname,subreddit="r/wallstreetbets",limitnum)
    for c in comments:
        print(str(comments.index(c)) + ' | ' + c)



# This method returns the fullname/s for a sub reddit post. 
# Category determines which grouping of posts to return, optionally
# you can specify a limit of items returned.

def getPostFullName(subreddit, category, limitnum):

    if subreddit is None:
        raise ValueError("Sub Reddit Argument is null and needs to have a value for call to work.")

    my_headers = {'User-agent' : 'MyUserAgent'}
    my_filtercriteria = {'limit':limitnum}

    baseURI  = "http://www.reddit.com/"
    endpoint = subreddit +'/'+ category +'/.json'
    url = baseURI + endpoint

    try:
        r = requests.get(url,headers= my_headers,params=my_filtercriteria)
        r.raise_for_status()
        
        data = r.json()

        return(data['data']['children'][0]['data']['name'])
        
    except Exception as e:
        print('Unable to get latest reddit post due to:\n' + str(e))




#  This method returns the comments from a subreddit post.
#  It requires that a full name be included in the method,
#  optionally you can specify a limit of items returned.

def getComments(fullname, subreddit, limitnum):
    my_headers = {'User-agent' : 'MyUserAgent'}
    my_filtercriteria = {'article':fullname, 'limit': limitnum}

    if subreddit is None:
        raise ValueError("FullName/SubReddit Argument is null and needs to have a value for call to work.")

    baseURI  = "http://www.reddit.com/"
    endpoint = subreddit +"/comments/.json"
    url = baseURI + endpoint

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
    

