FROM python:latest
WORKDIR /root
RUN apt update 
RUN apt install -y iperf3
RUN pip install multiping pytest iperf3
COPY *.py ./
ENTRYPOINT [ "pytest", "-v", "-s", "--tb=no" ]
