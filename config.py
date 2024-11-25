import os


class Settings:
    __DATA_DIR_NAME = 'data'
    __DATA_FILE_NAME = 'data.json'
    __LOG_FILE_NAME = 'log.log'

    @property
    def data_file_path(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(current_dir, self.__DATA_DIR_NAME, self.__DATA_FILE_NAME)

    @property
    def log_file_path(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(current_dir, self.__LOG_FILE_NAME)


settings = Settings()
