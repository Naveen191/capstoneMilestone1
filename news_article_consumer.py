from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads

consumer = KafkaConsumer('newsarticle', bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest', enable_auto_commit=True, group_id='my-group', value_deserializer=lambda x: loads(x.decode('utf-8')))
client = MongoClient("mongodb+srv://naveen:itsmenaveen@cluster0.idvt3.mongodb.net/news_articles?retryWrites=true&w=majority")
collection = client.news_articles.news_article
for message in consumer:
    message = message.value
    collection.insert_one(message)
    print('{} added to {}'.format(message, collection))
    print(message)
