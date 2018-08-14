# Home Credit Default Risk: Open Solution
This repository has been forked from  https://github.com/bielrv/open-solution-home-credit-1.git and has been later modified by myself.  

## 1. Installation
1. Clone repository
```shell
git clone https://github.com/bielrv/open-solution-home-credit-1.git
```
2. Create virtual environment
```shell
virtualenv -p python3 venv
```
3. Activate virtualenv
```shell
source venv/bin/activate
```
4. Install requirements
```shell
pip install -r requirements.txt
```

## 2. Train and predict

Execute main.py
```shell
python main.py -- train_evaluate_predict_cv --pipeline_name lightGBM
```
## 4. Issues

### Increase SWAP memory

In order to successfully train the model an increase of the swap might be required.

#### What is SWAP space?

Swap space is a restricted amount of physical memory that is allocated for use by the operating system when available memory has been fully utilized. It is memory management that involves swapping sections of memory to and from physical storage.
