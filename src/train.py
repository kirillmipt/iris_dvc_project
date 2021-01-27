import argparse
import os
import pickle
from sklearn import svm
import yaml
import pandas as pd


def train(input_file_path_train, out_model_file_path, params_seed, params_c):

    df_train = pd.read_csv(input_file_path_train)
    x_train = df_train.drop(columns=['Species'])
    y_train = df_train['Species']

    model = svm.SVC()
    model.fit(x_train, y_train)

    with open(out_model_file_path, 'wb') as fd:
        pickle.dump(model, fd)


if __name__ == '__main__':
    # parser for optional console arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--idir', help='path to file')
    parser.add_argument('-o', '--out_model_file_path', help='path to file')

    args = parser.parse_args()
    input_file_path_dir = args.idir
    out_model_file_path = args.out_model_file_path

    input_file_path_train = os.path.join(input_file_path_dir, 'train.csv')

    # get params
    params = yaml.safe_load(open('params.yaml'))['train']
    params_seed = params['seed']
    params_c = params['c']

    output_file_path_train = os.path.join('data', 'features', 'train.csv')
    output_file_path_test = os.path.join('data', 'features', 'test.csv')
    os.makedirs(os.path.join('data', 'features'), exist_ok=True)

    # run processing
    train(input_file_path_train, out_model_file_path, params_seed, params_c)








