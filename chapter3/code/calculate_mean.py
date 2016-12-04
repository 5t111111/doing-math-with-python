'''
Calculating the mean od numbers stored in a file
'''


def read_data(filename):
    numbers = []

    with open(filename) as f:
        for line in f:
            numbers.append(float(line))

    return numbers


def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s / N

    return mean


if __name__ == '__main__':
    data = read_data('mydata.txt')
    mean = calculate_mean(data)
    print('Mean: {0}'.format(mean))
