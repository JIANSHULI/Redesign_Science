import os
import subprocess
import json


def construct_version_info():
    redesign_science_dir = os.path.dirname(os.path.realpath(__file__))
    if 'src' in redesign_science_dir:
        redesign_science_dir = redesign_science_dir[:-4]
    version_file = os.path.join(redesign_science_dir, 'VERSION')
    version = open(version_file).read().strip()
    print('redesign_science: %s'%redesign_science_dir)
    print('version_file: %s'%version_file)
    print('version: %s'%version)

    try:
        try:
            git_origin = subprocess.check_output(['git', '-C', redesign_science_dir, 'config',
                                                  '--get', 'remote.origin.url'],
                                                 stderr=subprocess.STDOUT).strip()
        except:
            print('Exception: git_origin.')
        git_hash = subprocess.check_output(['git', '-C', redesign_science_dir, 'rev-parse', 'HEAD'],
                                           stderr=subprocess.STDOUT).strip()
        git_description = subprocess.check_output(['git', '-C', redesign_science_dir,
                                                   'describe', '--dirty', '--tag', '--always']).strip()
        git_branch = subprocess.check_output(['git', '-C', redesign_science_dir, 'rev-parse',
                                              '--abbrev-ref', 'HEAD'],
                                             stderr=subprocess.STDOUT).strip()
        try:
            git_version = subprocess.check_output(['git', '-C', redesign_science_dir, 'describe',
                                               '--tags', '--abbrev=0']).strip()
        except:
            # assert type(exception).__name__ == 'NameError'
            # assert exception.__class__.__name__ == 'NameError'
            print('Exception: git_version.')
            pass
        
    except subprocess.CalledProcessError:
        try:
            # Check if a GIT_INFO file was created when installing package
            git_file = os.path.join(redesign_science_dir, 'GIT_INFO')
            print('git_file: %s'%git_file)
            with open(git_file) as data_file:
                data = [x.encode('UTF8') for x in json.loads(data_file.read().strip())]
                git_origin = data[0]
                git_hash = data[1]
                git_description = data[2]
                git_branch = data[3]
        except (IOError, OSError):
            git_origin = ''
            git_hash = ''
            git_description = ''
            git_branch = ''

    version_info = {'version': version, 'git_origin': git_origin,
                    'git_hash': git_hash, 'git_description': git_description,
                    'git_branch': git_branch}
    print(version_info)
    return version_info
    

version_info = construct_version_info()
version = version_info['version']
git_origin = str(version_info['git_origin'], 'utf-8')
git_hash = str(version_info['git_hash'], 'utf-8')
git_description = str(version_info['git_description'], 'utf-8')
git_branch = str(version_info['git_branch'], 'utf-8')


def main():
    print('Version = {0}'.format(version))
    print('git origin = {0}'.format(git_origin))
    print('git branch = {0}'.format(git_branch))
    print('git description = {0}'.format(git_description))


if __name__ == '__main__':
    main()
