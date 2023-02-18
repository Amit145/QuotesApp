# Imports
import json
import os
from datetime import datetime
from typing import Optional
import pymongo
from fastapi import Request, FastAPI
import socket
from pydantic import BaseModel
from pymongo import MongoClient
from AWS.uploadToS3 import AWSOperations
from imageCreator import createImage

# Instantiate instance of FastAPI
api = FastAPI()

# MongoDB database connection
mongoClient = MongoClient('mongodb://localhost:27017')
db = mongoClient.QuotesDB
collection = db["Quotes"]


# QuoteData Model
class Quote(BaseModel):
    quote: str
    author: Optional[str] = ""
    tags: Optional[list] = []
    likes: Optional[int] = 0
    views: Optional[int] = 0
    shares: Optional[int] = 0
    creation_date: Optional[str] = ""
    id: Optional[int] = 0


# Functions
def get_instance_id():
    return socket.gethostname()


def get_latest_id():
    quote_id = 0
    cursor = collection.find({}, sort=[('_id', pymongo)]).limit(1)
    for document in cursor: quote_id = document['id'] + 1
    return quote_id


# Routes
@api.get('/')
async def get_server_root():
    return f'System is working fine! Instance Id {get_instance_id()}'


@api.get('/quote/viewAll')
async def get_all_quotes():
    items = []
    result = collection.find({})
    for document in result:
        document.pop('_id')
        items.append(document)
    return items


@api.get('/quote/view/{quote_id}')
async def get_quote(quote_id: int):
    cursor = collection.find_one({'id': quote_id})
    if cursor:
        cursor.pop('_id')
        return cursor
    else:
        return []


@api.post('/quote/add')
async def add_quote(quote: Quote):
    quote_id = get_latest_id()
    quote.id = quote_id
    quote.creation_date = datetime.now().strftime('%d-%m-%Y-%H:%M:%S.%f')
    json_quote = json.loads(quote.json())
    collection.insert_one(json_quote)
    return quote


# Update only certain fields and not all
@api.put('/quote/update/{quote_id}')
async def update_quote(quote_id: int, request: Request):
    request = await request.json()
    result = collection.find_one({
        'id': quote_id
    })

    if result:
        result_keys = result.keys()
        request_keys = request.keys()

        for key in request_keys:
            if key in result_keys:
                result.pop('_id')
                # updated = {"$set": {}}
                updated = {"$set": request}
                op = collection.update_one(result, updated)
                if op.matched_count == 1:
                    return updated
            else:
                return f'Error no field found {key}'
    else:
        return []


@api.delete('/quote/delete/{quote_id}')
async def delete_quote(quote_id: int):
    result = collection.find_one({'id': quote_id})
    if result:
        collection.delete_one({'id': quote_id})
        return f'Deleted! {quote_id}'
    else:
        return []


@api.put('/quote/update/{quote_id}/view')
async def update_quote_views(quote_id: int):
    result = collection.find_one({'id': quote_id})
    if result:
        result.pop('_id')
        updated = {"$set": {'views': result['views'] + 1}}
        op = collection.update_one(result, updated)
        if op.matched_count == 1:
            return updated
        return f'Error updating {quote_id}'
    else:
        return f'Not found {quote_id}'


@api.put('/quote/update/{quote_id}/like')
async def update_quote_likes(quote_id: int):
    result = collection.find_one({
        'id': quote_id
    })

    if result:
        result.pop('_id')
        update = {"$set": {
            'likes': (result['likes']) + 1
        }}

        op = collection.update_one(result, update)
        if op.matched_count == 1:
            return update
        else:
            return f'Error updating {quote_id}'
    else:
        return f'Not found {quote_id}'


@api.put('/quote/update/{quote_id}/share')
async def update_quote_shares(quote_id: int):
    result = collection.find_one({'id': quote_id})
    if result:
        result.pop('_id')
        update = {"$set": {'shares': result['shares'] + 1}}
        op = collection.update_one(result, update)
        if op.matched_count == 1:
            return update
        else:
            return f'Error updating: {quote_id}'
    else:
        return f'Not found {quote_id}'


@api.get('/quote/image/{quote_id}')
async def get_quote_image(quote_id: int):
    result = collection.find_one({'id': quote_id})
    if result:
        path, image_name = createImage.create_image(result['quote'])
        obj = AWSOperations()
        file_key = obj.upload_file(path, image_name)
        if file_key:
            if os.path.exists(path):
                os.remove(path)
            else:
                print("The file does not exist")
            url = obj.get_presigned_url_for_file(file_key)
            return url
    else:
        return []
