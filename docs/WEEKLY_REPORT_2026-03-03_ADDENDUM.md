# 주간 개발/작성 보고서 보강 (2026-03-03)

## A3) High-order + Heteroscedasticity 실험 반영

이번 주 보고서 내용에 추가로, `before_paper/img/high_order_heteroscedasticity.png` 기반 결과를 본문에 반영했습니다.

- 반영 위치: `swx.tex`의 시뮬레이션 결과 파트
- 새 소절: **High-Order Nonlinearity Under Heteroscedastic Noise**
- 새 그림: `img/high_order_heteroscedasticity.png` (라벨: `fig:high_order_heteroscedasticity`)

### 추가된 핵심 메시지

- 기본 시나리오(`x^2`, `x^3`)보다 어려운 조건(고차 비선형 + 이분산 오차)에서도 의존성 검출 프레임워크를 점검함.
- 특히 `x^3, x^5, x^7, x^9`와 같은 고차 단조 패턴에서 함수 차수와 잡음 구조에 따라 검출 강도/순위가 변할 수 있음을 명시함.
- 따라서 단일 지표(예: Pearson)만으로 결론내리기보다, `dCor before`, `dCor after ACE`, `ΔdCor`를 함께 보는 해석이 필요하다는 점을 강조함.

### 기대 효과

- 보고서의 실험 스코프가 “기본 비선형”에서 “고차 + 현실적 잡음 구조”까지 확장되어, 방법론의 실무 적용 설득력이 강화됨.
- 다음 단계(`x^3, x^5, x^7, x^9` 확장 실험)와도 자연스럽게 연결되는 서술 구조를 확보함.# 주간 개발/작성 보고서 보강 (2026-03-03)

## A3) High-order + Heteroscedasticity 실험 반영

이번 주 보고서 내용에 추가로, `before_paper/img/high_order_heteroscedasticity.png` 기반 결과를 본문에 반영했습니다.

- 반영 위치: `swx.tex`의 시뮬레이션 결과 파트
- 새 소절: **High-Order Nonlinearity Under Heteroscedastic Noise**
- 새 그림: `img/high_order_heteroscedasticity.png` (라벨: `fig:high_order_heteroscedasticity`)

### 추가된 핵심 메시지

- 기본 시나리오(`x^2`, `x^3`)보다 어려운 조건(고차 비선형 + 이분산 오차)에서도 의존성 검출 프레임워크를 점검함.
- 특히 `x^3, x^5, x^7, x^9`와 같은 고차 단조 패턴에서 함수 차수와 잡음 구조에 따라 검출 강도/순위가 변할 수 있음을 명시함.
- 따라서 단일 지표(예: Pearson)만으로 결론내리기보다, `dCor before`, `dCor after ACE`, `ΔdCor`를 함께 보는 해석이 필요하다는 점을 강조함.

### 기대 효과

- 보고서의 실험 스코프가 “기본 비선형”에서 “고차 + 현실적 잡음 구조”까지 확장되어, 방법론의 실무 적용 설득력이 강화됨.
- 다음 단계(`x^3, x^5, x^7, x^9` 확장 실험)와도 자연스럽게 연결되는 서술 구조를 확보함.