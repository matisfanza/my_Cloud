FROM python:3.9

# 作業ディレクトリの設定
WORKDIR /app

# 必要なパッケージのインストール
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# アプリケーションのコピー
COPY . .

# Streamlitの設定
ENV STREAMLIT_SERVER_HEADLESS true

# アプリケーションの起動
CMD ["streamlit", "run", "app.py"]