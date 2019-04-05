import os

FCG_DIR = os.path.dirname(os.path.realpath(__file__))
CACHE_DIR = FCG_DIR + '/cache/icon'

ICON_DIR = '/home/christian/workspace/icon'

ASSEMBLER_DIRS = [ICON_DIR + '/build/x86_64-unknown-linux-gnu/src',
                  ICON_DIR + '/build/x86_64-unknown-linux-gnu/externals/mtime/src',
                  ICON_DIR + '/build/x86_64-unknown-linux-gnu/externals/self/src',
                  ICON_DIR + '/build/x86_64-unknown-linux-gnu/externals/tixi/src',
                  ICON_DIR + '/build/x86_64-unknown-linux-gnu/externals/yac/src', 
                  ICON_DIR + '/build/x86_64-unknown-linux-gnu/support'] 
SOURCE_DIRS = ASSEMBLER_DIRS

SOURCE_FILES_PREPROCESSED = True

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
                        'mtime_print_by_callback': 'libmtime.f90', 'mtime_juliandelta': 'libmtime.f90',
                        'mo_meteogram_config': 'mo_mtgrm_config.f90', 
                        'mo_meteogram_output': 'mo_mtgrm_output.f90',
                        'mo_art_sedi_interface': 'mo_art_sedimentation_interface.f90',
                        'mo_assimi_config_class': 'mo_assimi_config_class_dsl4jsb.f90', 
                        'mo_assimi_constants': 'mo_assimi_constants_dsl4jsb.f90', 
                        'mo_assimi_interface': 'mo_assimi_interface_dsl4jsb.f90', 
                        'mo_assimi_memory_class': 'mo_assimi_memory_class_dsl4jsb.f90', 
                        'mo_assimi_process': 'mo_assimi_process_dsl4jsb.f90', 
                        'mo_a2l_memory_class': 'mo_atm2land_memory_class_dsl4jsb.f90', 
                        'mo_atmland_interface': 'mo_atmland_interface_dsl4jsb.f90', 
                        'mo_carbon_config_class': 'mo_carbon_config_class_dsl4jsb.f90', 
                        'mo_carbon_constants': 'mo_carbon_constants_dsl4jsb.f90', 
                        'mo_carbon_init': 'mo_carbon_init_dsl4jsb.f90', 
                        'mo_carbon_interface': 'mo_carbon_interface_dsl4jsb.f90', 
                        'mo_carbon_memory_class': 'mo_carbon_memory_class_dsl4jsb.f90', 
                        'mo_carbon_process': 'mo_carbon_process_dsl4jsb.f90', 
                        'mo_hd_config_class': 'mo_hd_config_class_dsl4jsb.f90', 
                        'mo_hd_init': 'mo_hd_init_dsl4jsb.f90', 
                        'mo_hd_interface': 'mo_hd_interface_dsl4jsb.f90', 
                        'mo_hd_memory_class': 'mo_hd_memory_class_dsl4jsb.f90', 
                        'mo_hd_reservoir_cascade': 'mo_hd_reservoir_cascade_dsl4jsb.f90', 
                        'mo_hsm_class': 'mo_hsm_class_dsl4jsb.f90', 
                        'mo_hydro_config_class': 'mo_hydro_config_class_dsl4jsb.f90', 
                        'mo_hydro_constants': 'mo_hydro_constants_dsl4jsb.f90', 
                        'mo_hydro_init': 'mo_hydro_init_dsl4jsb.f90', 
                        'mo_hydro_interface': 'mo_hydro_interface_dsl4jsb.f90', 
                        'mo_hydro_memory_class': 'mo_hydro_memory_class_dsl4jsb.f90', 
                        'mo_hydro_process': 'mo_hydro_process_dsl4jsb.f90', 
                        'mo_hydro_util': 'mo_hydro_util_dsl4jsb.f90', 
                        'mo_interface_hd_ocean': 'mo_interface_hd_ocean_dsl4jsb.f90', 
                        'mo_jsb4_forcing': 'mo_jsb4_forcing_dsl4jsb.f90', 
                        'mo_jsb_base': 'mo_jsb_base_dsl4jsb.f90', 
                        'mo_jsb_class': 'mo_jsb_class_dsl4jsb.f90', 
                        'mo_jsb_config_class': 'mo_jsb_config_class_dsl4jsb.f90', 
                        'mo_jsb_control': 'mo_jsb_control_dsl4jsb.f90', 
                        'mo_jsb_domain_iface': 'mo_jsb_domain_iface_dsl4jsb.f90', 
                        'mo_jsb_grid_class': 'mo_jsb_grid_class_dsl4jsb.f90', 
                        'mo_jsb_grid': 'mo_jsb_grid_dsl4jsb.f90', 
                        'mo_jsb_interface': 'mo_jsb_interface_dsl4jsb.f90', 
                        'mo_jsb_io': 'mo_jsb_io_dsl4jsb.f90', 
                        'mo_jsb_io_iface': 'mo_jsb_io_iface_dsl4jsb.f90', 
                        'mo_jsb_io_netcdf': 'mo_jsb_io_netcdf_dsl4jsb.f90', 
                        'mo_jsb_io_netcdf_iface': 'mo_jsb_io_netcdf_iface_dsl4jsb.f90', 
                        'mo_jsb_lct_class': 'mo_jsb_lct_class_dsl4jsb.f90', 
                        'mo_jsb_lctlib_class': 'mo_jsb_lctlib_class_dsl4jsb.f90', 
                        'mo_jsb_memory_class': 'mo_jsb_memory_class_dsl4jsb.f90', 
                        'mo_jsb_model_class': 'mo_jsb_model_class_dsl4jsb.f90', 
                        'mo_jsb_model_init': 'mo_jsb_model_init_dsl4jsb.f90', 
                        'mo_jsb_model_usecases': 'mo_jsb_model_usecases_dsl4jsb.f90', 
                        'mo_jsb_namelist_iface': 'mo_jsb_namelist_iface_dsl4jsb.f90', 
                        'mo_jsb_nml_iface': 'mo_jsb_nml_iface_dsl4jsb.f90', 
                        'mo_jsb_parallel': 'mo_jsb_parallel_dsl4jsb.f90', 
                        'mo_jsb_parallel_iface': 'mo_jsb_parallel_iface_dsl4jsb.f90', 
                        'mo_jsb_physical_constants': 'mo_jsb_physical_constants_dsl4jsb.f90', 
                        'mo_jsb_process_class': 'mo_jsb_process_class_dsl4jsb.f90', 
                        'mo_jsb_process_factory': 'mo_jsb_process_factory_dsl4jsb.f90', 
                        'mo_jsb_task_class': 'mo_jsb_task_class_dsl4jsb.f90', 
                        'mo_jsb_test': 'mo_jsb_test_dsl4jsb.f90', 
                        'mo_jsb_tile_class': 'mo_jsb_tile_class_dsl4jsb.f90', 
                        'mo_jsb_tile': 'mo_jsb_tile_dsl4jsb.f90', 
                        'mo_jsb_time': 'mo_jsb_time_dsl4jsb.f90', 
                        'mo_jsb_time_iface': 'mo_jsb_time_iface_dsl4jsb.f90', 
                        'mo_jsb_utils_iface': 'mo_jsb_utils_iface_dsl4jsb.f90', 
                        'mo_jsb_var_class': 'mo_jsb_var_class_dsl4jsb.f90', 
                        'mo_jsb_varlist': 'mo_jsb_varlist_dsl4jsb.f90', 
                        'mo_jsb_varlist_iface': 'mo_jsb_varlist_iface_dsl4jsb.f90', 
                        'mo_jsb_version': 'mo_jsb_version_dsl4jsb.f90', 
                        'mo_jsb_vertical_axes': 'mo_jsb_vertical_axes_dsl4jsb.f90',
                        'mo_jsb_vertical_axes_iface': 'mo_jsb_vertical_axes_iface_dsl4jsb.f90',
                        'mo_land2atm_memory_class': 'mo_land2atm_memory_class_dsl4jsb.f90', 
                        'mo_pheno_config_class': 'mo_pheno_config_class_dsl4jsb.f90', 
                        'mo_pheno_constants': 'mo_pheno_constants_dsl4jsb.f90', 
                        'mo_pheno_init': 'mo_pheno_init_dsl4jsb.f90', 
                        'mo_pheno_interface': 'mo_pheno_interface_dsl4jsb.f90', 
                        'mo_pheno_memory_class': 'mo_pheno_memory_class_dsl4jsb.f90', 
                        'mo_pheno_process': 'mo_pheno_process_dsl4jsb.f90', 
                        'mo_phy_schemes': 'mo_phy_schemes_dsl4jsb.f90', 
                        'mo_phy_schemes_iface': 'mo_phy_schemes_iface_dsl4jsb.f90', 
                        'mo_physical_constants_iface': 'mo_physical_constants_iface_dsl4jsb.f90', 
                        'mo_rad_config_class': 'mo_rad_config_class_dsl4jsb.f90', 
                        'mo_rad_constants': 'mo_rad_constants_dsl4jsb.f90', 
                        'mo_rad_init': 'mo_rad_init_dsl4jsb.f90', 
                        'mo_rad_interface': 'mo_rad_interface_dsl4jsb.f90', 
                        'mo_rad_memory_class': 'mo_rad_memory_class_dsl4jsb.f90', 
                        'mo_rad_process': 'mo_rad_process_dsl4jsb.f90', 
                        'mo_seb_config_class': 'mo_seb_config_class_dsl4jsb.f90', 
                        'mo_seb_init': 'mo_seb_init_dsl4jsb.f90', 
                        'mo_seb_interface': 'mo_seb_interface_dsl4jsb.f90', 
                        'mo_seb_lake': 'mo_seb_lake_dsl4jsb.f90', 
                        'mo_seb_land': 'mo_seb_land_dsl4jsb.f90', 
                        'mo_seb_memory_class': 'mo_seb_memory_class_dsl4jsb.f90', 
                        'mo_sse_config_class': 'mo_sse_config_class_dsl4jsb.f90', 
                        'mo_sse_constants': 'mo_sse_constants_dsl4jsb.f90', 
                        'mo_sse_init': 'mo_sse_init_dsl4jsb.f90', 
                        'mo_sse_interface': 'mo_sse_interface_dsl4jsb.f90', 
                        'mo_sse_memory_class': 'mo_sse_memory_class_dsl4jsb.f90', 
                        'mo_sse_process': 'mo_sse_process_dsl4jsb.f90', 
                        'mo_sse_util': 'mo_sse_util_dsl4jsb.f90', 
                        'mo_turb_config_class': 'mo_turb_config_class_dsl4jsb.f90', 
                        'mo_turb_constants': 'mo_turb_constants_dsl4jsb.f90', 
                        'mo_turb_init': 'mo_turb_init_dsl4jsb.f90', 
                        'mo_turb_interface': 'mo_turb_interface_dsl4jsb.f90', 
                        'mo_turb_memory_class': 'mo_turb_memory_class_dsl4jsb.f90', 
                        'mo_util': 'mo_util_dsl4jsb.f90',
                        'xt_core': 'xt_core_f.f90', 'xt_idxlist_collection': 'xt_idxlist_collection_f.f90',
                        'xt_idxlist_abstract': 'xt_idxlist_f.f90', 'xt_idxsection': 'xt_idxsection_f.f90',
                        'xt_mpi': 'xt_mpi_f.f90', 'xt_idxmod': 'xt_idxmod_f.f90',
                        'xt_idxvec': 'xt_idxvec_f.f90',
                        'xt_idxstripes': 'xt_idxstripes_f.f90', 'xt_redist_base': 'xt_redist_f.f90',
                        'xt_requests': 'xt_request_f.f90', 'xt_sort': 'xt_sort_f.f90',
                        'xt_xmap_abstract': 'xt_xmap_f.f90', 'xt_xmap_intersection': 'xt_xmap_intersection_f.f90' }
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
                    'mo_art_diag_types', 'mo_art_unit_conversion', 'mo_art_prescribed_state', #ICON-ART
                    'mo_assimi_config_class', 'mo_assimi_constants', 'mo_assimi_interface', 'mo_assimi_memory_class', 
                    'mo_assimi_process', 'mo_a2l_memory_class', 'mo_atmland_interface', 
                    'mo_carbon_config_class', 'mo_carbon_constants', 'mo_carbon_init', 'mo_carbon_interface', 
                    'mo_carbon_memory_class',  'mo_carbon_process', 'mo_carbon_constants', 
                    'mo_hd_config_class', 'mo_hd_init', 'mo_hd_interface', 'mo_hd_memory_class', 'mo_hd_reservoir_cascade', 
                    'mo_hsm_class', 'mo_hydro_config_class', 'mo_hydro_constants', 'mo_hydro_init', 'mo_hydro_interface', 
                    'mo_hydro_memory_class', 'mo_hydro_process', 'mo_hydro_util', 'mo_interface_hd_ocean', 
                    'mo_jsb4_forcing', 'mo_jsb_base', 'mo_jsb_class', 'mo_jsb_config_class', 'mo_jsb_control', 
                    'mo_jsb_domain_iface', 'mo_jsb_grid_class', 'mo_jsb_grid', 'mo_jsb_interface', 
                    'mo_jsb_io', 'mo_jsb_io_iface', 'mo_jsb_io_netcdf', 'mo_jsb_io_netcdf_iface', 'mo_jsb_lct_class', 
                    'mo_jsb_lctlib_class', 'mo_jsb_memory_class', 'mo_jsb_model_class', 'mo_jsb_model_init', 
                    'mo_jsb_model_usecases', 'mo_jsb_namelist_iface', 'mo_jsb_nml_iface', 'mo_jsb_parallel',
                    'mo_jsb_parallel_iface', 'mo_jsb_physical_constants', 'mo_jsb_process_class', 
                    'mo_jsb_process_factory', 'mo_jsb_task_class', 'mo_jsb_test', 'mo_jsb_tile_class', 'mo_jsb_tile',
                    'mo_jsb_time', 'mo_jsb_time_iface', 'mo_jsb_utils_iface', 'mo_jsb_var_class', 'mo_jsb_varlist',
                    'mo_jsb_varlist_iface', 'mo_jsb_version', 'mo_jsb_vertical_axes', 'mo_jsb_vertical_axes_iface', #JSBACH 
                    'mo_exception', 'mo_mpi' 
                  ]

IGNORE_GLOBALS_FROM_MODULES = EXCLUDE_MODULES + ['mtime']
IGNORE_DERIVED_TYPES = []
ALWAYS_FULL_TYPES = ['datetime', 'timedelta']

ABSTRACT_TYPE_IMPLEMENTATIONS = {'t_comm_pattern':('mo_communication_orig','t_comm_pattern_orig'),
                                 't_comm_pattern_collection':('mo_communication_orig','t_comm_pattern_collection_orig')}
