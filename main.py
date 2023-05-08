import typing
from typing import List


def get_stdin_and_parse() -> List[int]:
    raw_in = input().strip()
    refs = []
    while raw_in != 'EOF':
        if raw_in == "":
            continue
        for n in raw_in.split(","):
            refs.append(int(n))
        raw_in = input().strip()
    return refs


def main():
    pagerefs = get_stdin_and_parse()


if __name__ == '__main__':
    main()

