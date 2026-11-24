import os

HAIKU = (
    "Breakpoint holds its breath\n"
    "the log swears that nothing's wrong\n"
    "the bug grins at me\n"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
