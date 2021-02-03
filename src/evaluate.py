import argparse
import os
import yaml
import pandas as pd
import os
import pickle
import json

from sklearn.metrics import precision_recall_curve
import sklearn.metrics as metrics


def load_test_data(features_folder_path):
    test_features_file_path = os.path.join(features_folder_path, 'test.csv')
    return pd.read_csv(test_features_file_path)


def load_model(model_file_path):
    with open(model_file_path, 'rb') as fd:
        model = pickle.load(fd)
    return model


def evaluate(df_test, model, scores_file_path, plot_file_path):
    x_test = df_test.drop(columns=['Species'])
    y_test = df_test['Species']
    y_test_pred_proba = model.predict_proba(x_test)[:, 1]
    precision, recall, thresholds = precision_recall_curve(y_test, y_test_pred_proba)
    auc = metrics.auc(recall, precision)

    with open(scores_file_path, 'w') as fd:
        json.dump({'auc': auc}, fd)

    with open(plot_file_path, 'w') as fd:
        json.dump({'prc': [{
            'precision': p,
            'recall': r,
            'threshold': t
        } for p, r, t in zip(precision, recall, thresholds)
        ]}, fd)


if __name__ == '__main__':
    # parser for optional console arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-mfp', '--model_file_path', help='path to model file')
    parser.add_argument('-ffp', '--features_folder_path', help='path to features folder')
    parser.add_argument('-sfp', '--scores_file_path', help='path to scores file')
    parser.add_argument('-pfp', '--plot_file_path', help='path to plot file')

    args = parser.parse_args()
    model_file_path = args.model_file_path
    features_folder_path = args.features_folder_path
    scores_file_path = args.scores_file_path
    plot_file_path = args.plot_file_path

    df_test = load_test_data(features_folder_path)
    model = load_model(model_file_path)

    evaluate(df_test, model, scores_file_path, plot_file_path)
