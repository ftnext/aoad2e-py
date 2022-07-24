def transform(input_: str) -> str:
    if not isinstance(input_, str):
        raise TypeError("Expected string parameter")

    result = ""
    for character in input_:
        char_code = ord(character)
        result += transform_letter(character, char_code)
    return result


def transform_letter(letter: str, char_code: int) -> str:
    if is_between(letter, char_code, "a", "m") or is_between(
        letter, char_code, "A", "M"
    ):
        char_code += 13
    elif is_between(letter, char_code, "n", "z") or is_between(
        letter, char_code, "N", "Z"
    ):
        char_code -= 13
    return chr(char_code)


def is_between(
    letter: str, char_code: int, first_letter: str, last_letter: str
) -> bool:
    return letter >= first_letter and letter <= last_letter
