import logging
import sys


class FrameworkLogger:

    _logger = None

    @classmethod
    def get_logger(cls):

        if cls._logger:
            return cls._logger

        logger = logging.getLogger("QAFramework")

        logger.setLevel(logging.INFO)

        if not logger.handlers:

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )

            console = logging.StreamHandler(sys.stdout)

            console.setFormatter(formatter)

            logger.addHandler(console)

        cls._logger = logger

        return logger