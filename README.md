<h1 align='center'>
  Your Future Guide
</h1>


<div align="center">

   ![Logo](/frontend/public/YourFutureGuide.png)

   [![python](https://img.shields.io/badge/Python-3.11.5-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
   [![angular](https://img.shields.io/badge/Angular-DD0031?style=flat&logo=angular&logoColor=white)](https://angular.dev/)

</div>

**YourFutureGuide** is an LLM-based application to discover which is the most suitable educational or professional path. [LLaMa3-7b](https://ollama.com/library/llama3) will determine so by investigate your interests and aspirations in only 5 shots.

<div align="center">

![Demo](/frontend/public/demo_ERN_24.gif)

</div>

This project was shown during the European Research Night 2024 in Bari. Therefore the degree course prediction was limited to what proposed by the University of Bari in that moment. 
So, a Retreival Augmeted Generation (RAG) mechanism has been implemented at the end of the conversation to retrieve the three degree couses most similar to the student's interests.

> [!NOTE]
> Since this is a demo for the European Research Night 2024 in Bari, the conversation is in Italian.

## 🚀 Getting started

We recommend to use [Python 3.11.5](https://python.domainunion.de/downloads/release/python-3115/) to run our code, due to possible incompatibiities with newr versions.

Moreover, the frontend part of this project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 18.2.4. So, be sure that Angular is installed on your machine. You can find details on how to install it in the [Angular Github repository(https://github.com/angular/angular-cli)].

### 🛠️ Installation
The steps to correctly install the project are described below (both backend and frontend).

#### 🐍 Python backend
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

#### 🖥️ Angular frontend
Once te repository has been cloned:

1. Move to the frontend directory:
   ```
   cd ./frontend
   ```
2. Install the dependencies
   ```
   npm install
   ```

### 🗄️ Import documents in ChromaDB

The vectorial database Chroma is used to store PDF files used for RAG. You need to follow the steps below to insert documents in the DB and use them in the prediction process.

1. Upload your PDF files in the directory `data`
2. Insert them in the ChromaDB
   ```
   python ./backend/data/populate_db.py
   ```

### ✨ Run YourFutureGuide

To run the **python backend** follow the steps below: 
1. Move to the directory `backend`
2. Run the uvicorn server
   ```
   uvicorn main:app --reload
   ```

To run the **angular frontend** follow the steps below: 
1. Move to the directory `frontend`
2. Run the angular client
   ```
   ng serve
   ```

## 🖋️ Citation

```bibtex
@misc{laraspata2024YourFutureGuide,
author = {Lucrezia Laraspata},
title = {YourFutureGuide},
year = {2024},
url = {https://github.com/llaraspata/YourFutureGuide/}
}
```