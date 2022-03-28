FROM maven:3.3.9-jdk-8

WORKDIR /DostavimVse
COPY DostavimVse/ .

RUN mvn clean compile
RUN mvn package -Dmaven.test.skip -Dstart-class=ru.fivt.dostavimvse.DostavimvseApplication

RUN apt-get update || true
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends mysql-client

COPY fill-db.sh /

CMD sleep 20 && /fill-db.sh && exec java -jar target/dostavimvse-0.0.1-SNAPSHOT.jar
