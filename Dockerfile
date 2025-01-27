# Please, try to use images located in public.ecr.aws/docker/library
FROM public.ecr.aws/docker/library/python:3.11 AS builder

# Install dependencies for your tool
RUN pip install networkx && pip install numpy

# Copy your script to run the tool
COPY script.py /app/

# Necessary files for running your tool on the Datoma infrastructure
COPY install_jobrunner.py /app/install_jobrunner.py
RUN chmod +x /app/install_jobrunner.py
COPY install_jobrunner_and_run.sh /app/install_jobrunner_and_run.sh
RUN chmod +x /app/install_jobrunner_and_run.sh
COPY datomaconfig.yml /app/

# Necessary lines to run the tool
WORKDIR /app
ENTRYPOINT ["/bin/bash" ,"/app/install_jobrunner_and_run.sh" ]
