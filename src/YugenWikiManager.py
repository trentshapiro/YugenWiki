import json
import utils.API.Generic as api_utils
import utils.API.Yugen as yugen
import utils.API.Wiki as wiki
import utils.Templating.TemplateGenerator as TGen

ENDPOINT_MAP = {"monsters": yugen.get_monsters, "weapons": yugen.get_weapons}


def save_new_data(endpoint: str, body: dict) -> str:
    with open(f"src/data/incoming/{endpoint}.json", "w") as f:
        f.write(json.dumps(body, indent=4))


if __name__ == "__main__":
    credentials = api_utils.get_credentials("Yugen")

    # TODO:
    #   httpx calls later
    #   concurrent.futures depending on yugen allowable limits
    # save new tables (potential for sqlite, etc)
    for table in ["monsters", "weapons"]:
        api_return = ENDPOINT_MAP[table](credentials)
        print(api_return)
        save_new_data(table, api_return)

    # TODO:
    # compare to previous tables
    #  net new objects: create or insert page
    #  modified objects: create or update existing page

    # TODO:
    # For each new object:
    # generate page from a templates

    this_object = {"object_type": "monster", "object_name": "Mr.Sally's Ghost"}
    this_page_content = TGen.generate_from_template("monster", this_object)
    print(this_page_content)

    # Start fandom session
    wiki_client = wiki.get_session()

    print(wiki_client)

    # Check current page status
