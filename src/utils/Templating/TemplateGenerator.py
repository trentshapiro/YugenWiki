def generate_monster_template(monster_definition: dict) -> str:
    # TODO: IMPL

    with open("src/utils/Templating/templates/monster.txt") as f:
        template = f.read()

    return template


def generate_from_template(object_type: str, object_definition: dict) -> str:
    template_mapping = {
        "monster": generate_monster_template,
    }

    if object_type not in template_mapping.keys():
        raise NotImplementedError("Not yet.")

    return template_mapping[object_type](object_definition)


if __name__ == "__main__":
    print("Do not run file directly.")
