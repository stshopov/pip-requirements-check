import argparse


def get_elements(source):
    container = []
    for element in source:
        container.append(element.rstrip('\n'))

    return container


def get_only_name(packages):
    package_names = []
    for p in packages:
        if p[:6] == "-e git":
            package_names.append(p)
        else:
            package_names.append(p.split('==')[0])

    return package_names


def check_all_packages(list1, list2, names1, names2):
    new_dict = {}
    new_dict1 = {}

    for package in list1:
        if package in list2:
            new_dict[package] = package
        elif package not in list2:
            if package[:6] != "-e git" and package.split('==')[0] in names2:
                package_index = names2.index(package.split('==')[0])
                new_dict[package] = list2[package_index]
            elif package[:6] == "-e git" and package in names2:
                package_index = names2.index(package)
                new_dict[package] = list2[package_index]
            else:
                new_dict[package] = "None"
    for package in list2:
        if package not in list1:
            if package[:6] != "-e git" and package.split('==')[0] not in names1:
                new_dict1[package] = "None"
            elif package[:6] == "-e git" and package not in names1:
                new_dict1[package] = "None"

    return new_dict, new_dict1


def main():
    parser = argparse.ArgumentParser(description='requirements-files-tool')
    parser.add_argument('--source1', type=str, required=True, dest='source1')
    parser.add_argument('--source2', type=str, required=True, dest='source2')

    args = parser.parse_args()
    file1 = args.source1
    file2 = args.source2

    source1 = open(file1)
    source2 = open(file2)

    source1_packages = get_elements(source1)
    source2_packages = get_elements(source2)
    packages1_names = get_only_name(source1_packages)
    packages2_names = get_only_name(source2_packages)

    dict1, dict2 = check_all_packages(source1_packages, source2_packages, packages1_names, packages2_names)

    for element in dict1:
        if dict1[element] == "None":
            print("\033[91m {}\033[00m".format(element), "\033[91m {}\033[00m".format(dict1[element]))
        elif dict1[element] == element:
            print("\033[92m {}\033[00m".format(element), "\033[92m {}\033[00m".format(dict1[element]))
        elif dict1[element] != element and element != 'None':
            print("\033[93m {}\033[00m".format(element), "\033[93m {}\033[00m".format(dict1[element]))

    for element in dict2:
        if dict2[element] == "None":
            print("\033[91m {}\033[00m".format(dict2[element]), "\033[91m {}\033[00m".format(element))

    source2.close()
    source1.close()


if __name__ == '__main__':
    main()
