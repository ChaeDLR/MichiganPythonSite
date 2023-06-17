# Michigan Python Users Group Website

## Setup
Fork the repository and then clone your copy to your machine.
<br><br>
Traverse to the projects root directory and create a virtual environment.
### Mac OS venv
___

### Create virtual environment files in your current directory

```
python3 -m venv (folder name)
```
### Activate environment

```
source (folder name)/bin/activate
```

### Windows 10 venv
___

### Create virtual environment files in your current directory

```
python -m venv (folder name)
```

### Activate environment

```
(folder name)/Scripts/activate.bat
```

#### To deactivate venv in either environment

```
deactivate
```

### Install requirements
With the virtual environment active use the following command to install the projects requirements.
```
pip install -r requirements.txt
```

### Test the setup
Now to test that the project is setup correctly we will start djangos built in webserver and attempt to request the landing page using an internet browser.
<br><br>
Start the server using the manage.py file.
```
python manage.py runserver 8080
```
Launch your prefered browser and send an http request to the port specified in the previous command.
```
localhost:8080
```
You should now see the projects front page.
<br>
### Happy coding!
