import sys
from typing import Unpack

from poethepoet import app

# Create a client for the CLI application.
client: app.PoeThePoet = app.PoeThePoet(
    program_name="zotero",
    config_name="src/cli/tasks.toml",
)


def main() -> None:
    args: Unpack[str] = sys.argv[1:]
    result: int = client(args)
    sys.exit(result)


if __name__ == "__main__":
    main()
