def after_100(mm, dd, week):
    # dictionary = {'일': 0, '월': 1, '화': 2, '수': 3, '목': 4, '금': 5, '토': 6}
    array = ['일', '월', '화', '수', '목', '금', '토']
    month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    after_mm = mm

    p = array.index(week)
    after_dd = dd
    n = 100
    
    


        
    # print(after_mm, after_dd, array[p])
    print(f'{mm}월 {dd}일 {week}요일부터 100일 뒤는 {after_mm}월 {after_dd}일 {array[p]}요일')



after_100(6, 21, "월")