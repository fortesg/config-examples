import os

FCG_DIR = os.path.dirname(os.path.realpath(__file__))
CACHE_DIR = FCG_DIR + '/cache'

ICON_DIR = '/home/christian/workspace/icon'

ASSEMBLER_DIRS = [ICON_DIR + '/build/x86_64-unknown-linux-gnu/src',
                  ICON_DIR + '/build/x86_64-unknown-linux-gnu/externals/mtime/src',
                  ICON_DIR + '/build/x86_64-unknown-linux-gnu/externals/self/src',
                  ICON_DIR + '/build/x86_64-unknown-linux-gnu/externals/tixi/src',
                  ICON_DIR + '/build/x86_64-unknown-linux-gnu/externals/yac/src', 
                  ICON_DIR + '/build/x86_64-unknown-linux-gnu/support'] 
SOURCE_DIRS = [ICON_DIR + '/src',
               ICON_DIR + '/externals/mtime/src',
               ICON_DIR + '/externals/self/src',
               ICON_DIR + '/externals/yac/src',
               ICON_DIR + '/externals/tixi/src',
               ICON_DIR + '/externals/jsbach/src',
               ICON_DIR + '/support',
               ICON_DIR + '/build/x86_64-unknown-linux-gnu/src'] #Letzter Eintrag fuer JSBACH-Generate 

SPECIAL_MODULE_FILES = {'mo_mcrph_sb': 'mo_2mom_mcrph_driver.f90',
                        'mo_lrtm': 'mo_lrtm_driver.f90', 'ppm_extents': 'mo_extents.f90',
                        'ppm_distributed_array': 'mo_dist_array.f90',
                        'psrad_rrsw_kg16': 'mo_psrad_srtm_kgs.f90', 'psrad_rrsw_kg17': 'mo_psrad_srtm_kgs.f90', 
                        'psrad_rrsw_kg18': 'mo_psrad_srtm_kgs.f90', 'psrad_rrsw_kg19': 'mo_psrad_srtm_kgs.f90', 
                        'psrad_rrsw_kg20': 'mo_psrad_srtm_kgs.f90', 'psrad_rrsw_kg21': 'mo_psrad_srtm_kgs.f90', 
                        'psrad_rrsw_kg22': 'mo_psrad_srtm_kgs.f90', 'psrad_rrsw_kg23': 'mo_psrad_srtm_kgs.f90', 
                        'psrad_rrsw_kg24': 'mo_psrad_srtm_kgs.f90', 'psrad_rrsw_kg25': 'mo_psrad_srtm_kgs.f90', 
                        'psrad_rrsw_kg26': 'mo_psrad_srtm_kgs.f90', 'psrad_rrsw_kg27': 'mo_psrad_srtm_kgs.f90', 
                        'psrad_rrsw_kg28': 'mo_psrad_srtm_kgs.f90', 'psrad_rrsw_kg29': 'mo_psrad_srtm_kgs.f90', 
                        'rrlw_planck': 'mo_psrad_lrtm_kgs.f90', 'psrad_rrlw_kg01': 'mo_psrad_lrtm_kgs.f90', 
                        'psrad_rrlw_kg02': 'mo_psrad_lrtm_kgs.f90', 'psrad_rrlw_kg03': 'mo_psrad_lrtm_kgs.f90', 
                        'psrad_rrlw_kg04': 'mo_psrad_lrtm_kgs.f90', 'psrad_rrlw_kg05': 'mo_psrad_lrtm_kgs.f90', 
                        'psrad_rrlw_kg06': 'mo_psrad_lrtm_kgs.f90', 'psrad_rrlw_kg07': 'mo_psrad_lrtm_kgs.f90', 
                        'psrad_rrlw_kg08': 'mo_psrad_lrtm_kgs.f90', 'psrad_rrlw_kg09': 'mo_psrad_lrtm_kgs.f90', 
                        'psrad_rrlw_kg10': 'mo_psrad_lrtm_kgs.f90', 'psrad_rrlw_kg11': 'mo_psrad_lrtm_kgs.f90', 
                        'psrad_rrlw_kg12': 'mo_psrad_lrtm_kgs.f90', 'psrad_rrlw_kg13': 'mo_psrad_lrtm_kgs.f90', 
                        'psrad_rrlw_kg14': 'mo_psrad_lrtm_kgs.f90', 'psrad_rrlw_kg15': 'mo_psrad_lrtm_kgs.f90', 
                        'psrad_rrlw_kg16': 'mo_psrad_lrtm_kgs.f90', 
                        'rrlw_kg01': 'mo_lrtm_kgs.f90', 'rrlw_kg02': 'mo_lrtm_kgs.f90', 
                        'rrlw_kg03': 'mo_lrtm_kgs.f90', 'rrlw_kg04': 'mo_lrtm_kgs.f90', 
                        'rrlw_kg05': 'mo_lrtm_kgs.f90', 'rrlw_kg06': 'mo_lrtm_kgs.f90', 
                        'rrlw_kg07': 'mo_lrtm_kgs.f90', 'rrlw_kg08': 'mo_lrtm_kgs.f90', 
                        'rrlw_kg09': 'mo_lrtm_kgs.f90', 'rrlw_kg10': 'mo_lrtm_kgs.f90', 
                        'rrlw_kg11': 'mo_lrtm_kgs.f90', 'rrlw_kg12': 'mo_lrtm_kgs.f90', 
                        'rrlw_kg13': 'mo_lrtm_kgs.f90', 'rrlw_kg14': 'mo_lrtm_kgs.f90', 
                        'rrlw_kg15': 'mo_lrtm_kgs.f90', 'rrlw_kg16': 'mo_lrtm_kgs.f90', 
                        'yoesrta16': 'mo_srtm_kgs.f90', 'yoesrta17': 'mo_srtm_kgs.f90', 
                        'yoesrta18': 'mo_srtm_kgs.f90', 'yoesrta19': 'mo_srtm_kgs.f90', 
                        'yoesrta20': 'mo_srtm_kgs.f90', 'yoesrta21': 'mo_srtm_kgs.f90', 
                        'yoesrta22': 'mo_srtm_kgs.f90', 'yoesrta23': 'mo_srtm_kgs.f90', 
                        'yoesrta24': 'mo_srtm_kgs.f90', 'yoesrta25': 'mo_srtm_kgs.f90', 
                        'yoesrta26': 'mo_srtm_kgs.f90', 'yoesrta27': 'mo_srtm_kgs.f90', 
                        'yoesrta28': 'mo_srtm_kgs.f90', 'yoesrta29': 'mo_srtm_kgs.f90',
                        'mtime': 'libmtime.f90', 'mtime_calendar': 'libmtime.f90', 
                        'mtime_julianday': 'libmtime.f90', 'mtime_date': 'libmtime.f90', 
                        'mtime_time': 'libmtime.f90', 'mtime_datetime': 'libmtime.f90', 
                        'mtime_timedelta': 'libmtime.f90', 'mtime_events': 'libmtime.f90', 
                        'mtime_eventgroups': 'libmtime.f90', 'mtime_utilities': 'libmtime.f90', 
                        'mtime_print_by_callback': 'libmtime.f90',
                        'mo_meteogram_config': 'mo_mtgrm_config.f90', 
                        'mo_meteogram_output': 'mo_mtgrm_output.f90',
                        'mo_art_sedi_interface': 'mo_art_sedimentation_interface.f90' }
