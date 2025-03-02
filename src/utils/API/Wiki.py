from utils.API.Generic import get_credentials
import httpx

# Make a Bot and password at https://yugen-saga.fandom.com/wiki/Special:BotPasswords
# It will look like username: your_name@bot_name, password: qoihrq823hrqpo2i3rhn;q2io


# TODO: make into a class to handle rate limiting/concurrency/credential reading once

def get_session() -> httpx.Client:
    creds = get_credentials("Wiki")

    url = creds['url']
    username = creds['username']
    password = creds['password']

    wiki_client = httpx.Client()

    token_response = wiki_client.get(
        url,
        params={
            "action":"query",
            "meta":"tokens",
            "type":"login",
            "format":"json"
        }
    )

    token = token_response.json()['query']['tokens']['logintoken']

    print(f"token: {token}")

    login_response = wiki_client.post(
        url,
        data={
            "action":"login",
            "lgname":username,
            "lgpassword":password,
            "lgtoken": token,
            "format":"json"
        }
    )

    print(f"login status: {login_response.json()['login']['result']}")

    return wiki_client



if __name__ == "__main__":
    print("Do not run file directly.")
