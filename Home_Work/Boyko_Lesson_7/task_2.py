class Mathematician:
    def square_nums(self, lst):
        out_list = []
        for i in lst:
            out_list.append(i * i)
        return out_list

    def remove_positives(self, lst):
        out_list = []
        for i in lst:
            if i < 0:
                out_list.append(i)
        return out_list

    def filter_leaps(self, lst):
        our_list = []
        for i in lst:
            if i % 4 == 0 and i % 100 != 0:
                our_list.append(i)
        return our_list


m = Mathematician()
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
