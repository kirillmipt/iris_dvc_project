# iris_dvc_project

## Initialize project with dvc
```dvc init```


## Add iris data to dvc
```dvc add data/data.csv```

## add pipeline prepare step
```
dvc run -n prepare \
          -p prepare.seed,prepare.split \
          -d src/prepare.py -d data/data.csv \
          -o data/prepared \
          python src/prepare.py -f data/data.csv
```

## add featurize step
```
dvc run -n featurize \
          -p featurize.multiplier_1,featurize.bias_1 \
          -d src/featurization.py -d data/prepared \
          -o data/features \
          python src/featurization.py -i data/prepared -o data/features
```

## add train step
```
dvc run -n train \
          -p train.seed,train.c \
          -d src/train.py -d data/features \
          -o model.pkl \
          python src/train.py -i data/features -o model.pkl
```