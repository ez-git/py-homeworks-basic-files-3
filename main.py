def analyse(filename):
    with open(filename) as file:
        quantity = 0
        content = ''
        while True:
            line = file.readline()
            if line:
                content += line
                quantity += 1
            else:
                return [quantity, content]


def get_result_file(filename1, filename2, filename3):
    filenames = {filename1: analyse(filename1),
                 filename2: analyse(filename2),
                 filename3: analyse(filename3)}

    sorted_files = dict(sorted(filenames.items(), key=lambda item: item[1][0]))
    with open('4.txt', 'w') as file4:
        for key, value in sorted_files.items():
            file4.write(f'{key}\n{value[0]}\n{value[1]}\n')


get_result_file('1.txt', '2.txt', '3.txt')
