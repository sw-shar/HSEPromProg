# cmake, make, python

FROM python:3.9

# install cmake
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive \
	apt-get install -yq --no-install-recommends cmake
	
WORKDIR /cmake-with-flask
COPY requirements.txt .	
RUN pip install -r requirements.txt
	
# In ".dockerignore": Dockerfile.
COPY . .
RUN cmake .
RUN make
RUN bin/C

RUN useradd techproguser
USER techproguser
RUN whoami

#ENTRYPOINT ["/bin/sh", "-c"]  # by default
CMD ["python", "app.py", "--host=0.0.0.0"]
