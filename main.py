import sys
import logging
from src import Program


if __name__ == "__main__":
    exit_code = Program.main(sys.argv[1:])
    sys.exit(exit_code)
