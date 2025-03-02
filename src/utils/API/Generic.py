import json


def get_credentials(connection_name: str) -> dict[str, str]:
    with open("src/utils/API/config.json") as f:
        conn = json.loads(f.read())[connection_name]
    return conn


if __name__ == "__main__":
    print("Do not run file directly.")
