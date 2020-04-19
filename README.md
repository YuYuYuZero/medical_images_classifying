# medical_images_classifying

simple classifying analysis for 47 medical images.

## environment

- *Python 3.7.3*

### requirements

Listed in `requirements.txt`:

- *pyradiomics==3.0*
- *numpy==1.18.0*
- *matplotlib==3.1.2*
- *scikit-learn==0.22*

Run if needed:

```shell
pip3 install -r requirements.txt
```

## feature_extraction

1. Put your radiomics data in `feature_extraction/image` & `feature_extraction/mask` 
2. Edit `feature_extraction/input_images.csv` for your own radiomics data, referring to [pyradiomics](https://github.com/radiomics/pyradiomics)

- Run:

  ```shell
  cd feature_extraction
  bash feature_extraction.sh
  ```

- Results will show in `feature_extraction/features_extracted.csv`

## data_processing

- Doing the dimension reduction, respectively by using 3 methods: *PCA*, *TSNE*, *LDA*.

- Run:

  ```shell
  cd data_processing
  python3 dimension_reduction.py
  ```

- Results:

### PCA-2

![PCA-2](https://raw.githubusercontent.com/YuYuYuZero/medical_images_classifying/master/data_processing/PCA-2.jpg)

### TSNE-2

![TSNE-2](https://raw.githubusercontent.com/YuYuYuZero/medical_images_classifying/master/data_processing/TSNE-2.jpg)

### LDA-1

![LDA-1](https://raw.githubusercontent.com/YuYuYuZero/medical_images_classifying/master/data_processing/LDA-1.jpg)

As the results shown, the third one has an outstanding performance. 

We'll take the third processed data for a simple classifying.

## simple_classifying

### Logistic Regression

- Run:

  ```shell
  cd simple_classifying
  python3 lr_clf.py
  ```

- Results:

  ```
  accuracy of training data: 0.9714285714285714
  accuracy of testing data: 1.0
  ```

### SVM

- Run:

  ```shell
  cd simple_classifying
  python3 svm_clf.py
  ```

- Results:

  ```
  accuracy of training data: 0.9714285714285714
  accuracy of testing data: 1.0
  ```

