import subprocess
#import pkg_resources

def get_outdated_packages(): 
    result = subprocess.run(['pip', 'list', '--outdated'], capture_output=True, text=True)  # get all the outdated packages into a string
    outdated_packages = result.stdout.split('\n')   # split the string each newline and get into a list --> 'package version latest type'
    outdated_packages_list = []                     # it'll works like list of list with the information of the outdated packages
    for package in outdated_packages:
        outdated_packages_list.append(package.split())  # split each string(element) from outdated_packages
                                                        # 'package version latest type' --> [package,version,latest,type]
                                                        # each list is allocated in outdated_packages_list
    return outdated_packages_list

def update_package(package_name):
    subprocess.run(['pip', 'install', '--upgrade', package_name], check=True)

def main():
    # proces to update packages
    outdated_packages = get_outdated_packages()
    if not outdated_packages[0]:
        print("All the packages are updated")
    else:
        i = 0
        for package in outdated_packages:
            i+=1
            if(i>2):    # jump the two first element of the list because it's unesessary information (without information about the packages and their versions)
                package_name = f'{package[0]}=={package[2]}'    
                print(f'Updating {package[0]}...')
                update_package(package_name)
        print('Update process completed.')

if __name__ == '__main__':
    main()
