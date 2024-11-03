# LoReHM

[EMNLP 2024] Towards Low-Resource Harmful Meme Detection with LMM Agents

## Install

1. Clone the repo
```
git clone https://github.com/Jianzhao-Huang/LoReHM.git
cd LoReHM
```

2. Install Package
```
conda create -n lorehm python=3.10 -y
conda activate lorehm
pip install -r requirements.txt
```

## Dataset

Please obtain FHM, harM, and MAMI, and place them in the following directories: 

- LoReHM/datasets/FHM
- LoReHM/datasets/harmC
- LoReHM/datasets/MAMI

## Inference
Edit the command line args to change inference settings.

```
python main.py \
--dataset_name FHM \
--model 'llava-v1.6-34b' \
--rsa \
--mia
```