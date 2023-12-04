#digit recognizer test 
import tensorflow as tf
from keras.models import load_model
import numpy as np
from PIL import Image

# 저장된 모델을 불러오기
loaded_model = load_model("./model/model.keras")

# 테스트 이미지 로드
test_image_path = './images/test_image.png'
test_image = Image.open(test_image_path).convert('L')  # Convert to grayscale
test_image = test_image.resize((28,28))
test_image_array = np.array(test_image)

# 배경이 하얗다면 색상 반전
if test_image_array.mean() > 127.5:
    test_image_array = 255 - test_image_array

test_image = test_image_array.reshape((1, 28, 28, 1)).astype('float32') / 255


# 모델에 테스트 이미지 적용
predictions = loaded_model.predict(test_image)

# 예측 결과 출력
predicted_label = np.argmax(predictions)
print(f'Predicted Label: {predicted_label}')
