import json
from sklearn.metrics import classification_report, confusion_matrix
from openai import OpenAI
import base64
from time import sleep
import random
from os import path as osp
import os
import dotenv

SUPPORT_DATASETS = ('harmC', 'FHM', 'MAMI')


class Dataset():
    def __init__(self, name, rsa=False):
        if name not in SUPPORT_DATASETS:
            raise ValueError('Invalid Dataset Name')

        dotenv.load_dotenv()
        
        dataset_path_info = json.loads(os.getenv('DATASET_PATH_INFO'))[name]
        data_dir, annot_dir = dataset_path_info['DATA_DIR'], dataset_path_info['ANNOT_DIR']
        basic_annot_fn, rel_samp_fn = dataset_path_info['BASIC_ANNOT_FN'], dataset_path_info['REL_SAMPL_FN']

        self.data = [json.loads(line) for line in open(osp.join(data_dir, annot_dir, basic_annot_fn)).readlines()]
        rel_sampl_data = [json.loads(line) for line in open(osp.join(data_dir, annot_dir, rel_samp_fn)).readlines()]

        if rsa:
            for i in range(len(self.data)):
                self.data[i]['rel_sampl'] = (rel_sampl_data[i]['example'], rel_sampl_data[i]['harmful_example'], rel_sampl_data[i]['harmless_example'])
        
        match name:
            case 'harmC':
                for i in range(len(self.data)):
                    self.data[i]['image'] = data_dir + f"images/{self.data[i]['image']}"
                    self.data[i]['label'] = 0 if self.data[i]['labels'][0] == 'not harmful' else 1
                    self.data[i]['text'] = self.data[i]['text'].replace("\n", ' ')
            case 'FHM':
                for i in range(len(self.data)):
                    self.data[i]['image'] = data_dir + f"images/{self.data[i]['img']}"
                    self.data[i]['text'] = self.data[i]['org_sent'].replace("\n", ' ')
            case 'MAMI':
                for i in range(len(self.data)):
                    self.data[i]['image'] = data_dir + f"images/{self.data[i]['image']}"

        
    def __getitem__(self, index):
        return index, self.data[index]['image'], self.data[index]['text'], self.data[index]['label'], self.data[index].get('rel_sampl', None)

    def __len__(self):
        return len(self.data)


def compute_metrics(y_true, y_pred, is_print=True):
    matrix, report, report_str = confusion_matrix(y_true, y_pred).tolist(), classification_report(y_true, y_pred, output_dict=True), classification_report(y_true, y_pred)
    macro_f1 = round(report['macro avg']['f1-score']*100, 2)
    if is_print:
        print(matrix)
        print(f'Macro-F1: {macro_f1}')
    return matrix, macro_f1, report_str


def parse_answer(judge_result, sep):
    answer = judge_result.split(sep)[-1].split('.')[0].split(',')[0].lower().strip()
    if 'harmless' in answer:
        predict = 0
    elif 'harmful' in answer:
        predict = 1
    else:
        print("Judge output error!")
        answer = "skip"
        predict = 1
    
    return answer, predict


def breakpoint_resume(result_path):
    with open(result_path, 'r') as f:
        lines = [json.loads(line) for line in f.readlines()]
        start_idx = len(lines)
        if start_idx > 0:
            y_true, y_pred = [line['label'] for line in lines], [line['predict'] for line in lines]
        return start_idx, y_true, y_pred



def get_rsa_label(rel_sampl, k):
    examples, harmful_examples, harmless_examples = rel_sampl
    examples = examples[:k]

    count = 0
    for l, example in enumerate(examples):
        if example in harmful_examples:
            count += 1
        elif example in harmless_examples:
            count -= 1
    
    rsa_label = 1 if count >= 0 else 0
    return rsa_label