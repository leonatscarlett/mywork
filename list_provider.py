WAKING = "waking"
LOL = "lol"
SOCIAL = "social"
PERSONAL = "personal"
BNM = "bnm"
PIDOR = "pidor"


def read_file(file_name):
    lines = []
    with open(f"dict/{file_name}") as file:
        for line in file:
            lines.append(line.strip())
    return lines


def get_keywords(key):
    return read_file(f"{key}_keywords")


def get_lines(key):
    return read_file(f"{key}_lines")


def get_idle():
    return read_file("idle_lines")


def get_known_nicknames():
    return read_file("known_nicknames")


def get_lines_dict():
    return {
        WAKING: get_lines(WAKING),
        LOL: get_lines(LOL),
        SOCIAL: get_lines(SOCIAL),
        PERSONAL: get_lines(PERSONAL),
        BNM: get_lines(BNM),
        PIDOR: get_lines(PIDOR)
    }


def get_keywords_dict():
    return {
        WAKING: get_keywords(WAKING),
        LOL: get_keywords(LOL),
        SOCIAL: get_keywords(SOCIAL),
        PERSONAL: get_keywords(PERSONAL),
        BNM: get_keywords(BNM),
        PIDOR: get_keywords(PIDOR)
    }

