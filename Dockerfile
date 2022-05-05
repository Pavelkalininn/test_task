# pull official base image
FROM python:3.7.9

# set work directory
WORKDIR /question_app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# # copy entrypoint.sh
# COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
#
# # copy project
# COPY . /usr/src/app/
#
# # run entrypoint.sh
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]