#! nlpenv\Scripts\python.exe

# https://realpython.com/python-command-line-arguments/
# https://realpython.com/working-with-files-in-python/

from sys import argv, exit


def main() -> None:

    intro()


def intro() -> None:
    usage = f"Usage: {argv[0]} [6-digit case number]"

    try:
        arg = argv[1]
    except IndexError:
        raise SystemExit(usage)

    if len(arg) != 6:
        exit(usage)


if __name__ == "__main__":
    main()
