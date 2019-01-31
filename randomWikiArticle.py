import wikipedia
import json
from urllib import request, error
import webbrowser
import time

# -- Retrieves random wiki article json  and converts data to a dict --

def retrieveArticle():
    url = "https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json"
    req = request.Request(url)
    resp = request.urlopen(req)
    articleJson = resp.read().decode("utf-8")
    articleJsonDict = json.loads(articleJson)
    return articleJsonDict

# --------------------------------------------------------------------
# -- Function to allow of input of y/n to view an article in browser

def openLink(articleData):
    repeat = "yes"
    while repeat == "yes":
        openLink = input("Would you like to view:" + articleData["title"] + " y/n")
        if openLink == "y":
            print("opening link code")
            time.sleep(0.5)
            articleId = articleData["id"]
            url = "http://en.wikipedia.org/wiki?curid=" + str(articleId)
            webbrowser.open(url, new=0)
            repeat = "no"
        elif openLink == "n":
            print("retrieving next article")
            time.sleep(0.5)
            repeat = "no"
        elif openLink == "q":
            quit()
        else:
            print("invalid input please try again")
            time.sleep(0.5)

# ------------------------------------------------------------------
# -- Function iterates though all 10 randomly generated articles --

def viewArticle(articleJsonDict):
    currentIndex = 0
    while currentIndex <= 9:
        articleData = articleJsonDict["query"]["random"][currentIndex]
        openLink(articleData)
        currentIndex += 1
    if currentIndex == 10:
        print("Finding more articles")
        articleJsonDict = retrieveArticle()
        currentIndex = 0
        viewArticle(articleJsonDict)

# -- Function to run to find random article for user

def randomArticle():
    print("Welcome to the random wiki article finder, Lets get started!! \nUse 'y' if you would like to view the "
          "article or 'n' if you would like to skip to the next one or 'q' to end the program")
    time.sleep(1)
    print("Retrieving your first article")
    viewArticle(retrieveArticle())






randomArticle()
