/*
CAR_RENTAL_COMPANY_CAR 테이블과 
CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블과 CAR_RENTAL_COMPANY_DISCOUNT_PLAN 테이블에서 
자동차 종류가 '세단' 또는 'SUV' 인 자동차 중 
2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고 
30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차에 대해서 
자동차 ID, 자동차 종류, 대여 금액(컬럼명: FEE) 리스트를 출력하는 SQL문을 작성해주세요. 
결과는 대여 금액을 기준으로 내림차순 정렬하고, 
대여 금액이 같은 경우 자동차 종류를 기준으로 오름차순 정렬, 
자동차 종류까지 같은 경우 자동차 ID를 기준으로 내림차순 정렬해주세요.
*/
-- 0.9라는 할인율을 변수로 가져와야되는데 이걸 모르겠다. CASE로 해결해야되나?

-- 메인 쿼리 시작
SELECT
    A.CAR_ID,          -- 차량 아이디
    A.CAR_TYPE,        -- 차량 유형 (세단 또는 SUV)
    A.FEE              -- 할인된 월간 비용
FROM (
    -- 서브쿼리 시작
    SELECT 
        C.CAR_ID,      -- 차량 아이디
        C.CAR_TYPE,    -- 차량 유형 (세단 또는 SUV)
        C.DAILY_FEE,   -- 차량의 일일 요금
        ROUND((C.DAILY_FEE * (100-D.DISCOUNT_RATE)/100) * 30) FEE,  -- 할인 적용된 월간 비용
        D.DISCOUNT_RATE,   -- 할인율
        D.DURATION_TYPE,   -- 할인 요금제의 기간 유형
        H.START_DATE,      -- 대여 시작 날짜
        H.END_DATE         -- 대여 종료 날짜
    FROM CAR_RENTAL_COMPANY_CAR C
        -- 렌탈 기록과 차량 테이블 왼쪽 조인
        LEFT JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H
        ON C.CAR_ID=H.CAR_ID
        -- 할인 플랜과 차량 테이블 조인
        JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN D
        ON C.CAR_TYPE=D.CAR_TYPE
    WHERE C.CAR_TYPE IN ('세단', 'SUV')  -- 세단과 SUV 차량만 대상
        AND D.DURATION_TYPE IN (30)      -- 30일 할인 요금제만 대상
    GROUP BY
        C.CAR_ID, D.DISCOUNT_RATE, D.DURATION_TYPE
) A
WHERE
    A.FEE BETWEEN 500000 AND 2000000     -- 월간 비용이 500,000원에서 2,000,000원 사이인 경우만 대상
    AND (DATEDIFF(A.END_DATE,'2022-11-01') < 0
    OR DATEDIFF(A.START_DATE,'2022-11-30') > 0)  -- 2022년 11월에 대여 가능한 차량만 대상
ORDER BY
    A.FEE DESC, A.CAR_TYPE ASC, A.CAR_ID DESC  -- 결과를 월간 비용 내림차순, 차량 유형 오름차순, 차량 아이디 내림차순으로 정렬