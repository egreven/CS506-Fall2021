def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    with open(csv_file_path, "r") as d:
        data = d.readlines()
        X = []
        for line in data:
            words = line.split(',')
            X += [words]
        return X
