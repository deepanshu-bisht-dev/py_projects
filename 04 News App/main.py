try:
    import requests
    query = input("What type of news are you interested in today?")
    api = "You can use your api key here..."  # I haven'nt used mine because you all will otherwise exhaust my quota...


    url = f"https://newsapi.org/v2/everything?q={query}&from=2026-05-24&sortBy=publishedAt&apiKey={api}"

    print(url)
    r = requests.get(url)
    data = r.json()
    articles = data["articles"]

    for index, article in enumerate(articles):
        print(index+1,article["title"],article["author"],article["url"],article["publishedAt"])
        print("\n*****************************************************************\n")

except:
    print("Enter a valid query...")