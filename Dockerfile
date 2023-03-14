FROM python

WORKDIR /app
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY . .
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

# CMD ["flask", "run"]
ENTRYPOINT ["sh", "./launch.sh"]