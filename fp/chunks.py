# Write function that splits given list into random chunks of length from 4 to 7
# Last chunk has to be from 4 to 7 length max
# Custom chunk lengths
from random import randint

alphabet = [x for x in "abcdefghijklmnoprstuwxyz"]


def to_chunks(data: list, min_length: int, max_length: int):
    if len(data) <= max_length:
        return [data,]
    if len(data) <= 2 * max_length:
        chunk_len = randint(len(data) - max_length, max_length)
        return [data[:chunk_len], data[chunk_len:]]
    else:
        chunk_len = randint(min_length, max_length)
        new_data = [
            data[:chunk_len],
        ]
        new_data.extend(to_chunks(data[chunk_len:], min_length, max_length))
        return new_data


chunks = to_chunks(alphabet, 1, 30)
print(chunks)
