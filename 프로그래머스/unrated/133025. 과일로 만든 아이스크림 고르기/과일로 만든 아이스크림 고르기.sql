SELECT A.FLAVOR FROM FIRST_HALF AS A, ICECREAM_INFO AS B

WHERE A.FLAVOR = B.FLAVOR AND A.TOTAL_ORDER >= 3000 AND INGREDIENT_TYPE = 'FRUIT_BASED'
ORDER BY A.TOTAL_ORDER DESC