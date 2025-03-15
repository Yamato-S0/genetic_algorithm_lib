import logging

# シンプルに標準出力にログを出す設定例
logging.basicConfig(level=logging.INFO)


def get_logger(name=__name__):
    return logging.getLogger(name)
