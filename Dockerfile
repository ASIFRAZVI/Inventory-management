#importing python latest image from Docker
FROM python:latest 

#create workdir 
WORKDIR /inventory_management  

#add or copy all to workdir
COPY . /inventory_management  

# Create a virtual environment named 'menv'
RUN python -m venv venv

# Activate the virtual environment
RUN . venv/bin/activate

#install the all requirements
RUN pip install -r requirements.txt

# install the ginicorn
RUN pip3 install gunicorn

# migrete the database
RUN python3 manage.py migrate

#choose the port where app is exposed
EXPOSE 8000

# #run command for local
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

#  run command for  gunicorn server
CMD [ "python3", "-m", "gunicorn", "fatmag.wsgi", "0.0.0.0:8000" ]