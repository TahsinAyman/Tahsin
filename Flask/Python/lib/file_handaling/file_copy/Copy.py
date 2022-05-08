# def copy(source_file: str, copy_file: str):
#     with open(source_file, 'w') as input_file:
#         with open(copy_file) as output_file:
#             input_file.write(output_file.read())


def copyIshan(source_file, dest_file):
    with open(source_file, 'r') as main:
        with open(dest_file, 'w') as coppy:
            coppy.write(main.read())


def copyTahsin(source_file: str, desitination_file: str):
    with open(source_file, 'r') as input_file:
        with open(desitination_file, 'w') as output_file:
            output_file.write(input_file.read())


def copyPro(srcfile, desfile):
    with open(srcfile, 'r') as main:
        with open(desfile, 'w') as copy:
            copy.write(main.read())


copyTahsin('file.txt', 'file copy.txt')
