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
          -p train.seed,train.n_estimators \
          -d src/train.py -d data/features \
          -o model.pkl \
          python src/train.py -i data/features -o model.pkl
```

## add evaluate step
```
dvc run -n evaluate \
          -d src/evaluate.py -d model.pkl -d data/features \
          -M scores.json \
          --plots-no-cache prc.json \
          python src/evaluate.py -mfp model.pkl -ffp data/features \
                -sfp scores.json -pfp prc.json
```

## run reproduce experiment after change something
```dvc repro```

## To see how params in the workspace differ vs. the last commit
```dvc params diff```

## To see how metrics in the workspace differ vs. the last commit
````dvc metrics diff````

## To compare precision recall curves with a single command
```dvc plots diff -x recall -y precision```