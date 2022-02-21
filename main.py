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

    pprint(f"Getting database..."
           f"{response.text}")


if __name__ == '__main__':
    get_database(str(os.getenv('notion_database_id')))
