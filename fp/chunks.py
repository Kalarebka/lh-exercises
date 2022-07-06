# Write function that splits given list into random chunks of length from 4 to 7
# Last chunk has to be from 4 to 7 length max
# Custom chunk lengths
from random import randint

alphabet = [x for x in "abcdefghijklmnoprstuwxyz"]


def to_chunks(data: list, min_length: int, max_length: int):
    chunk_len = randint(min_length, max_length)
    if len(data) <= min_length + max_length:
        return [data[:chunk_len], data[chunk_len:]]
    else:
        new_data =[data[:chunk_len],]
        new_data.extend(to_chunks(data[chunk_len:], min_length, max_length))
        return new_data


chunks = to_chunks(alphabet, 4, 7)
print(chunks)

# chunks:
# [[a,b,c,d,e,f],[g,h,i,j,k],[l,m,n,o,p,r,s],[t,u,w,x,y,z]]