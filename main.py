import os
import requests
from pprint import pprint


def get_database(database_id):
    url = "https://api.notion.com/v1/databases/" +database_id

    headers = {
        "Accept": "application/json",
        "Notion-Version": "2021-08-16",
        "Authorization": "Bearer " + str(os.getenv('notion_key'))
    }

    response = requests.request("GET", url, headers=headers)

    pprint({response.text})


def create_database():
    import requests

    url = "https://api.notion.com/v1/databases"

    payload = {
        "parent": {
            "type": "page_id",
            "page_id": os.getenv("notion_vinyls")
        },
        "title": [
            {
                "type": "text",
                "text": {
                    "content": "vinyls!"
                }
            }
        ],
        # set up the database columns
        "properties": {
        "album_id": {
            "id": "0v;b",
            "name": "album_id",
            "type": "number",
            "number": {
                "format": "number"
            }
        },
        "title": {
            "id": "title",
            "name": "title",
            "type": "title",
            "title": {}
        },
        "artist_name": {
            "id": "{v`m",
            "name": "artist_name",
            "type": "rich_text",
            "rich_text": {}
        },
        "artist_id": {
            "id": "3kfb",
            "name": "artist_id",
            "type": "number",
            "number": {
                "format": "number"
            }
        },
        "discogs_id": {
            "id": "s;30f",
            "name": "discogs_id",
            "type": "number",
            "number": {
                "format": "number"
            }
        },
        "barcode": {
            "id": "s;50f",
            "name": "barcode",
            "type": "number",
            "number": {
                "format": "number"
            }
        }
    }
    }
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2021-08-16",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + str(os.getenv('notion_key'))
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    print(response.text)


if __name__ == '__main__':
    #get_database(str(os.getenv('notion_database_id')))
    create_database()
