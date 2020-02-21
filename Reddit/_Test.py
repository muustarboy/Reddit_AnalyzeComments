from pprint import pprint
import requests


my_headers = {'User-agent' : 'MyUserAgent'}
my_filtercriteria = {'limit':'1'}

try:
    r = requests.get('http://www.reddit.com/r/WallStreetBets/hot/.json',headers= my_headers,params=my_filtercriteria)
    r.raise_for_status()
        
    pprint(r.json()) 
except Exception as e:
    print(str(e))


