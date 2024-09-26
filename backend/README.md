Python Backend - LLM interaction 
==============================

We employed LLaMa3-7b to handle the conversation for all the tasks. 
Once selected what to determine, the model will start to ask questions in order to understand which are the person's interest and aspirations. 
Currently, the number of questions to generate is set to 5, then, the model will respond with the final suggestion.


The execution flow followed once selected to identify the most suitable career path is described below.
 
<div align="center">

![CareerPrediction](/backend/figures/career_prediction_schema.svg)

</div>


The execution flow followed once selected to identify the most suitable UniBa's degree course is described below.
 
<div align="center">

![DegreePrediction](/backend/figures/degree_prediction_schema.svg)

</div>