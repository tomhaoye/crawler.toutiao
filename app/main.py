import logging
import config
from pathlib import Path
from model import Topic
from util.orm import Session
from pyquery import PyQuery
import requests

DATA_DIR = Path(__file__).parent.joinpath('../html/').resolve()
DATA_DIR.mkdir(parents=True, exist_ok=True)
db_session = Session()


def insert_db_topic(db, title, url, like_count, like_it):
    exist = db.query(Topic).filter(
        Topic.title == title,
    ).first()
    if not exist:
        db.add(Topic(title, url, like_count, like_it))
        db.commit()
        logging.info('新增1条收藏数据')


def fetch_page():
    page = 1
    while page < config.config.largest_page:
        logging.info('抓取页面中')
        url = f'https://toutiao.io/favorites?page={page}'
        res = requests.get(url, headers=config.config.headers, timeout=5)
        res.raise_for_status()
        save_file = DATA_DIR.joinpath(f'{page}.html')
        save_file.write_bytes(res.content)
        logging.info('抓取页面完成')
        page += 1


def analyze(db):
    page = 1
    while page < config.config.largest_page:
        logging.info('分析区域与数据入库中')
        doc = PyQuery(DATA_DIR.joinpath(f'{page}.html').read_text(encoding='utf-8'))
        post = doc('.post')
        while post:
            title = post('.title a').html()
            url = post('.meta').html().splitlines()[1].strip()
            like_it_id = post('.like-button').attr.id
            like_it = post(f'#{like_it_id}').has_class('liked')
            like_count = int(post('.like-button span').html())
            insert_db_topic(db, title, url, like_count, like_it)
            post = post.next()
        logging.info('分析与数据入库done')
        page += 1
    db.close()


def main():
    fetch_page()
    analyze(db_session)


if __name__ == '__main__':
    main()
