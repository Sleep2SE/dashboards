from pyngrok import ngrok
ngrok.set_auth_token("Your_token")
import os
import time

# Указываем порт, который использует Streamlit (по умолчанию 8501)
port = 8501

# Открываем туннель через pyngrok
public_url = ngrok.connect(port)
print("Public URL:", public_url)

# Запуск Streamlit-приложения в background
!streamlit run dashboard_app.py &
time.sleep(5)  # небольшая задержка для корректного старта приложения
