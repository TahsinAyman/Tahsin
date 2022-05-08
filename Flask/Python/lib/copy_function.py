def copy(source_file: str, copy_file: str):
    with open(source_file, 'w') as input_file:
        with open(copy_file) as output_file:
            input_file.write(output_file.read())


copy('')