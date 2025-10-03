import os

MID_BRANCH = "├──"
LAST_BRANCH = "└──"
NO_BRANCH = "│"

OFFSET_STRING = ""

def main():
    path = "test_dir"

    print(path)
    dump_tree([OFFSET_STRING], path)

def dump_tree(offset_string_list, path):
    try:
        entries = list(os.scandir(path))
    except FileNotFoundError as e:
        print(f"dirtree error: {e}")
        exit(1)

    entry_len = len(entries)
    for i, entry in enumerate(entries):
        entry_name = ""
        if i == entry_len - 1:
            entry_name = f"{LAST_BRANCH} {entry.name}"
        else:
            entry_name = f"{MID_BRANCH} {entry.name}"


        if entry.is_dir():
            print("".join(offset_string_list) + entry_name)
            offset_string_list.append(f"{NO_BRANCH}   ")
            dump_tree(offset_string_list, entry.path)
            offset_string_list.pop()
        else:
            print("".join(offset_string_list) + entry_name)



if __name__ == "__main__":
    main()

