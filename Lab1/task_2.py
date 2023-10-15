# TODO Найдите количество книг, которое можно разместить на дискете

vol = 1.44
page_cnt = 100
str_cnt = 50
sym_cnt = 25
vol_sym = 4


book_count = int(vol * 1024 * 1024/ (page_cnt * str_cnt * sym_cnt * vol_sym))
print("Количество книг, помещающихся на дискету:", book_count)
