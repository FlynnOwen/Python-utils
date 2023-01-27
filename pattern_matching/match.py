"""
Using structural pattern matching (introduced Python 3.10) - essentially switch statements for Python
"""


def run_command(command: str) -> int:
    match command:
        case "multiply":
            print("multiplying...")

        case "add":
            print("adding...")

        case other:
            print(f"Unknown command {other}!")


def main() -> None:
    command = input("Command: ")
    run_command(command)


if __name__ == '__main__':
    main()
