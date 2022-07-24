import re


def transform(input_: str) -> str:
    if not isinstance(input_, str):
        raise TypeError("Expected string parameter")

    return re.sub(
        r"[A-Za-z]",
        lambda matchobj: transform_letter(matchobj.group(0)),
        input_,
    )


def transform_letter(letter: str) -> str:
    char_code = ord(letter)
    if ("a" <= letter <= "m") or ("A" <= letter <= "M"):
        char_code += 13
    elif ("n" <= letter <= "z") or ("N" <= letter <= "Z"):
        char_code -= 13
    return chr(char_code)
