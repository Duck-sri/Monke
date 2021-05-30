from hashlib import sha256



def sha_sum(string):
    h = sha256(string.encode('utf-8')).hexdigest()
    return h