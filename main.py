import argparse
import os

MID_BRANCH = "├──"
LAST_BRANCH = "└──"
NO_BRANCH = "│"

DIR_COLOR = "\033[94m"
ENDC = "\033[0m"

OFFSET_STRING = ""

def main():
    parser = argparse.ArgumentParser(
            prog="my_tree",
            usage="%(prog)s [dir]",
            description="display dir content in a nice tree structure"
            )
    parser.add_argument('dir', nargs="?",default=".")
    args = parser.parse_args()

    print(DIR_COLOR + args.dir + ENDC)
    dump_tree([OFFSET_STRING], args.dir)

def dump_tree(offset_string_list, path):
    try:
        entries = list(os.scandir(path))
    except FileNotFoundError as e:
        print(f"dirtree error: {e}")
        exit(1)

    entry_len = len(entries)
    for i, entry in enumerate(entries):
        entry_branch = ""
        last_entry = i == entry_len - 1
        if last_entry:
            entry_branch = f"{LAST_BRANCH} "
        else:
            entry_branch = f"{MID_BRANCH} "


        entry_name = ""
        if entry.is_dir():
            entry_name = entry_branch + DIR_COLOR + entry.name + ENDC
            print("".join(offset_string_list) + entry_name)
            if not last_entry:
                OFFSET_STRING = f"{NO_BRANCH}   "
            else:
                OFFSET_STRING = "    "

            offset_string_list.append(OFFSET_STRING)
            dump_tree(offset_string_list, entry.path)
            offset_string_list.pop()
        else:
            entry_name = entry_branch + entry.name
            print("".join(offset_string_list) + entry_name)



if __name__ == "__main__":
    main()

