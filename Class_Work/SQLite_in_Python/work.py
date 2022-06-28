import wh

w = wh.WH('white_house_2017_salaries_com.csv')
#print(dir(w))
#print(w.sotr)
#print(dir(w.sotr[0]))


w.save_to_sql('wh.db')