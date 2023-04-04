-- 코드를 입력하세요
# SELECT USER_ID, NICKNAME, CONCAT(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) AS '전체주소',
# CONCAT(SUBSTR(TLNO, 1, 3), '-', SUBSTR(TLNO, 4, 4), '-', SUBSTR(TLNO, 7, 4)) AS '전화번호'
# FROM USED_GOODS_USER
# WHERE USER_ID IN (SELECT WRITER_ID
#                  FROM USED_GOODS_BOARD
#                  GROUP BY WRITER_ID
#                  HAVING COUNT(WRITER_ID) >= 3)
# ORDER BY USER_ID DESC


# SELECT user_id
#      , nickname
#      , CONCAT(city, " ", street_address1, " ", street_address2) AS address
#      , CONCAT(LEFT(tlno,3),"-",SUBSTR(tlno,4,4),"-",RIGHT(tlno,4)) AS tlno
# FROM used_goods_user
# WHERE user_id IN (SELECT writer_id
#                   FROM used_goods_board
#                   GROUP BY writer_id
#                   HAVING COUNT(*)>=3)
# ORDER BY user_id DESC

select user_id, nickname, 
    concat(city, ' ', street_address1, ' ', street_address2) '전체주소',
    concat(left(tlno, 3), '-', mid(tlno, 4, 4), '-', substr(tlno,8)) '전화번호'
from used_goods_user
where user_id in (select writer_id
        from used_goods_board
        group by writer_id
        having count(writer_id) >= 3)
order by user_id desc;