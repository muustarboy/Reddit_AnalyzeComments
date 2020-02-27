import categories
import rcomments
import spacy

spacy.load('en_core_web_sm')


subreddit = "r\WallStreetBets"
category = categories.Category.Hot.name


name = rcomments.getPostFullName(name,category,1)
comments = rcomments.getComments(name,subreddit,50)



