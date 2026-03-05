# 개발/작성 리포트 (V3 적용 초안)

## A. 통계 방법 개발

### A1) 검정 모드(p-value) 추가: permutation test

- 목적: dCor, Delta dCor의 효과크기에 p-value를 결합하여 추정+검정 구조 제공.
- 귀무가설: H0: X ⫫ Y
- 대립가설: H1: X ⫫̸ Y
- 통계량: `T_obs = dCor_n(X, Y)`
- p-value 근사:

`p = (1 + sum(I(T_b >= T_obs))) / (B + 1)`

- 구현 API:
  - `dcor_test(x, y, B=999, method="perm", random_state=None)`
  - `acedcor_test(x, y, B=999, ...)`
- 제공 검정:
  - Raw dependence test
  - After-ACE dependence test
- 실험 계획(논문용):
  - 독립/단조/대칭 시나리오에서 type-I error와 power 표/그림 요약

### A2) 조건부 의존성: confounder 통제

- 목적: X-Y 의존이 Z에 의한 가짜 상관인지 진단.
- 구현:
  - Residualization + dCor (`partial_dcor_residual`)
  - Partial distance correlation (`partial_distance_correlation`, 단일 Z)
- 데모 권장:
  - synthetic confounding (X ⫫ Y | Z), raw dCor는 큼 / partial은 작음

## B. 소프트웨어 개발

### B1) 자동 리포트(단일 함수)

- 함수: `auto_diagnosis_report(...)`
- 고정 출력:
  - Pearson before/after(ACE)
  - dCor before/after(ACE)
  - Delta dCor
  - 옵션 p-value
  - 룰 기반 결론 문장
  - 최소 2개 그림(raw, after-ACE)
- 산출 경로: `output_dir` 하위 PNG 파일 자동 저장

## 입력/출력 스키마(요약)

- 입력: `x: 1D`, `y: 1D`, `B: int`, `random_state: Optional[int]`
- 출력:
  - test: `(stat, pvalue)` 또는 dict
  - report: 수치 요약 + 권고문 + 그림 경로 dict

## 참고문헌

- Székely et al. (2007)
- Székely and Rizzo (2014)