from pprint import pprint
import requests
import plac


def main():
    subreddit = 'r/wallstreetbets'
    name = getPopularPost(subreddit)
    print(name)
    comments = getComments(name,subreddit)
    # for c in comments:
    #     print(str(comments.index(c)) + ' ' + c)


def getPopularPost(subreddit):
    my_headers = {'User-agent' : 'MyUserAgent'}
    my_filtercriteria = {'limit':'1'}

    try:
        r = requests.get('http://www.reddit.com/'+ subreddit +'/hot/.json',headers= my_headers,params=my_filtercriteria)
        r.raise_for_status()
        
        data = r.json()

        return(data['data']['children'][0]['data']['name'])
        
    except Exception as e:
        print('Unable to get latest reddit post due to:\n' + str(e))

def getComments(fullname, subreddit):
    my_headers = {'User-agent' : 'MyUserAgent'}
    my_filtercriteria = {'article':fullname, 'limit': '10'}
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
    