import feedparser

CRAIGSLIST_LOCATIONS = ["aberdeen", "bath", "belfast", "birmingham", "brighton", "bristol", "cambridge", "cardiff / wales", "coventry", "derby", "devon/cornwall", "dundee", "east anglia", "east midlands", "edinburgh", "essex", "glasgow", "hampshire", "kent", "leeds", "liverpool", "london", "manchester", "newcastle", "nottingham", "oxford", "sheffield"]
CRAIGSLIST_KEYWORDS = ["magic the gathering"]

def processCraigslist(locations, keywords):
    for location in locations:
        for keyword in keywords:
            rss_url = 'https://' + location + '.craigslist.org/search/sss?format=rss&query=' + keyword.replace(" ", "%20")
            rss = feedparser.parse(rss_url)
            for entry in rss.entries:
                print entry.title_detail.value
                # add relavant details to sqlite database

if __name__ == "__main__":
    processCraigslist(CRAIGSLIST_LOCATIONS, CRAIGSLIST_KEYWORDS)
