import os

FCG_DIR = os.path.dirname(os.path.realpath(__file__))
CACHE_DIR = FCG_DIR + '/cache/mom6'

MOM6_DIR = '/home/christian/workspace/MOM6-examples'

ASSEMBLER_DIRS = [MOM6_DIR + '/build/gnu/ocean_only/savetemps',
                  MOM6_DIR + '/build/gnu/shared/savetemps'] 
SOURCE_DIRS = ASSEMBLER_DIRS + [MOM6_DIR + '/src']

SOURCE_FILES_PREPROCESSED = True

SPECIAL_MODULE_FILES = {'regional_dyes':'dye_example.f90', 
                        'MOM_int_tide_input':'MOM_internal_tide_input.f90',
                        'MOM_PressureForce_AFV': 'MOM_PressureForce_analytic_FV.f90', 
                        'MOM_PressureForce_blk_AFV':'MOM_PressureForce_blocked_AFV.f90',
                        'MOM_PressureForce_Mont':'MOM_PressureForce_Montgomery.f90',
                        'MOM_set_visc':'MOM_set_viscosity.f90',
                        'USER_tracer_example':'tracer_example.f90',
                        'null_fms_io_test':'test_fms_io.f90',
                        'null_test_horiz_interp':'test_horiz_interp.f90',
                        'null_mpp_domains_test':'test_mpp_domains.f90',
                        'null_mpp_test':'test_mpp.f90',
                        'null_mpp_io_test':'test_mpp_io.f90',
                        'null_mpp_pset_test':'test_mpp_pset.f90',
                        'null_test_xgrid':'test_xgrid.f90'
                        }
EXCLUDE_MODULES = []

IGNORE_GLOBALS_FROM_MODULES = EXCLUDE_MODULES
IGNORE_DERIVED_TYPES = []
ALWAYS_FULL_TYPES = []

ABSTRACT_TYPE_IMPLEMENTATIONS = {}
