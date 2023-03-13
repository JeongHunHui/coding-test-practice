WITH RESTOURANTS_RANK AS(
    SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES,
    ROW_NUMBER() OVER(PARTITION BY FOOD_TYPE
                      ORDER BY FAVORITES DESC
                     ) AS ROW_NUM
    FROM REST_INFO)
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM RESTOURANTS_RANK
WHERE ROW_NUM = 1
ORDER BY FOOD_TYPE DESC