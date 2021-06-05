# Core requirements
- Python3
- pip
# How to run
### Open app folder
    $ cd python-json-template                       # open app root folder
### Install package requirements
    $ python3 -m pip install -r requirements.txt    # install requirements from file
### Run application
    $ cd src                                        # open app source folder
    $ python3 app.py                                # app entry point execution
    $ ./app.py                                      # app entry point execution
Once application finished successfully you should find the results in outputs folder. 
### If you've added/removed some packages
    $ python3 -m pip freeze                         # output requirements installed
    $ python3 -m pip freeze > requirements.txt      # write requirements to the file
