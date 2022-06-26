# Machine_learning_project

# Software and account requirements

1. [Guthub Account](https://github.com/)
2. [Hiroku Account](https://dashboard.hroku.com/login)
3. [VS Code](https://code.visualstudio.com/downloads)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)

# creating conda environment
```
conda create -p venv python==3.7 -y
```
# Activating conda environment
```
conda activate venv
```
OR
```
conda activate venv/
```
# To add files to git
```
git add .
```
OR
```
git add <file_name>
```
>NOTE: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check all git status
```
git status
```
To check all version maintainted by git
```
git log
```
To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url
```
git remote -v
```

To setup CI/CD pipeline in heroku we need 3 information :-
1. HEROKU_EMAIL = chandan216113@gmail.com
2. HEROKU_API_KEY = <>
3. HEROKU_APP_NAME = ml-regressionapplication

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> NOTE: Image name for docker must be in lowercase

To list docker images
```
docker images
```

Run docker images
```
docker run -p 5000:5000 -e PORT=5000 <IMAGE ID>
```

To check running container in docker
```
docker ps
```

To stop docker comtainer
```
docker stop <container_id>
```

'''
python setup.py install
'''

Install ipykernel (Jupyter Notebook)
'''
pip install ipykernel
'''


