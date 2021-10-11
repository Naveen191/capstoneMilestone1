from api_request import free_news_api_request
import schedule
import time
queryStringsList = ["Elon Musk","Bitcoin", "Rohit Sharma", "Harry Potter", "Egyptian Pyramids", "Covid", "Fifa", "Donald Trump", "Engineering", "Bank Robbery"]
for i in queryStringsList:
    free_news_api_request(i)
    time.sleep(60)
