YourFutureGuide
==============================
<p align="center">
  <img src="/frontend/public/YourFutureGuide.png" alt="logo">

   [![python](https://img.shields.io/badge/Python-3.11.5-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
   [![angular](https://img.shields.io/badge/Angular-DD0031?style=flat&logo=angular&logoColor=white)](https://angular.dev/)
</p>

TODO



## Getting started

We recommend to use [Python 3.11.5](https://python.domainunion.de/downloads/release/python-3115/) to run our code, due to possible incompatibiities with newr versions.

### Installation
The installation process is described below:

1. Clone this repository:
   ```
   git clone https://github.com/llaraspata/YourFutureGuide.git
   ```
2. Create a virtual environment and activate it:
   ```
   python -m venv your_venv_name
   source <your_venv_name>/bin/activate  # On Windows, use: <your_venv_name>\Scripts\activate
   ```
3. Install all the project dependencies:
   ```
   pip install -r requirements.txt
   ```
TODO angular

### Run YourFutureGuide

TODO


## Citation

```bibtex
@misc{laraspata2024YourFutureGuide,
author = {Lucrezia Laraspata},
title = {YourFutureGuide},
year = {2024},
url = {https://github.com/llaraspata/YourFutureGuide/}
}
```




Project Organization (TODO)
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Raw questionnaires derived from the augmentation process.
    │   ├── interim        <- Intermediate augmented data that has been transformed to JSON.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The data used as starting point from this project
    │                         (taken from Talentia Software HCM).
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Predictions for each run experiments. For each of the a log and a picke file are saved.
    │
    ├── notebooks          <- Jupyter notebooks used to illustrate class usage, dataset insights, and experimental results.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment.
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   ├── convert_qst_to_json.py
    │   │   └── TFQuestionnairesDataset.py
    │   │
    │   ├── prompts        <- Catalog of the employed prompts
    │   │   ├── qst_to_json_prompts.py
    │   │   ├── QstToJsonPromptGenerator.py
    │   │   ├── QstToJsonScenarioGenerator.py
    │   │   │
    │   │   ├── prediction_prompts.py
    │   │   ├── PredictionPromptGenerator.py
    │   │   ├── PredictionScenarioGenerator.py
    │   │   │
    │   │   ├── topic_modeling_prompts.py
    │   │   ├── TopicModelingPromptGenerator.py
    │   │   └── TopicModelingScenarioGenerator.py
    │   │
    │   ├── models         <- Scripts to run experiments and evaluations
    │   │   ├── experiment_config.json
    │   │   │
    │   │   ├── predict.py
    │   │   │
    │   │   ├── QuestionnairesEvaluator.py
    │   │   ├── ModelEvaluator.py
    │   │   └── evaluate.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       ├── experiment_pairs.json
    │       │
    │       ├── GlobalResultVisualizer.py
    │       ├── PairResultVisualizer.py
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
