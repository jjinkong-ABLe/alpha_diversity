# alpha_diversity

Python 3.11 이상 표준 라이브러리만 사용하는 생물정보학 CLI입니다. AI 도움을 받아 작성했으며 예제는 합성 자료입니다.

## 실행

```console
python alpha_diversity.py examples/abundance.csv
python -m unittest -v
```

결과는 표준 출력으로 내보냅니다. 파일로 저장하려면 `> results.txt`를 붙이세요. 잘못된 입력은 오류 메시지와 종료 코드 2로 반환합니다.

## 4. Alpha diversity

입력은 `feature_id,sample_1,...` 풍부도 CSV입니다. 관측 풍부도 S, 자연로그 Shannon H, Gini-Simpson 1−Σp², Pielou H/ln(S)를 계산합니다. 빈 샘플은 richness=0이고 나머지는 빈 값이며, S≤1인 Pielou도 정의하지 않아 빈 값으로 둡니다. Rarefaction·오염 제거·샘플 간 통계 검정은 하지 않습니다. 시퀀싱 깊이와 전처리가 다른 자료의 지표를 단순 비교하지 마세요.

[scikit-bio 지표 정의](https://scikit.bio/docs/latest/diversity.html)

