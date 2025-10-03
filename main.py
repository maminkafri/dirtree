import os

def main():
    path = "."

    try:
        dircontent = os.scandir(path)
    except FileNotFoundError as e:
        print(f"dirtree error: {e}")

    for i in dircontent:
        print(i.path)
        print(i.is_dir())


if __name__ == "__main__":
    main()

