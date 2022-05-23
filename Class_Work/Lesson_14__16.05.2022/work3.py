with open('access-log', 'r') as wwwlog:
    pages_404 = (int(i.rsplit(maxsplit=1)[1]) for i in wwwlog if '404' in i.rsplit(maxsplit=2)[1])
    print(sum(pages_404))

