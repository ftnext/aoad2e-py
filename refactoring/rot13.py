def transform(input_: str) -> str:
    result = ""
    for character in input_:
        char_code = ord(character)
        result += transform_letter(char_code)
    return result


def transform_letter(char_code: int) -> str:
    if is_between(char_code, "a", "m"):
        char_code += 13
    elif is_between(char_code, "n", "z"):
        char_code -= 13
    return chr(char_code)


def is_between(char_code: int, first_letter: str, last_letter: str) -> bool:
    return char_code >= code_for(first_letter) and char_code <= code_for(
        last_letter
    )


def code_for(letter: str) -> int:
    return ord(letter)
