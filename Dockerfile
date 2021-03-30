FROM python:latest

# Install app
ADD . /usr/src/src
WORKDIR /usr/src/src
RUN python3 setup.py install

# Launch app
CMD ["python3", "src/test.py"]