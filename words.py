import requests


def format_text():

    response_API = requests.get(api)

    temp = "".join(response_API.text.split('["'))
    words = "".join(temp.split('"]'))

    return words


api = 'https://random-word-api.herokuapp.com/word'

words = format_text()

if __name__ == "__main__":
    print(words)
