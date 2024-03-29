SELECT
A.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY,
SUM(S.SALES* B.PRICE) AS TOTAL_SALES
FROM BOOK AS B
JOIN AUTHOR AS A ON B.AUTHOR_ID = A.AUTHOR_ID
JOIN (SELECT BOOK_ID, SUM(SALES) as SALES FROM BOOK_SALES
     WHERE YEAR(SALES_DATE) = '2022' AND MONTH(SALES_DATE) = '01'
     GROUP BY BOOK_ID) AS S ON B.BOOK_ID = S.BOOK_ID
GROUP BY AUTHOR_ID, CATEGORY
ORDER BY AUTHOR_ID ASC, CATEGORY DESC