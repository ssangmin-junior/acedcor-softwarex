# 주간 개발/작성 보고서 (2026-03-03)

## 1) 보고 목적
이번 주 작업의 목표는 V3 기능(A1/A2/B1)을 “코드 구현” 수준에서 끝내지 않고, 실제 논문 본문(`swx.tex`)에 실험 결과와 해석까지 연결해 **재현 가능한 서술 구조**로 완성하는 것이었습니다.  
핵심은 다음 3가지입니다.
- A1: permutation test 결과를 type-I error/power 관점으로 제시
- A2: confounding 통제의 필요성을 수치+도식으로 명확히 제시
- B1: API 입력/출력 스키마 및 자동 권고 규칙을 본문에 명시

---

## 2) 이번 주 실제 변경 사항 (무엇을 바꿨는지)

### A1. Permutation test 실험 정식화 및 본문 반영
- 구현/산출
  - 실험 스크립트: `V3/scripts/generate_weekly_assets.py`
  - 원자료: `V3/a1_type1_power_summary.csv`
  - 그림: `img/a1_type1_power.png`
- 논문 반영 위치
  - 표: `tab:a1_type1_power`
  - 그림: `fig:a1_type1_power`
  - 실험 조건 문장: `N=180`, `B=99`, 반복 `25회`, `alpha=0.05`

### A2. Synthetic confounding 데모 정식화 및 본문 반영
- 구현/산출
  - 원자료: `V3/a2_confounding_summary.csv`
  - 그림: `img/a2_confounding_demo.png`
- 논문 반영 위치
  - 표: `tab:a2_confounding`
  - 그림: `fig:a2_confounding_demo`
- 추가 수정
  - 그림 인코딩 깨짐(특수기호) 이슈를 ASCII 문구로 교체해 재생성 완료

### B1. 입력/출력 스키마 + 자동 권고 규칙 명시
- 구현/산출
  - 본문 스키마 표 반영: `tab:v3_io_schema`
  - `dcor_test`, `acedcor_test`, `conditional_dependence_report`, `auto_diagnosis_report`의 입출력 명시
  - 자동 권고 규칙(\(\Delta dCor\) 기준) 문장 삽입
- 표 가독성 개선
  - `conditional_dependence_report` 행 줄바꿈 및 열폭 조정으로 칸 넘침 문제 수정

---

## 3) 실제 결과 값 (무엇이 나왔는지)

### A1 결과 (type-I error / power)
`V3/a1_type1_power_summary.csv` 기준:
- Independent: Raw `0.040`, After-ACE `0.080`
- Monotonic (`x^3`): Raw `1.000`, After-ACE `1.000`
- Symmetric (`x^2`): Raw `0.160`, After-ACE `0.160`

### A2 결과 (confounding 통제)
`V3/a2_confounding_summary.csv` 기준:
- Raw dCor: `0.8947`
- Residual dCor: `0.0673`
- Partial distance correlation: `0.0891`

---

## 4) 결과 해석 (이 값이 의미하는 바)

### A1 해석
- Independent 시나리오에서 기각률이 유의수준 근처(0.05 부근)에 위치하여, 검정이 과도하게 false positive를 내지 않음을 확인했습니다.
- Monotonic 시나리오에서는 강한 의존 구조를 안정적으로 검출했습니다.
- Symmetric 시나리오는 Monotonic 대비 낮은 기각률(0.160)로 나타나, 데이터 구조/신호강도 조건에서 검출 난이도가 다름을 보여줍니다.
- 즉, A1 표/그림은 “검정 기능이 작동한다”를 넘어서, **시나리오별 검출 난이도 차이**까지 보여주는 근거가 됩니다.

### A2 해석
- Raw dCor가 매우 높지만(`0.8947`), Z를 통제한 뒤 residual/partial 지표가 크게 감소(`0.0673`, `0.0891`)했습니다.
- 이는 X–Y의 관측 의존성이 상당 부분 confounder Z로 설명됨을 의미합니다.
- 즉, A2 결과는 “상관이 높다”는 관측만으로 인과적/직접적 관계를 해석하면 위험하다는 점을 명확히 보여줍니다.

### B1 해석
- 스키마 표(`tab:v3_io_schema`)를 통해 API 사용 진입장벽을 낮췄고,
- 자동 권고 규칙을 본문에 명시함으로써 결과 해석이 사용자 주관에만 의존하지 않도록 했습니다.
- 연구/실무 적용 관점에서 재현성과 해석 일관성을 동시에 강화한 변경입니다.

---

## 5) 실제 적용 효과 (어디에 어떻게 쓰이는지)
- 논문 독자 관점
  - “방법 소개”에서 끝나지 않고, 검정 성능(A1), confounder 통제 필요성(A2), API 적용 경로(B1)를 한 흐름으로 확인 가능
- 패키지 사용자 관점
  - 단순 dCor 값 확인에서 벗어나, `p-value`, `conditional check`, `auto report`까지 연계된 분석 파이프라인 사용 가능
- 투고 문서 품질 관점
  - 표/그림/본문 서술이 서로 참조되며, 결과-해석-적용 논리가 강화됨

---

## 6) 검증 및 반영 상태
- 빌드 검증 명령
  - `latexmk -pdf -interaction=nonstopmode -halt-on-error swx.tex`
- 결과
  - `swx.pdf` 정상 생성
  - 신규 표/그림/문장 반영 확인 완료

---

## 7) 다음 개선 제안
- A1 반복수(repeats) 확대 및 추가 신호강도 구간 실험으로 신뢰구간 제시
- A2에 다변량 Z(복수 confounder) 사례를 추가해 적용 범위 확장
- B1 스키마 표에 예외 처리(결측/상수열/비유한값) 항목 추가