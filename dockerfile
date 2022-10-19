FROM python:3
RUN git clone https://github.com/perezmatias/Palindromos.git
WORKDIR /Palindromos
RUN pip install -r requirements.txt
CMD ["python3", "-m", "unittest"]