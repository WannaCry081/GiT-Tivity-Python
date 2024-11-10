class ValidationUtil:
    
    @staticmethod
    def git_is_init() -> bool:
        return Path(".git").exists()
