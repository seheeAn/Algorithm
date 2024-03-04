-- 코드를 입력하세요
SELECT
COUNT(DISTINCT(NAME)) AS count
FROM ANIMAL_INS
WHERE NAME IS NOT NULL

-- DISTINCT는 NULL도 하나의 종류로 본다.
-- 하지만 COUNT는 NULL을 세지 않는다.
-- 따라서 해당 WHERE절은 없어도 된다.