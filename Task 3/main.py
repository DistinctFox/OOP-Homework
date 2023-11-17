import os
from pprint import pprint


if __name__ == '__main__':
    ls = [i for i in os.listdir() if i.endswith('.txt')]
    ls.sort()
    if 'result.txt' in ls:
        ls.remove('result.txt')
    with open('result.txt', 'w', encoding='utf-8') as f:
        all_files_data = []
        for j in ls:
            s = open(j, encoding='utf - 8').read()
            all_files_data.append(j + '\n' + str(s.count('\n')+1) + '\n' + s + '\n\n')

        all_files_data.sort(key=len)
        for file_data in all_files_data:
            f.write(file_data)
