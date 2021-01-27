import os
import argparse
import pandas as pd
import yaml


def process_posts(input_file_path_train, input_file_path_test,
                  output_file_path_train, output_file_path_test, params_multiplier_1, params_bias_1):

    df_train = pd.read_csv(input_file_path_train)
    df_train['SepalLengthCm'] = df_train['SepalLengthCm'] * params_multiplier_1 + params_bias_1
    df_train.to_csv(output_file_path_train, index=False)

    df_test = pd.read_csv(input_file_path_test)
    df_test['SepalLengthCm'] = df_test['SepalLengthCm'] * params_multiplier_1 + params_bias_1
    df_test.to_csv(output_file_path_test, index=False)


if __name__ == '__main__':
    # parser for optional console arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--idir', help='path to file')
    parser.add_argument('-o', '--odir', help='path to file')

    args = parser.parse_args()
    input_file_path_dir = args.idir
    output_file_path_dir = args.odir

    input_file_path_train = os.path.join(input_file_path_dir, 'train.csv')
    input_file_path_test = os.path.join(input_file_path_dir, 'test.csv')

    # get params
    params = yaml.safe_load(open('params.yaml'))['featurize']
    params_multiplier_1 = params['multiplier_1']
    params_bias_1 = params['bias_1']

    output_file_path_train = os.path.join('data', 'features', 'train.csv')
    output_file_path_test = os.path.join('data', 'features', 'test.csv')
    os.makedirs(os.path.join('data', 'features'), exist_ok=True)

    # run processing
    process_posts(input_file_path_train, input_file_path_test,
                  output_file_path_train, output_file_path_test, params_multiplier_1, params_bias_1)








