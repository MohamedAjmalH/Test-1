# Crop Prediction

## Description
A Regression type prediction model using *Random Forest Regressor* algorithm. It uses R², MAE (Mean Absolute Error) and MSE (Mean Squared Error) as the metric for prediction.

## Steps

### Building Files
1) app.py: which has regression model code
2) requirements.txt: which has the required library names
3) Liver Patient Dataset (LPD)_train.csv: .csv dataset which includes the data regarding counsumer forcast prediction
4) Dockerfile: which contains the commands to be run in docker
5) selenium_test.py: which contains the selenium code for automated testing
6) templates/index.html: in contains html (computer language) which is used to display the contents from app.py

### Git & Other Commands used in Command Prompt
1) `mkdir <file_name>` to create the folder
2) `cd <file_name>` to go inside the folder
3) `git init`, initializing folder as git repository
4) manually add all the files
5) `git add .` to add all the files into git track
6) `git commit -m "<message>"`, it commits whatever is there in the track
7) `git remote add origin <GitHub repository link>`, builds connection between git and github
8) `git push --set-upstream origin master`, sends all the files from git to github.


### Jenkins
1) created a new item with item name as **<item_name>**
2) selected *Freestyle project* as the item type
3) selected *Git* in **Source Code Management**
4) added *Execute Windows batch command* step in **Build Steps**
5) Saved the Configurations
6) Clicked build now

#### Output
  ![test 1](https://github.com/user-attachments/assets/ee896205-6fbf-4105-ab0a-e3b5969ac210)

### Dockers
1) used `cd` to go forward and `cd..` to do backward, to get to the correct path in command prompt (i.e. the folder where all the files including docerfile is located.
2) executed the command `docker build -t <docker_image_name> .` to build the docker image.
3) executed the command `docker run <docker_image_name>` to run the docker image.

#### Output
  ##### Command Prompt
  ![test 1 1](https://github.com/user-attachments/assets/77f56cf7-610b-4609-a3e5-2ffaec1c90f8)
  ![test 1 1 1](https://github.com/user-attachments/assets/8f8338be-1aca-4d59-a55a-a3879ecd0466)
  ![test 1 1 2](https://github.com/user-attachments/assets/dcce3b90-9774-407e-9826-a4a4de76f876)
  ![test 1 1 3](https://github.com/user-attachments/assets/d3615a52-0f2d-459b-846f-19a4ba21cc85)

  
  ##### Docker Hub
  ![test 1 2](https://github.com/user-attachments/assets/3335af03-867c-48cf-a58e-c70fa48d84e6)


### Selenium
1) integrated flask into app.py. And build an html file called index.html inside templates folder.
2) created selenium_test.py file which contains the selenium code for autotesting app.py

#### Output
  ##### Flask app (Command Prompt)
  ![test 0 1](https://github.com/user-attachments/assets/75b060d7-06f3-4a39-9fda-781939519d69)


  ##### Flask app (Web Browser)
  ![test 0 2](https://github.com/user-attachments/assets/34f6ec18-5520-412f-a77d-380d7731803a)


  ##### Selenium 
  ![test 1](https://github.com/user-attachments/assets/068a30f5-98cc-48a7-9e57-b081b4573deb)

  

