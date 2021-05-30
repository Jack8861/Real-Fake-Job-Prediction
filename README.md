# Real-Fake-Job-Prediction
#### A simple machine learning based website which can predict if a job offer is real or fake/fraud

## MOTIVATION

- There are a lot of job offers that are advertized on the internet and most of them are from companies seeking employees but a few of them happen to be fraud.

- These fraud job offers target people who are in desire to get a job but and try to get their bank account details, ask for initial purchases ( like software purchases ), etc., and rob them

- As a future data scientist i wanted to see if we can try to solve this problem, if we can find patterns which can help us predict fraud and protect people from it.

## DATA SOURCE
- [ [Real or Fake] Fake JobPosting Prediction ](https://www.kaggle.com/shivamb/real-or-fake-fake-jobposting-prediction)

## Notebook
##### I have also published the corresponding code on Kaggle Notebook. (EDA, will be updated within a week from now)
- [real-fake-job-for-end-to-end](https://www.kaggle.com/jackfroster/real-fake-job-for-end-to-end)

# Built with
<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code>
<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/html/html.png"></code>
<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/css/css.png"></code>
<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/javascript/javascript.png"></code>
<code><img height="30" src="https://github.com/tomchen/stack-icons/raw/master/logos/bootstrap.svg"></code>
<code><img height="30" src="https://symbols.getvecta.com/stencil_80/56_flask.3a79b5a056.jpg"></code>
<code><img height="30" src="https://raw.githubusercontent.com/github/explore/fbceb94436312b6dacde68d122a5b9c7d11f9524/topics/aws/aws.png"></code>

<code><img height="30" src="https://raw.githubusercontent.com/pandas-dev/pandas/761bceb77d44aa63b71dda43ca46e8fd4b9d7422/web/pandas/static/img/pandas.svg"></code>
<code><img height="30" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1280px-Scikit_learn_logo_small.svg.png"></code>

## DEPLOYMENT
#### Deployment is done using [deploy](https://github.com/Jack8861/Real-Fake-Job-Prediction/) master branch itself
#### This website was deployed at [AWS](https://aws.amazon.com/)

## How to use
#### You will have to enter the following details (NOTE: the options available are limited by the dataset used)
- First select the job title
- Then, enter the location the job is offered at 
- Then, select the department the job role belongs to
- Then, select the salary range (close enough is fine)
- Then, enter the company profile or simply enter "NO PROFILE" if it does not exist (its likely a scam ;)

## DEMO

![not available yet]()

## Usage
You can use this project for further developing it and adding your work in it. If you use this project, kindly mention the original source of the project and mention the link of this repo in your report.

## Further Improvements
This was my first end to end project so their are actually a lot of improvements but i want to apply them in my upcoming projects as this was past my dead line

- The front-end structure (all except the form) was from [ineuron](https://ineuron.ai/) ( i have taken the course and it was provided as a course material )
- The select statement has over 1000's of options os the options list gets black for a second ( didn't find any better method but it works )	
- More data can be collected and used to improve the model performance
- MLOPS is not properly followed
- model retraining approach can be used if data collection is possible...
- can use logging
- should explore a range of algorithms and techniques
- the real jobs data was 17,000 records and fake data was 800 records so i used oversampling. This might have increased our accuracy by causing data leakage... without oversampling we were able to get 90%-92% accuracy in predicting the fake jobs correctly ( overall accuracy was 99.9% )
- can dockerize it, i ran into a problem with dockers after my recent windows update, (i'll have to fix it before the next project is done)

## Licenseing 
This project is licensed under [GNU (GENERAL PUBLIC LICENSE)]().

## Contact

[linkedin](https://www.linkedin.com/in/syed-rahim-saqib-2505221b5)
[kaggle](https://www.kaggle.com/jackfroster)
