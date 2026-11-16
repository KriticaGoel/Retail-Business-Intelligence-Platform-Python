import configparser
from pathlib import Path

import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler

# Find project root dynamically
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Configuration file location
CONFIG_FILE = PROJECT_ROOT / "config.ini"

# Read configuration
config = configparser.ConfigParser()

if not CONFIG_FILE.exists():
    raise FileNotFoundError(
        f"Configuration file not found: {CONFIG_FILE}"
    )

config.read(CONFIG_FILE)

# Read directories
RAW_DATA_DIR = PROJECT_ROOT / config.get(
    "PATHS", "raw_data_dir"
)

# PROCESSED_DATA_DIR = PROJECT_ROOT / config.get(
#     "PATHS", "processed_data_dir"
# )

# QUARANTINE_DATA_DIR = PROJECT_ROOT / config.get(
#     "PATHS", "quarantine_data_dir"
# )

# Read filenames and construct full paths
TRANSACTIONS_FILE = RAW_DATA_DIR / config.get(
    "FILES", "transactions_file"
)

PRODUCTS_FILE = RAW_DATA_DIR / config.get(
    "FILES", "products_file"
)

CUSTOMERS_FILE = RAW_DATA_DIR / config.get(
    "FILES", "customers_file"
)

class TimestampedRotatingFileHandler(RotatingFileHandler):
    """
    Rotates log files based on maximum size.
    Every newly created log file gets a timestamp.
    """

    def __init__(
        self,
        log_directory: Path,
        file_prefix: str,
        max_bytes: int,
        backup_count: int
    ):
        self.log_directory = log_directory
        self.file_prefix = file_prefix

        self.log_directory.mkdir(
            parents=True,
            exist_ok=True
        )

        filename = self._generate_filename()

        super().__init__(
            filename=str(filename),
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8"
        )

    def _generate_filename(self) -> Path:
        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S_%f"
        )

        return self.log_directory / (
            f"{self.file_prefix}_{timestamp}.log"
        )

    def doRollover(self):
        """
        Close the current file and create a new timestamped file.
        """

        if self.stream:
            self.stream.flush()
            self.stream.close()
            self.stream = None

        self.baseFilename = str(self._generate_filename())

        self.stream = self._open()

        self._cleanup_old_files()

    def _cleanup_old_files(self):
        """
        Retain only the configured number of old log files.
        """

        if self.backupCount <= 0:
            return

        log_files = sorted(
            self.log_directory.glob(
                f"{self.file_prefix}_*.log"
            ),
            key=lambda path: path.name,
            reverse=True
        )

        # Keep the newest backup_count files plus current file.
        for old_file in log_files[self.backupCount + 1:]:
            try:
                old_file.unlink()
            except OSError:
                logging.getLogger(__name__).exception(
                    "Unable to delete old log file: %s",
                    old_file
                )


def configure_logging():


    log_dir = PROJECT_ROOT / config.get(
        "LOGGING", "log_dir"
    )

    level_name = config.get(
        "LOGGING", "level"
    ).upper()

    console_level_name = config.get(
        "LOGGING", "console_level"
    ).upper()

    file_level_name = config.get(
        "LOGGING", "file_level"
    ).upper()

    # Validate logging levels.
    level = getattr(logging, level_name, None)
    console_level = getattr(logging, console_level_name, None)
    file_level = getattr(logging, file_level_name, None)

    valid_levels = {
        logging.DEBUG,
        logging.INFO,
        logging.WARNING,
        logging.ERROR,
        logging.CRITICAL
    }

    if any(
        item not in valid_levels
        for item in (level, console_level, file_level)
    ):
        raise ValueError("Invalid logging level in config.ini")

    max_bytes = config.getint(
        "LOGGING", "max_bytes"
    )

    backup_count = config.getint(
        "LOGGING", "backup_count"
    )

    file_prefix = config.get(
        "LOGGING", "file_prefix"
    )

    if max_bytes <= 0 or backup_count < 0:
        raise ValueError("Invalid logging size or backup count")

    # Configure the root logger.
    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    # Prevent duplicate handlers if configuration runs again.
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
        handler.close()

    # Common log format.
    formatter = logging.Formatter(
        fmt=(
            "%(asctime)s | "
            "%(levelname)-8s | "
            "%(name)s | "
            "%(message)s"
        ),
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console handler.
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)
    console_handler.setFormatter(formatter)

    # File handler with size-based rollover.
    file_handler = TimestampedRotatingFileHandler(
        log_directory=log_dir,
        file_prefix=file_prefix,
        max_bytes=max_bytes,
        backup_count=backup_count
    )

    file_handler.setLevel(file_level)
    file_handler.setFormatter(formatter)

    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    root_logger.info("Global logging configured successfully")