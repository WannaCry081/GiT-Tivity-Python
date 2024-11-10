import sys
import logging
from src import Program


if __name__ == "__main__":
    try:
        exit_code = Program.main(sys.argv[1:])

    except Exception as e:
        logging.error(
            "An unexpected error occurred while executing the program.", exc_info=True
        )
        exit_code = -1

    sys.exit(exit_code)
