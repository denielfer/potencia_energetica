def get_all_files_from_directory(directory):
    files = []
    from os import walk
    for p, d, arquivo in walk(directory):
        for a in arquivo: #concatena path com file name
            files.append(p+"/"+a)
    return files