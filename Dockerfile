FROM python:latest
WORKDIR /root
COPY ping.py .
RUN pip install multiping
ENTRYPOINT [ "python", "/root/ping.py" ]
