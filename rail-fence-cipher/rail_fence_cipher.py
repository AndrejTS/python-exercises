from itertools import cycle


def encode(message, rails):
    rails_matrix = make_matrix(message, rails)
    rail_index = make_sequence(rails)
    for i in range(len(message)):
        rails_matrix[next(rail_index)][i] = message[i]
    return ''.join([k for i in rails_matrix for k in i])


def decode(encoded_message, rails):
    decoded = ''
    rails_matrix = make_matrix(encoded_message, rails)
    rail_index = make_sequence(rails)
    for i in range(len(encoded_message)):
        rails_matrix[next(rail_index)][i] = '?'
    for rail in rails_matrix:
        for i in range(len(rail)):
            if rail[i] == '?':
                rail[i] = encoded_message[0]
                encoded_message = encoded_message[1:]
    rail_index = make_sequence(rails)
    for i in range(len(rails_matrix[0])):
        decoded += rails_matrix[next(rail_index)][i]
    return decoded


def make_sequence(num_rails):
    sequence = []
    for i in range(num_rails):
        sequence.append(i)
    for i in range(num_rails - 2, 0, -1):
        sequence.append(i)
    return cycle(sequence)


def make_matrix(message, num_rails):
    matrix = []
    for _ in range(num_rails):
        matrix.append(['' for _ in range(len(message))])
    return matrix


