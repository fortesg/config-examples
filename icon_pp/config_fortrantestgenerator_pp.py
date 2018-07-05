import os

FTG_DIR = os.path.dirname(os.path.realpath(__file__))

FCG_DIR = FTG_DIR + '/../fortrancallgraph'
FCG_CONFIG_FILE = 'config_fortrancallgraph_pp.py'

TEMPLATE = FTG_DIR + '/templates/IconStandalone/IconStandalone.tmpl'

ICON_DIR = '/home/christian/workspace/icon'

TEST_SOURCE_DIR = ICON_DIR + '/src/tests'
TEST_DATA_BASE_DIR = ICON_DIR + '/ftg'

MODIFY_SOURCE_DIRS = [ICON_DIR + '/src',
                      ICON_DIR + '/externals/mtime/src',
                      ICON_DIR + '/externals/self/src',
                      ICON_DIR + '/externals/yac/src',
                      ICON_DIR + '/externals/tixi/src',
                      ICON_DIR + '/externals/jsbach/src',
                      ICON_DIR + '/support'] 
