import typing
from typing import List


class SCPage:
    def __init__(self, name: str):
        self.name = name
        self.content = None
        self.frozenLeft = 0
        self.referenced = False

    def replace_to(self, content: int):
        self.content = content
        self.frozenLeft = 3 + 1
        self.referenced = False

    def __str__(self):
        return self.name


def solution(refs: List[int]) -> [str, int]:
    allocations = ""
    page_faults = 0

    A = SCPage("A")
    B = SCPage("B")
    C = SCPage("C")

    pages_fifo = [A, B, C]

    move_to_end_of_fifo = lambda p: pages_fifo.remove(p) or pages_fifo.append(p)

    for ref in refs:
        r = abs(ref)

        # decrement frozenLeft
        for p in pages_fifo:
            if p.frozenLeft > 0:
                p.frozenLeft -= 1

        # check if page is already in memory
        for p in pages_fifo:
            if p.content == r:
                p.referenced = True
                p.frozenLeft = 0
                allocations += "-"
                break

        # if not, replace one that is not frozen (preferably not referenced either)
        else:
            i = 0
            while i < len(pages_fifo):
                p = pages_fifo[i]
                if p.frozenLeft <= 0:
                    if p.referenced:    # if referenced, give it a Second Chance™️
                        p.referenced = False
                        move_to_end_of_fifo(p)
                        continue
                    p.replace_to(r)
                    move_to_end_of_fifo(p)
                    allocations += f"{p.name}"
                    page_faults += 1
                    break
                i += 1

            # if all pages are frozen, give up
            else:
                allocations += "*"
                page_faults += 1

    return allocations, page_faults


def get_stdin_and_parse() -> List[int]:
    raw_in = input().strip()
    refs = []
    try:
        while True:
            raw_in = raw_in.strip()
            if raw_in == "":
                continue
            for n in raw_in.split(","):
                refs.append(int(n))
            raw_in = input()
            if raw_in == "end":
                break
    except EOFError:
        pass
    return refs


def main():
    pagerefs = get_stdin_and_parse()
    allocated, faults = solution(pagerefs)
    print(f"{allocated}\n{faults}")


if __name__ == '__main__':
    main()
