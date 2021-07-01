FROM alpine:3.13 as installer

# find downloads for all versions here - https://www.elastic.co/downloads/past-releases#filebeat-oss
# logstash is still OSS, see - https://www.elastic.co/pricing/faq/licensing

ARG FB_VERSION="7.10.2"
WORKDIR /download
ADD https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-oss-${FB_VERSION}-linux-x86_64.tar.gz ./filebeat.tar.gz

RUN mkdir /filebeat && \
    tar -xzf filebeat.tar.gz --strip-components=1 -C /filebeat

# Filebeat
FROM debian:buster-slim

WORKDIR /usr/share/filebeat
COPY --from=installer /filebeat .
COPY filebeat.yml .
COPY apache.yml ./modules.d/apache.yml

ENTRYPOINT [ "/usr/share/filebeat/filebeat", "run",  "-e" ]