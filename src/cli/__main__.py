#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

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
