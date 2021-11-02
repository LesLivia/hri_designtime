import configparser

from src.logging.logger import Logger
from src.domain.query import Query
from typing import List

config = configparser.ConfigParser()
config.read('./resources/config/config.ini')
config.sections()


class Query_Mgr:
    DEST_PATH = config['TEMPLATES SETTING']['MODEL_PATH']
    QUERY_EXT = config['TEMPLATES SETTING']['QUERY_EXT']

    def __init__(self, q: List[Query]):
        self.LOGGER = Logger('Query_Mgr')
        self.q = q

    def gen_q_file(self, scen_name: str):
        with open(self.DEST_PATH + scen_name + self.QUERY_EXT, 'w') as query_file:
            self.LOGGER.info("Creating .q file...")
            queries = [q.get_query() for q in self.q]
            query_file.writelines(queries)
            self.LOGGER.info("Query file successfully saved in {}".format(self.DEST_PATH))
