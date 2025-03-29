
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)#Progress bar mode - displays a progress bar with training and validation metrics.
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list