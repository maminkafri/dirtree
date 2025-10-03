import os

OFFSET_STRING = " "

def main():
    path = "test_dir"

    print(path)
    dump_tree([OFFSET_STRING], path)

def dump_tree(tabs, path):
    try:
        entries = os.scandir(path)
    except FileNotFoundError as e:
        print(f"dirtree error: {e}")
        exit(1)

    for entry in entries:
        if entry.is_dir():
            print("".join(tabs), "-", entry.name)
            tabs.append(OFFSET_STRING)
            dump_tree(tabs, entry.path)
            tabs.pop()
        else:
            print("".join(tabs), "-", entry.name)



if __name__ == "__main__":
    main()

