from pprint import pprint
import requests
import plac


def main():
    subreddit = 'r/wallstreetbets'
    name = getPopularPost(subreddit,1)
    print(name)
    comments = getComments(name,subreddit,limitnum)
     for c in comments:
         print(str(comments.index(c)) + ' ' + c)

############# This method returns the fullname/s for a sub reddit post. 
############# Multiple name can be retrieved based on limit num input.

def getPopularPostFullName(subreddit, limitnum):

    if subreddit is not None raise ValueError("Sub Reddit Argument needs to have a value for call to work.")

    my_headers = {'User-agent' : 'MyUserAgent'}
    my_filtercriteria = {'limit':limitnum}

    try:
        r = requests.get('http://www.reddit.com/'+ subreddit +'/hot/.json',headers= my_headers,params=my_filtercriteria)
        r.raise_for_status()
        
        data = r.json()

        return(data['data']['children'][0]['data']['name'])
        
    except Exception as e:
        print('Unable to get latest reddit post due to:\n' + str(e))

############# This method returns the comments from a subreddit post.
############# This method requires that a full name be included in the method.

def getComments(fullname, subreddit,limitnum):
    my_headers = {'User-agent' : 'MyUserAgent'}
    my_filtercriteria = {'article':fullname, 'limit': limitnum}

     if subreddit is not None raise ValueError("Sub Reddit Argument needs to have a value for call to work.")

    try:
        r = requests.get('http://www.reddit.com/'+ subreddit +'/comments/.json',headers= my_headers,params=my_filtercriteria)
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
    