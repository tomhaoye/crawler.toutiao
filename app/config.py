import logging
import sys
from pathlib import Path
import json

logging.basicConfig(format='%(asctime)s %(name)s[%(module)s] %(levelname)s: %(message)s', level=logging.INFO)
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "",
    "Host": "toutiao.io",
    "Referer": "https://toutiao.io/",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}


class Config:
    def __init__(self):
        self.largest_page = 1
        self.headers = {}
        self.database = {}


def load():
    this_config = Config()
    this_config.headers = headers
    config_name = 'config.example.json'
    logging.info(f'配置文件 "{config_name}"')
    config_file = Path(__file__).parent.joinpath(config_name)
    if not config_file.exists():
        sys.exit(f'配置文件{config_name}不存在')
    config_json = config_file.resolve()
    config_dict = json.loads(config_json.read_text())
    this_config.database = config_dict['database']
    this_config.largest_page = config_dict['extra']['largest_page']
    return this_config


config = load()
