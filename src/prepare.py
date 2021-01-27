import argparse
import os
import yaml
import pandas as pd
from sklearn.model_selection import train_test_split


def process_posts(input_file_path, output_file_path_train, output_file_path_test, params_seed, params_split):
    df = pd.read_csv(input_file_path)

    df_train, df_test = train_test_split(df, test_size=params_split, random_state=params_seed)

    df_train.to_csv(output_file_path_train, index=False)
    df_test.to_csv(output_file_path_test, index=False)


if __name__ == '__main__':
    # parser for optional console arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file_path', help='path to file')
    args = parser.parse_args()
    input_file_path = args.file_path

    # get params
    params = yaml.safe_load(open('params.yaml'))['prepare']
    params_split = params['split']
    params_seed = params['seed']
    output_file_path_train = os.path.join('data', 'prepared', 'train.csv')
    output_file_path_test = os.path.join('data', 'prepared', 'test.csv')
    os.makedirs(os.path.join('data', 'prepared'), exist_ok=True)

    # run processing
    process_posts(input_file_path, output_file_path_train, output_file_path_test, params_seed, params_split)







