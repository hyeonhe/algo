-- 코드를 입력하세요
SELECT CAR_TYPE, COUNT(CAR_TYPE) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
# WHERE OPTIONS REGEXP '^(가죽시트|열선시트|통풍시트)%'
WHERE OPTIONS LIKE '%통풍시트%'
OR OPTIONS LIKE '%열선시트%'
OR OPTIONS LIKE '%가죽시트%'
# WHERE OPTIONS IN ('통풍시트', '열선시트', '가죽시트')
GROUP BY CAR_TYPE
# HAVING COUNT(CAR_TYPE)
ORDER BY CAR_TYPE ASC
