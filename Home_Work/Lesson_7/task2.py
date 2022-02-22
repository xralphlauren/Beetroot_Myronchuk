def make_country(country, capital):
    dict_country = dict()
    dict_country[country] = capital
    return dict_country


x = make_country('Ukraine', 'Kyiv')
print(x['Ukraine'])