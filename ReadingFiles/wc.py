def wc(file):
    with open(file, 'r') as f:
        # reading the file into a list
        content = f.read().splitlines()

        lines = len(content)

        words = 0
        for line in content:
            words += len(line.split())

        chars = 0
        for line in content:
            print(list(line))
            chars += len(list(line))

        return lines, words, chars

print(wc('sample_file.txt'))