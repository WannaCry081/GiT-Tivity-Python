from pathlib import Path
from typing import Optional

class ValidationUtil:
    
    @staticmethod
    def git_is_init() -> bool:
        return Path(".git").exists()

    @staticmethod
    def git_has_config(result: str) -> Optional[bool]:
        value = result.strip() if isinstance(result, str) else ""
        return bool(value) if value else None
