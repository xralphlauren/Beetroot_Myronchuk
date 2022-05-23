with open('access-log', 'r') as wwwlog:
    byte_column = (i.rsplit(maxsplit=1)[1] for i in wwwlog)
    byte_sent = (int(x) for x in byte_column if x.isdigit())
    print(sum(byte_sent))


