-- 코드를 입력하세요
SELECT US.USER_ID AS USER_ID, NICKNAME, CONCAT(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) AS '전체주소', CONCAT(SUBSTRING(TLNO,1,3),'-',SUBSTRING(TLNO,4,4),'-',SUBSTRING(TLNO,8,4)) AS '전화번호'
FROM USED_GOODS_BOARD AS BOARD JOIN USED_GOODS_USER AS US ON BOARD.WRITER_ID = US.USER_ID
GROUP BY US.USER_ID
HAVING COUNT(*) >= 3
ORDER BY US.USER_ID DESC