import json
import argparse
import requests


# https://newsapi.org/register
API_KEY = ""


def search(keyword):
    url = f"http://newsapi.org/v2/everything?q={keyword}&sortBy=publishedAt&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data


def save_file():
    parser = argparse.ArgumentParser()
    parser.add_argument("query")
    args = parser.parse_args()

    with open("result.json", "w") as fp:
        result = search(args.query)
        fp.write(json.dumps(result))


if __name__ == "__main__":
    save_file()
