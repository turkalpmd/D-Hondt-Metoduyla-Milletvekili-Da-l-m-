FROM python:3.8

LABEL maintainer "Turkalpmd  <izzetakbasli@gmail.com>"
# If you have any comment : LinkedIn - https://www.linkedin.com/in/turkalpmd/
# sudo docker build -t dhontapp:latest .
# sudo docker run -p 80:8501 -d --restart=always dhontapp:latest


WORKDIR /home/ubuntu/dhont

COPY requirements.txt ./requirements.txt

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt \
	&& rm -rf requirements.txt

# --------------- Configure Streamlit ---------------
RUN mkdir -p /root/.streamlit

RUN bash -c 'echo -e "\
	[server]\n\
	enableCORS = false\n\
	enableXsrfProtection = false\n\
	enableWebsocketCompression = false\n\
	" > /root/.streamlit/config.toml'
# enableWebsocketCompression = false\n\

EXPOSE 8501

COPY . /home/ubuntu/dhont

# --------------- Export envirennement variable ---------------
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ENTRYPOINT ["streamlit","run"]

CMD ["--server.port", "8501", "app.py"]