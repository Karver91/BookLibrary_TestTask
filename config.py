import os


class Settings:
    __DATA_DIR_NAME = 'data'
    __DATA_FILE_NAME = 'data.json'
    __LOG_FILE_NAME = 'log.log'

    @property
    def data_file_path(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir_path = os.path.join(current_dir, self.__DATA_DIR_NAME)
        if not os.path.exists(data_dir_path):
            os.makedirs(data_dir_path)
        return os.path.join(data_dir_path, self.__DATA_FILE_NAME)

    @property
    def log_file_path(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(current_dir, self.__LOG_FILE_NAME)


settings = Settings()
