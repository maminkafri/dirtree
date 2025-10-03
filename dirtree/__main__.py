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
            prog="dirtree",
            usage="%(prog)s [options] [dir]",
            description="display dir content in a nice tree structure"
            )
    parser.add_argument('dir', nargs="?",default=".")
    parser.add_argument('-a', '--all', action="store_true", help="Account for hidden directory (directory beginning with .)")
    args = parser.parse_args()

    print(DIR_COLOR + args.dir + ENDC)
    dir_count, file_count = dump_tree([OFFSET_STRING], args.dir, show_hidden=args.all)
    print(f"\n{dir_count + 1} directories", end=", ")
    print(f"{file_count} files")

def dump_tree(offset_string_list, path, show_hidden=False):
    dir_count = 0
    file_count = 0
    with os.scandir(path) as entries:
        if show_hidden:
            entries = list(entries)
        else:
            entries = [e for e in entries if not e.name.startswith(".")]

        # Sort: directories first, then files, alphabetical
        entries = sorted(
            entries,
            key=lambda e: (not e.is_dir(), e.name.lower())
        )
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
                dir_count = dir_count + 1
                entry_name = entry_branch + DIR_COLOR + entry.name + ENDC
                print("".join(offset_string_list) + entry_name)
                if not last_entry:
                    OFFSET_STRING = f"{NO_BRANCH}   "
                else:
                    OFFSET_STRING = "    "

                offset_string_list.append(OFFSET_STRING)
                new_dir_count, new_file_count = dump_tree(offset_string_list, entry.path)
                dir_count += new_dir_count
                file_count += new_file_count
                offset_string_list.pop()
            else:
                file_count = file_count + 1
                entry_name = entry_branch + entry.name
                print("".join(offset_string_list) + entry_name)

    return dir_count, file_count


if __name__ == "__main__":
    main()

