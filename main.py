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
                    "content": 'vinyls'
                }
            }
        ],
        # set up the database columns
        "properties": {
            "album_id": {
                "number": {}
                    },
            "title": {
                "text": {}
                },
            "artist_name": {
                "text": {}
                },
            "artist_id": {
                "number": {}
            },
            "discogs_id": {
                "number": {}
            },
            "barcode": {
                "number": {}
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
