import configparser
import sys

from src.domain.hri_const import Constants as const
from src.logging.logger import Logger
from src.mgr.param_mgr import Param_Mgr

config = configparser.ConfigParser()
config.read('./resources/config/config.ini')
config.sections()


class Template_Mgr:
    TPLT_PATH = config['TEMPLATES SETTING']['TEMPLATES_PATH']
    DEST_PATH = config['TEMPLATES SETTING']['MODEL_PATH']
    TPLT_EXT = config['TEMPLATES SETTING']['TEMPLATES_EXT']
    MAIN = const.MAIN_TPLT.value
    TEMPLATES = [const.ROB_TPLT.value, const.BTR_TPLT.value, const.HA_TPLT.value, const.HC_TPLT.value,
                 const.HF_TPLT.value, const.HL_TPLT.value, const.HRec_TPLT.value,
                 const.HRes_TPLT.value, const.ORCH_TPLT.value, const.OPCHK_TPLT.value, const.ROS_TPLT.value]
    KEYWORDS = [const.ROB_KEY.value, const.BTR_KEY.value, const.HA_KEY.value, const.HC_KEY.value,
                const.HF_KEY.value, const.HL_KEY.value, const.HRec_KEY.value,
                const.HRes_KEY.value, const.ORCH_KEY.value, const.OPCHK_KEY.value, const.ROS_KEY.value]

    def fill_dict(self):
        res = {}
        for (i, tplt) in enumerate(self.TEMPLATES):
            res[tplt] = self.KEYWORDS[i]
        return res

    def __init__(self, param_mgr: Param_Mgr):
        self.TPLT_DICT = self.fill_dict()
        self.LOGGER = Logger('Template_Mgr')
        self.param_mgr = param_mgr

    def replace_tplt(self, scen_name: str):
        with open(self.DEST_PATH + scen_name + self.TPLT_EXT, 'r') as main_tplt:
            self.LOGGER.debug('Replacing SHA templates...')
            main_content = main_tplt.read()
            for tplt in self.TPLT_DICT:
                with open(self.TPLT_PATH + tplt + self.TPLT_EXT, 'r') as tplt_file:
                    self.LOGGER.debug('Replacing {} template...'.format(tplt))
                    tplt_content = self.param_mgr.replace_traj_keys(tplt) # tplt_file.read()
                    main_content = main_content.replace(self.TPLT_DICT[tplt], tplt_content)
        dest_model = open(self.DEST_PATH + scen_name + self.TPLT_EXT, 'w')
        dest_model.write(main_content)
        dest_model.close()
        self.LOGGER.info('{} model successfully saved in {}.'.format(scen_name, self.DEST_PATH))
