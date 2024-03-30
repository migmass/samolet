from contextlib import ExitStack

filenames=["file1.txt", "file2.txt", "file3.txt"]

with open('outfile.txt', 'a') as outfile:
    with ExitStack() as stack:
        file_pointers = [stack.enter_context(open(file, 'r'))
                         for file in filenames]
        for fp in file_pointers:
            outfile.write(fp.read())