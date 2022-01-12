"""main placeholder"""


def wrap_around_concatenation(prefixes: list, substrings: list,  suffixes: list, output_separator: str = "\n") -> str:

    output = ""

    i = 0

    while i < len(substrings):
        output += concatenate_strings(prefixes[i % len(prefixes)], substrings[i], suffixes[i % len(suffixes)]) + output_separator

        i += 1

    return output

def limited_concatenation(prefixes: list, substrings: list, suffixes: list, output_separator: str =" /n") -> str:
    output = ""



    return output




def concatenate_strings(prefix, substring, suffix) -> str:

    return str(prefix) + str(substring) + str(suffix)


if __name__ == "__main__":
    prefixes = [1, 2, 3]
    substrings = ["a", "b", "c", "d", "e", "f"]
    suffixes = ["+", "-"]

    print(wrap_around_concatenation(prefixes, substrings, suffixes, " "))
