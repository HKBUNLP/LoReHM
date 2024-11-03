import os
import warnings
from PIL import Image
import json
from termcolor import colored
from utils.utils import *
import utils.constants
import argparse
from os import path as osp
from tqdm import tqdm
from datetime import datetime
warnings.filterwarnings("ignore")


parser = argparse.ArgumentParser()

parser.add_argument('--dataset_name', type=str)
parser.add_argument('--model', type=str, default='llava-v1.6-34b')
parser.add_argument('--rsa', action='store_true', help='Relative Sample Augmentation')
parser.add_argument('--rsa_k', type=int, default=5)
parser.add_argument('--mia', action='store_true', help='Meme Insight Augmentation')
parser.add_argument('--log_dir', type=str, default=f'logs/{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}')
cli_args = parser.parse_args()


if cli_args.model.split("-")[0]=='llava':
    from utils.run_llava import run_proxy
    model_path = f"liuhaotian/{cli_args.model}"
    proxy = run_proxy(model_path, None)
    args = type('Args', (), {
        "query": None,
        "conv_mode": None,
        "image_file": None,
        "sep": ",",
        "temperature": 0,
        "top_p": None,
        "num_beams": 1,
        "max_new_tokens": 1024,
    })()


basic_prompt, rsa_prompt = utils.constants.BASIC_PROMPT, utils.constants.RSA_PROMPT
if cli_args.mia:
    meme_insight = utils.constants.MEME_INSIGHTS[cli_args.model][cli_args.dataset_name]

os.makedirs(cli_args.log_dir, exist_ok=True)
result_path = osp.join(cli_args.log_dir, "result.jsonl")

if not os.path.exists(result_path):
    with open(osp.join(cli_args.log_dir, "args.json"), 'w') as f:
        json.dump(vars(cli_args), f)
    start_idx, y_true, y_pred = 0, [], []
else:
    start_idx, y_true, y_pred = breakpoint_resume(result_path)

test_set = Dataset(cli_args.dataset_name, rsa=cli_args.rsa)


f = open(result_path, 'a')
results = []
labels_str = ['harmless', 'harmful']

for idx, image, text, label, rel_sampl in tqdm(test_set):
    if idx < start_idx:
        continue

    trajectory = []
    args.image_file = image

    args.query = basic_prompt.format(text)
    if cli_args.mia:
        args.query += f'\nNote:\n{meme_insight}\n'
    
    print(colored(args.query, "yellow"))
    response = proxy.run_model(args)
    print(colored(response + '\n', "red"))
    trajectory.append(args.query)
    trajectory.append(response)
    answer, basic_predict = parse_answer(response, 'Answer:')

    if cli_args.rsa:
        rsa_label = get_rsa_label(rel_sampl, cli_args.rsa_k)
        if basic_predict != rsa_label:
            print(f'Basic Predict: {basic_predict}, RSA Label: {rsa_label}')
            args.query = rsa_prompt.format(text, labels_str[rsa_label])
            if cli_args.mia:
                args.query += f'\nNote:\n{meme_insight}\n'

            print(colored(args.query, "yellow"))
            response = proxy.run_model(args)
            print(colored(response + '\n', color="green"))
            trajectory.append(args.query)
            trajectory.append(response)

            answer, predict = parse_answer(response, 'Answer:')
        else:
            predict = basic_predict
    else:
        predict = basic_predict

    y_true.append(label)
    y_pred.append(predict)
    print(f'Label: {label}, Predict: {predict}')
    matrix, macro_f1, _ = compute_metrics(y_true, y_pred)

    result = {'index': idx, 'matrix': matrix, 'macro_f1': macro_f1, 'label': label, 'predict': predict, 'image': image, 'text': text, 'trajectory': trajectory}
    if cli_args.rsa:
        result['rsa_label'] = rsa_label
    json.dump(result, f)
    f.write('\n')