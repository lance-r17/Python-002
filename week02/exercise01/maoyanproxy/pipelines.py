# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from scrapy.utils.project import get_project_settings

sqls = {
    'DELETE': "delete from `movie`", 
    'CREATE': "insert into `movie` (`title`, `catetory`, `release`) value (%s, %s, %s)"
}


class MaoyanproxyPipeline:
    def __init__(self):
        settings = get_project_settings()
        self.conn = pymysql.connect(
            host = settings.get('MYSQL_HOST'),
            port = settings.get('MYSQL_PORT'),
            user = settings.get('MYSQL_USER'),
            password = settings.get('MYSQL_PASSWORD'),
            db = settings.get('MYSQL_DB'),
            charset = settings.get('MYSQL_CHARSET'))
        self.cur = self.conn.cursor()
        try:
            self.cur.execute(sqls['DELETE'])
            self.conn.commit()
        except:
            self.conn.rollback()

    def close_spider(self, spider):
        self.conn.close

    def process_item(self, item, spider):
        try:
            self.cur.execute(sqls['CREATE'], (item['title'], item['category'], item['release']))
            self.conn.commit()
        except:
            self.conn.rollback()
        return item

