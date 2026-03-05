## Reproducibility (Draft)

### 목표
- `generate_assets.py` 기준으로 표/그림을 재생성 가능한 형태로 유지
- 랜덤시드 및 라이브러리 버전 기록을 통해 동일 결과 재현

### 산출물
- `img/` 하위 그림 파일들(예: `ace_step.png`, `performance_benchmark.png`, 시뮬레이션 결과 그림)
- 표에 사용되는 요약값(시뮬레이션 결과 DataFrame/CSV가 있다면 함께 저장)

### 체크리스트
- 랜덤시드 고정(`numpy.random.seed`, 필요 시 기타 RNG 포함)
- 샘플 크기, 반복 횟수, permutation 횟수(B) 기록
- Python/R 패키지 버전 기록(예: `pip freeze`, R `sessionInfo()`)
