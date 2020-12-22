FROM continuumio/miniconda3

EXPOSE 8501
WORKDIR /app

COPY . .
COPY requirements.txt ./requirements.txt

RUN conda install python=3.9
RUN conda install -c conda-forge --file requirements.txt

CMD streamlit run --server.port $PORT app.py
