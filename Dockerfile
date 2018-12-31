FROM python:latest
WORKDIR /root
RUN pip install multiping pytest
COPY *.py ./
ENTRYPOINT [ "pytest", "-v", "-s", "--tb=no" ]
