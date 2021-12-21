import os
import json
import jsonlines
from glob import glob

def load_file_list(dir_path):
    file_list = glob(dir_path + "/*/*/*/output.json")
    return file_list

def load_data(file_list):
    data = []

    for file_path in file_list:
        with open(file_path, 'rt', encoding='UTF8') as f:
            annotations = json.load(f)
        data.extend(annotations)

    return data

def generate_context(data):
    context = f"[{data['category_code']}] "
    context += f"{data['sum_vidPlace']} - {data['sum_vidSitu']} "
    context += data['sum'].replace("\n", ". ")

    if data['script'] is not None:
        context += f" {data['script']}".replace("\n", ". ")

    return context 

def convert_data_for_training(data):
    converted_data = []

    for annotation in data:
        temp = {}
        temp["qid"] = annotation["qid"]
        temp["sent1"] = generate_context(annotation)
        temp["sent2"] = annotation["que"] + "?"
        
        for i, answer in enumerate(annotation['answers']):
            temp[f'ending{i}'] = answer

        temp['label'] = annotation['correct_idx']
        converted_data.append(temp)

    return converted_data

def save_data(file_path, data):
    with jsonlines.open(file_path, 'w') as writer:
        writer.write_all(data)


if __name__ == "__main__":
    dir_path = "data/raw_data"

    data_mode_list = ["train", "test"]
    
    for data_mode in data_mode_list:
        data_path = os.path.join(dir_path, data_mode)
    
        file_list = load_file_list(data_path)
        data = load_data(file_list)
        converted_data = convert_data_for_training(data)

        converted_path = os.path.join("data", f"{data_mode}.json")
        save_data(converted_path, converted_data) 