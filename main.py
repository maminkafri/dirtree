import os

MID_BRANCH = "├──"
LAST_BRANCH = "└──"
NO_BRANCH = "│"

DIR_COLOR = "\033[94m"
ENDC = "\033[0m"

OFFSET_STRING = ""

def main():
    path = "test_dir"

    print(DIR_COLOR + path + ENDC)
    dump_tree([OFFSET_STRING], path)

def dump_tree(offset_string_list, path):
    try:
        entries = list(os.scandir(path))
    except FileNotFoundError as e:
        print(f"dirtree error: {e}")
        exit(1)

    entry_len = len(entries)
    for i, entry in enumerate(entries):
        entry_branch = ""
        if i == entry_len - 1:
            entry_branch = f"{LAST_BRANCH} "
        else:
            entry_branch = f"{MID_BRANCH} "


        entry_name = ""
        if entry.is_dir():
            entry_name = entry_branch + DIR_COLOR + entry.name + ENDC
            print("".join(offset_string_list) + entry_name)
            OFFSET_STRING = f"{NO_BRANCH}   "
            offset_string_list.append(OFFSET_STRING)
            dump_tree(offset_string_list, entry.path)
            offset_string_list.pop()
        else:
            entry_name = entry_branch + entry.name
            print("".join(offset_string_list) + entry_name)



if __name__ == "__main__":
    main()

