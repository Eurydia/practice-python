import pprint

seen: dict[str, list[tuple[str, str]]] = dict()

stack = ["MI"]


def main():
    while stack:
        proc = stack.pop(0)
        if proc in seen or len(proc) > 30:
            continue
        else:
            seen[proc] = list()
        if proc == "MU":
            break
        if proc.endswith("I"):
            procR = proc + "U"
            stack.append(procR)
            seen[proc].append(("I", procR))
        if proc.startswith("M"):
            procR = proc + proc[1:]
            stack.append(procR)
            seen[proc].append(("II", procR))
        if "III" in proc:
            for i, _ in enumerate(proc):
                if proc[i:].startswith("III"):
                    procR = proc[:i] + "U" + proc[i + 3 :]
                    stack.append(procR)
                    seen[proc].append(("III", procR))

        if "UU" in proc:
            for i, _ in enumerate(proc):
                if proc[i:].startswith("UU"):
                    procR = proc[:i] + proc[i + 2 :]
                    stack.append(procR)
                    seen[proc].append(("IV", procR))


if __name__ == "__main__":
    main()
    # pprint.pprint(seen)
    pprint.pprint(seen["MU"])
    # proc = "MUUUUIIIIU"
    # lastFoundUU = 0
    # countUU = proc.count("UU")
    # for i, _ in enumerate(proc):
    #     if proc[i:].startswith("UU"):
    #         print(proc[:i] + proc[i + 2 :])
