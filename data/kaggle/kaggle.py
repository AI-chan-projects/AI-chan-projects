# kaggle API
# Check here first 
# https://www.kaggle.com/docs/api
# https://github.com/Kaggle/kaggle-api
# Quick start example : Shell : >>  kaggle competitions download -c digit-recognizer -p ./digit-recognizer

import subprocess

# 실행할 쉘 명령어
command = "kaggle competitions download -c digit-recognizer -p ./digit-recognizer"

# 쉘 명령어 실행
subprocess.run(command, shell=True)
