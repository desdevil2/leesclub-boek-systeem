FROM python:3.11-slim
WORKDIR /app
COPY . /app
EXPOSE 5000
ENV FLASK_RUN_HOST=0.0.0.0
RUN pip install -r requirements.txt
CMD ["python", "-m", "flask", "--app", "router", "run", "--debug"]