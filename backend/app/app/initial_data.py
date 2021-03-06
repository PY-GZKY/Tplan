import os
import sys

from app.db.init_db import init_db

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    init_db()


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
