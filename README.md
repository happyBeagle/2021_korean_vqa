# 2021_korean_vqa

## 프로젝트 구조

```
.
├── data
│   ├── raw_data
│   │   ├── train
│   │   │   └── 원천데이터
│   │   │       ├── 스포츠
│   │   │       │   └── 대본X
│   │   │       ├── 예능교양
│   │   │       │   ├── 대본O
│   │   │       │   └── 대본X
│   │   │       └── 생활안전
│   │   │           ├── 대본O
│   │   │           └── 대본X
│   │   │   └── 라벨링데이터
│   │   │       ├── 스포츠
│   │   │       │   └── 대본X
│   │   │       │       └── output.json
│   │   │       ├── 예능교양
│   │   │       │   ├── 대본O
│   │   │       │   │   └── output.json
│   │   │       │   └── 대본X
│   │   │       │       └── output.json
│   │   │       └── 생활안전
│   │   │           ├── 대본O
│   │   │           │   └── output.json
│   │   │           └── 대본X
│   │   │               └── output.json
│   │   └── test # train과 동일
│   │    
│   ├── test.json
│   └── train.json
├── infer.sh
├── requirements.txt
├── preprocess.py
├── run.py
└── run.sh
```
### data
- 초기 상태에는 [baselinee 코드](https://github.com/Surromind-AI/videonarrative)에서 제공된 `raw_data` 만 존재합니다.
- `train.json`, `test.json` 파일은 이후에 `preprocess.py` 파일을 통해 생성합니다.

## 사용법
### Clone
``` bash
git clone https://github.com/happyBeagle/2021_korean_vqa.git
```
### Install requirements
``` bash
pip install -r requirements.txt
```
### Download raw data
- [baseline repository](https://github.com/Surromind-AI/videonarrative) 에서 raw_data 를 다운 받아 `data` 디렉토리 안에 둡니다

### Preprocess raw data
``` bash
python preprocess.py
```
### Train
``` bash
sh run.sh
```
### Inference
``` bash
sh infer.sh
```

## Reference
- [huggingface transformers](https://github.com/huggingface/transformers)
