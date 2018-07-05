import os

FTG_DIR = os.path.dirname(os.path.realpath(__file__))

FCG_DIR = FTG_DIR + '/../fortrancallgraph'
FCG_CONFIG_FILE = 'config_fortrancallgraph.py'

ICON_DIR = '/home/christian/workspace/icon'

TEMPLATE = FTG_DIR + '/templates/IconStandalone/IconStandalone.tmpl'
TEST_SOURCE_DIR = ICON_DIR + '/src/tests'
TEST_DATA_BASE_DIR = ICON_DIR + '/ftg'
