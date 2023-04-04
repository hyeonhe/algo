-- 코드를 입력하세요


-- 조회수가 가장 높은 중고거래 게시물에 대한 첨부파일 경로를 조회
-- 첨부파일 경로는 FILE ID를 기준으로 내림차순
-- 기본적인 파일 경로는 /home/grep/src/
SELECT CONCAT('/home/grep/src/', B.BOARD_ID, '/', B.FILE_ID, FILE_NAME, FILE_EXT) as FILE_PATH FROM USED_GOODS_BOARD AS A, USED_GOODS_FILE AS B
WHERE A.BOARD_ID = B.BOARD_ID AND VIEWS = (SELECT MAX(VIEWS) FROM USED_GOODS_BOARD)
ORDER BY B.FILE_ID DESC