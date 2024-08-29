import subprocess
#import pkg_resources

def get_outdated_packages():
    result = subprocess.run(['pip', 'list', '--outdated'], capture_output=True, text=True)
    outdated_packages = result.stdout.split('\n')
    outdated_packages_list = []
    for package in outdated_packages:
        outdated_packages_list.append(package.split())
    return outdated_packages_list

def update_package(package_name):
    subprocess.run(['pip', 'install', '--upgrade', package_name], check=True)

def main():
    outdated_packages = get_outdated_packages()
    print(outdated_packages)
    if not outdated_packages[0]:
        print("All the packages are updated")
    else:
        i = 0
        for package in outdated_packages:
            i+=1
            if(i>2):
                package_name = f'{package[0]}=={package[2]}'    
                print(f'Updating {package[0]}...')
                update_package(package_name)
        print('Update process completed.')

if __name__ == '__main__':
    main()
