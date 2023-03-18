-- 보호소에서 중성화 수술을 거친 동물 정보를 알아보려 합니다. 
-- 보호소에 들어올 당시에는 중성화1되지 않았지만, 보호소를 나갈 당시에는 
-- 중성화된 동물의 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회하는 SQL 문을 작성해주세요.
SELECT A_IN.ANIMAL_ID, A_IN.ANIMAL_TYPE, A_IN.NAME
FROM ANIMAL_INS A_IN INNER JOIN ANIMAL_OUTS A_OUT ON A_IN.ANIMAL_ID = A_OUT.ANIMAL_ID
WHERE A_IN.SEX_UPON_INTAKE LIKE '%INTACT%' 
AND (A_OUT.SEX_UPON_OUTCOME LIKE '%SPAYED%' OR A_OUT.SEX_UPON_OUTCOME LIKE '%NEUTERED%')
ORDER BY A_IN.ANIMAL_ID