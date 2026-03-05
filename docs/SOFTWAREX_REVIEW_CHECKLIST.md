# SoftwareX 심사 대응 체크리스트 (라인별)

대상 파일: `swx.tex`

## A. 저널 필수 요건 정합성

- [x] **코드/저장소 영구 접근 링크 명시**  
  - 위치: `swx.tex:163`
- [x] **소프트웨어 메타데이터 표 제공**  
  - 위치: `swx.tex:145`, `swx.tex:153`, `swx.tex:154`
- [x] **설치/실행 진입점 제공(Software Functionalities)**  
  - 위치: `swx.tex:220`

## B. 재현성(SoftwareX 핵심) 강화

- [x] **GitHub 업로드 번들 참조 문장 추가**  
  - 위치: `swx.tex:231`
  - 내용: `github_release_package/` 경로와 URL 직접 명시
- [x] **API 입출력 스키마 표 제공**  
  - 위치: `swx.tex:261` (`tab:v3_io_schema`)

## C. 실험 결과 제시/해석 일관성

- [x] **A1 permutation type-I/power 표 반영**  
  - 위치: `swx.tex:478` (`tab:a1_type1_power`)
- [x] **주요 시뮬레이션 요약표(고차 시나리오 확장 포함)**  
  - 위치: `swx.tex:501` (`tab:results_summary`)
- [x] **dCor 개선 순위표(랭크 정렬 반영)**  
  - 위치: `swx.tex:543` (`tab:improvement_rank`)

## D. 확장 시나리오/실사용성 보강

- [x] **High-order + heteroscedasticity 소절 추가**  
  - 위치: `swx.tex:606`
- [x] **해당 그림 라벨/참조 연결**  
  - 위치: `swx.tex:615` (`fig:high_order_heteroscedasticity`)
- [x] **Confounding 통제 데모 소절 명확화**  
  - 위치: `swx.tex:618`, `swx.tex:623` (`tab:a2_confounding`)
- [x] **실데이터 적용 결과 표 유지**  
  - 위치: `swx.tex:649` (`tab:real_data_results`)

## E. 마무리 섹션 정합성

- [x] **결론/향후계획에 방법론 및 확장 방향 반영**  
  - 위치: `swx.tex:714`

## F. GitHub 업로드 전 최종 확인 권고

- [ ] `github_release_package/README.md`의 경로와 실제 업로드 경로 일치 확인
- [ ] 저장소 푸시 후 URL 접근 확인
- [ ] `swx.tex` 재컴파일 후 링크/라벨 깨짐 확인
