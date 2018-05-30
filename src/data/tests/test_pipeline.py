import os
import subprocess
import json
import shutil

#This is still a work in progress. Code might be incomplete/not working.
def test_entire_pipeline_should_run_without_errors(tmpdir):

    # Copy test data into temp directory
    orig_path = os.path.dirname(
        os.path.abspath(__file__)) + '/data/'
    path = tmpdir.strpath + '/data/'
    raw_files_path = path + '/test_pipeline/'
    
    #copy over data needed for test inside tmpDir
    shutil.copytree(orig_path+'/test_pipeline/', path+'/test_pipeline/')
    
    boston_path = path+'boston/'

    city_level_data_path_standardized = boston_path +'standardized/'
    city_level_data_path_raw = boston_path +'raw/'
    shutil.copytree(orig_path+'/raw/', city_level_data_path_raw)

    os.makedirs(boston_path + 'standardized')

    if not os.path.exists(boston_path + 'raw/crashes/cad_crash_events_with_transport_2016_wgs84_with_modetype.csv'):
        print 'No raw crashes here...'


    if os.path.exists(boston_path + 'raw/crashes/cad_crash_events_with_transport_2016_wgs84_with_modetype.csv'):
        print 'crashes here...'

    subprocess.check_call([
        'python',
        '-m',
        'pipeline',
        '-b',
        tmpdir.strpath,
        '--config_file',
        path+'/test_pipeline/config_boston.yml',
        '--onlysteps',
        'generation, standardization'
    ])