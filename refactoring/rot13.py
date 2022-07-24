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
    assert re.match(
        r"[A-Za-z]", letter
    ), f"specify a letter in A-Za-z: {letter}"

    rotation = 13 if letter.upper() <= "M" else -13
    return chr(ord(letter) + rotation)
