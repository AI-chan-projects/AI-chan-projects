# digit_recognizer/models.py

from django.db import models # django models
from tensorflow.keras import models as tf_models # ai models
from tensorflow.keras import layers
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

class DigitRecognizerModel(models.Model):
    model_path = "models/digit_recognizer.keras"
    model = load_model(model_path)
    # # 이미지 분류 모델 정의
    # model = tf_models.Sequential([
    #     layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    #     layers.MaxPooling2D((2, 2)),
    #     layers.Conv2D(64, (3, 3), activation='relu'),
    #     layers.MaxPooling2D((2, 2)),
    #     layers.Conv2D(64, (3, 3), activation='relu'),
    #     layers.Flatten(),
    #     layers.Dense(64, activation='relu'),
    #     layers.Dense(10, activation='softmax')
    # ])

    @classmethod
    def predict(cls, image):
        # 이미지 데이터 읽어오기
        image_data = Image.open(image)
        image = image_data.copy()

        #이미지 스케일 변경
        image = image.convert('L')

        # 이미지 크기 출력
        #print("Original Image Size:", image_data.size)

        # 이미지 크기 조절 (Thumbnail | resize 메서드 사용)
        image = image.resize((28, 28))

        # 이미지 크기 출력
        #print("Resized Image Size:", image.size)

        # 이미지 전처리
        image_array = np.array(image)

        # 배경이 하얗다면 색상 반전
        if image_array.mean() > 127.5:
            image_array = 255 - image_array

        # 모델에 테스트 이미지 적용
        image_array = image_array.reshape((1, 28, 28, 1)).astype('float32') / 255
        predictions = cls.model.predict(image_array)

        # 예측 결과 출력
        predicted_label = np.argmax(predictions)
        return predicted_label

    def __str__(self):
        return "Digit Recognizer Model"
