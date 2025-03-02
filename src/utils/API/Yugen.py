from utils.API.Generic import get_credentials

# TODO: make into a class to handle rate limiting/concurrency/credential reading

def get_monsters(credentials: dict[str, str] = None, monster_name: str = None) -> dict[str, dict]:
    # TODO: IMPL
    if not credentials:
        credentials = get_credentials("Yugen")

    endpoint = credentials["url"] + "/monsters"

    if monster_name:
        endpoint += f"?query={monster_name}"

    return {
        "monsters": [
            {
                "name": "Mr Sally's Ghost",
                "location": "Isle of Moroha",  # fine if these are external keys instead, can do joins
                "level": 25,
                "hp": 14811,
                "ac": 375,
                "exp": 1400,
                "aggro_range": 8,
                "move_speed": 1.5,
                "damage": 152,
                "atk_speed": 1,
                "atk_range": 1,
                "is_boss": True,
                "spawn_x": 250,
                "spawn_y": 250,
                "respawn_time_sec": 900,
                "loot_table": [
                    {"name": "Skullthumper", "chance": 0.15},
                    {"name": "Quartz Staff", "chance": 0.15},
                    {"name": "Sturdy Hammer", "chance": 0.15},
                    {"name": "Reinforced Knuckle", "chance": 0.15},
                    {"name": "Poison Dagger", "chance": 0.15},
                    {"name": "Magic Moon Wand", "chance": 0.15},
                    {"name": "Distracting Lute", "chance": 0.15},
                ],
                "img_url": "https://static.wikia.nocookie.net/yugen-saga/images/c/cd/Mr_Sally%27s_Ghost.png/revision/latest?cb=20230619220840",
            },
        ]
    }


def get_weapons(credentials: dict[str, str] = None, weapon_name: str = None) -> dict[str, dict]:
    # TODO: IMPL

    if not credentials:
        credentials = get_credentials("Yugen")

    endpoint = credentials["url"] + "/weapons"

    if weapon_name:
        endpoint += f"?query={weapon_name}"

    return {
        "weapons": [
            {
                "name": "Skullthumper",
                "ac": 67,
                "req_level": 20,
                "req_class": "Warrior",
                "damage_min": 55,
                "damage_max": 75,
                "stats": {"str": 4, "sta": 3, "int": 1, "wis": 1, "dex": 2},
                "sell_value": 440,
                "image_url": "https://static.wikia.nocookie.net/yugen-saga/images/f/f3/Skullthumper.jpg/revision/latest?cb=20230224185329",
            }
        ]
    }


if __name__ == "__main__":
    print("Do not run file directly.")