EXCLUDE_MODULES = [ 'iso_fortran_env', 'iso_c_binding', 'ifcore', 'mpi', 'omp_lib', #Standard libraries
                    'messy_main_channel_bi', 'messy_main_tracer_bi', 'messy_main_timer_bi', #MESSY
                    'mo_remap_config', 'mo_utilities', #?
                    'gme_data_parameters', 'prognostic_pp', #GME
                    'mo_rttov_ifc', #RTTOV
                    'mo_wwonly', #ONLYWW
                    'mo_filename', 'mo_netcdf', 'mo_time_control', 'mo_decomposition', 'mo_interpo', 
                    'mo_io', 'mo_time_conversion', 'mo_time_event', 'mo_gaussgrid', 'mo_tr_scatter',
                    'mo_transpose', 'mo_geoloc', 'mo_memory_base', 'mo_control', 'mo_semi_impl', 
                    'mo_submodel', #ECHAM?
                    'meteo_utilities', 'environment', 'utilities', 'pp_utilities', 'kind_parameters', 
                    'src_stoch_physics', 'turbulence_data', 'data_gscp', 'data_parameters', 'data_constants', 
                    'data_runcontrol', 'data_parallel', 'data_modelconfig', 'data_soil', 'data_fields', #COSMO
                    'data_lheat_nudge', 'src_lheating', #NUDGING
                    'mod_prism_proto', #PRISM
                    'sct', #SCT
                    'data_1d_global', #SCLM
                    'mo_art_init', 'mo_art_tracer', 'mo_art_diag_state', 'mo_art_read_emissions', 
                    'mo_art_emission_pntSrc', 'mo_art_integration', 'mo_art_emission_dust', 
                    'mo_art_emission_volc_2mom', 'mo_art_emission_chemtracer', 'mo_art_modes', 
                    'mo_art_emission_dust_simple', 'mo_art_emission_pollen', 'mo_art_data', 
                    'mo_art_emission_volc_1mom', 'mo_art_emission_seas', 'mo_art_modes_linked_list', 
                    'mo_art_emission_gasphase', 'mo_art_aerosol_utilities', 'mo_art_clipping', 
                    'mo_art_sedi_2mom', 'mo_art_sedi_1mom', 'mo_art_drydepo_radioact', 'mo_art_depo_2mom', 
                    'mo_art_photolysis', 'mo_art_decay_radioact', 'mo_art_gasphase', 'mo_art_chemtracer', 
                    'mo_art_washout_volc', 'mo_art_washout_radioact', 'mo_art_washout_aerosol', 
                    'mo_art_radiation_aero', 'mo_art_prepare_aerosol', 'mo_art_2mom_driver', 
                    'mo_art_diagnostics', 'mo_art_aero_optical_props', 'mo_art_surface_value', 
                    'mo_art_diag_types', 'mo_art_unit_conversion',  #ICON-ART
                    
                    'mo_exception', 'mo_mpi' 
                  ]

IGNORE_GLOBALS_FROM_MODULES = EXCLUDE_MODULES 
IGNORE_DERIVED_TYPES = []
