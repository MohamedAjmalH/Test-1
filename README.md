# Crop Prediction

## Description
A regression prediction model utilizing the *Random Forest Regressor* algorithm, evaluated using R², MAE (Mean Absolute Error), and MSE (Mean Squared Error) metrics.

---

## Steps

### Building Files
1. **app.py**: Contains the regression model code.
2. **requirements.txt**: Lists required library dependencies.
3. **Liver Patient Dataset (LPD)_train.csv**: .csv dataset used for consumer forecast prediction.
4. **Dockerfile**: Commands for building and running the Docker image.
5. **selenium_test.py**: Contains Selenium code for automated testing.
6. **templates/index.html**: HTML file used to display the output from `app.py`.

---

## Git & Other Commands Used in Command Prompt
1. `mkdir <file_name>` - Create a new folder.
2. `cd <file_name>` - Navigate into the folder.
3. `git init` - Initialize the folder as a Git repository.
4. Manually add all the necessary files.
5. `git add .` - Stage all files for tracking.
6. `git commit -m "<message>"` - Commit changes with a message.
7. `git remote add origin <GitHub repository link>` - Establish connection between the local repository and GitHub.
8. `git push --set-upstream origin master` - Push all files to the GitHub repository.

---

## Jenkins
1. Created a new item with the name **<item_name>**.
2. Selected *Freestyle project* as the project type.
3. Selected *Git* under **Source Code Management**.
4. Added *Execute Windows batch command* step under **Build Steps**.
5. Saved the configurations.
6. Clicked "Build Now".

#### Output:
![Jenkins Build Output](https://github.com/user-attachments/assets/ee896205-6fbf-4105-ab0a-e3b5969ac210)

---

## Docker
1. Used `cd` to navigate and `cd..` to move backward to ensure the correct path (where the Dockerfile is located) is active.
2. Executed `docker build -t <docker_image_name> .` to build the Docker image.
3. Executed `docker run <docker_image_name>` to run the Docker container.

#### Output:
**Command Prompt:**  
![Docker Build Output 1](https://github.com/user-attachments/assets/77f56cf7-610b-4609-a3e5-2ffaec1c90f8)  
![Docker Build Output 2](https://github.com/user-attachments/assets/8f8338be-1aca-4d59-a55a-a3879ecd0466)  
![Docker Build Output 3](https://github.com/user-attachments/assets/dcce3b90-9774-407e-9826-a4a4de76f876)  
![Docker Build Output 4](https://github.com/user-attachments/assets/d3615a52-0f2d-459b-846f-19a4ba21cc85)  

**Docker Hub:**  
![Docker Hub Output](https://github.com/user-attachments/assets/3335af03-867c-48cf-a58e-c70fa48d84e6)

---

## Selenium
1. Integrated Flask into `app.py` and created an HTML file (`index.html`) inside the templates folder.
2. Created a `selenium_test.py` file containing Selenium code to automate testing of `app.py`.

#### Output:
**Flask App (Command Prompt):**  
![Flask App Output 1](https://github.com/user-attachments/assets/75b060d7-06f3-4a39-9fda-781939519d69)  

**Flask App (Web Browser):**  
![Flask App Output 2](https://github.com/user-attachments/assets/34f6ec18-5520-412f-a77d-380d7731803a)  

**Selenium:**  
![Selenium Output](https://github.com/user-attachments/assets/068a30f5-98cc-48a7-9e57-b081b4573deb)
