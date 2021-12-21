# 2021_korean_vqa
[2021 한국어 질의응답 AI 경진대회: 비디오 네러티브 질의응답 태스크](http://ai-competition.kaist.ac.kr/) 애서 사용한 솔루션입니다.
## 대회 설명
<img src='https://user-images.githubusercontent.com/57934461/146944769-a62a0b8f-4a19-4a47-85e8-4818f9ef8ce6.jpg' width=500 />

### 개요

비디오 네러티브 질의응답이란 영상(4~5초)에 대한 질문이 주어졌을 때 해당 질문에 대한 답을 보기에서 찾는 태스크로서, 기존의 이미지에 대한 질문에 답하는 VQA 문제에 시간축이 추가된 태스크임. 본 태스크는 영상정보와 자연어 정보에 대한 이해를 바탕으로 각각 다른 modality 정보를 활용하여 학습하여, 주어진 자연어 질문에 대한 가장 적합한 답을 찾는 문제임.


예를 들어, 빨간색 유니폼을 입은 선수가 오른쪽으로 뛰는 영상에 대해 다음과 같은 질문과 보기가 주어짐.
```
질문: 오른쪽으로 뛰는 사람이 어떤 옷을 입었습니까?
보기: 1. 한복, 2. 소방복, 3. 운동복, 4. 경찰복, 5. 수술복
```
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
## To Do
- [ ] Use image features
## Reference
- [huggingface transformers](https://github.com/huggingface/transformers)
