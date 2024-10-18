FROM python:3.11-slim

WORKDIR /app


COPY requirements.txt requirements.txt
COPY mystreamlit_app.py mystreamlit_app.py

RUN pip install -r requirements.txt
EXPOSE 8501

CMD ["streamlit", "run", "mystreamlit_app.py"]