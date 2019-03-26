import os

FTG_DIR = os.path.dirname(os.path.realpath(__file__))

FCG_DIR = FTG_DIR + '/../fortrancallgraph'
FCG_CONFIG_FILE = 'config_fortrancallgraph_mom6.py'

BACKUP_SUFFIX = 'ftg-backup'
FTG_PREFIX = 'ftg_'

TEMPLATE = FTG_DIR + '/templates/Standalone/Standalone.tmpl'

MOM6_DIR = '/home/christian/workspace/MOM6-examples'

TEST_SOURCE_DIR = MOM6_DIR + '/src/ftgtests'
TEST_DATA_BASE_DIR = MOM6_DIR + '/ftg'

MODIFY_SOURCE_DIRS = [MOM6_DIR + '/src'] 
