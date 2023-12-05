this document is about the app "digit_recognizer" 

AI-Chan : field 라는 프로젝트에 digit_recognizer라는 앱을 만들었어.
해당 앱에서 png 파일을 입력 받고,  모델을 통해 분류 결과를 받는 작업을 하려면 어떻게 digit_recognizer 앱을 구성할까?

LLM : `digit_recognizer` 앱을 구성하여 PNG 파일을 입력으로 받고, 모델을 통해 분류 결과를 얻기 위해서는 다음과 같은 단계를 따를 수 있습니다.:

1. **모델 정의**: `digit_recognizer` 앱 내에서 `models.py` 파일을 생성하고, 이미지 분류를 위한 모델을 정의합니다. 모델은 이미지를 입력으로 받아 숫자를 예측하는 형태여야 합니다.

    ```python
    # digit_recognizer/models.py

    from django.db import models

    class DigitRecognizerModel(models.Model):
        # 모델 필드 및 메서드 정의
        # ...
    ```
    모델을 정의하는 부분은 모델의 구조 및 필드를 결정하는 부분이에요. 여기서는 이미지 분류를 위한 간단한 모델을 정의하는 예제를 보여 드릴게요. 일반적으로 이미지 분류를 위해서는 CNN(Convolutional Neural Network)을 사용합니다.

    ```python
   # digit_recognizer/models.py

    from django.db import models # django models
    from tensorflow.keras import models as tf_models # ai models
    from tensorflow.keras import layers
    from tensorflow.keras.models import load_model
    import numpy as np
    from PIL import Image

    class DigitRecognizerModel(models.Model):
        # 모델 가중치를 불러오는 상대경로. 이 때 `models` 폴더는 Django Project의 루트에 위치해야 한다.
        model_path = "models/digit_recognizer.keras" 
        model = load_model(model_path)
       
        @classmethod
        def predict(cls, image):
            # 이미지 데이터 읽어오기
            image_data = Image.open(image)
            image = image_data.copy() # 원본 유지

            #이미지 스케일 변경 (model의 input shape과 관련 있음)
            image = image.convert('L')

            # 이미지 크기 조절 (Thumbnail | resize 메서드 사용)
            image = image.resize((28, 28))

            # 이미지 전처리
            image_array = np.array(image)

            # 배경이 비교적 하얗다면 색상 반전 (모델을 학습한 그대로 적용)
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


    ```
    이 코드에서는 간단한 CNN 아키텍처를 사용하여 이미지를 입력으로 받고 0부터 9까지의 숫자 중 하나를 예측하는 모델을 정의했어요. 모델의 구조나 하이퍼파라미터를 실제로 훈련시킨 모델과 맞추어야 합니다. 모델을 훈련시킨 후에는 `predict` 메서드에서 실제 예측 로직을 구현해야 해요.
    `predict` 메서드에는 digit-recognizer의 test로직을 구현했어요.



2. **폼 정의**: `forms.py` 파일을 생성하여 이미지를 업로드할 수 있는 폼을 정의합니다.

    ```python
    # digit_recognizer/forms.py

    from django import forms

    class ImageUploadForm(forms.Form):
        image = forms.ImageField()
    ```

3. **뷰 정의**: `views.py` 파일에서 이미지를 처리하고 모델을 사용하여 예측 결과를 얻는 뷰를 정의합니다.

    ```python
    # digit_recognizer/views.py

    from django.shortcuts import render
    from .forms import ImageUploadForm
    from .models import DigitRecognizerModel

    def digit_recognizer_view(request):
        if request.method == 'POST':
            form = ImageUploadForm(request.POST, request.FILES)
            if form.is_valid():
                # 업로드된 이미지를 모델에 전달하여 예측
                image = form.cleaned_data['image']
                prediction = DigitRecognizerModel.predict(image)

                # 예측 결과를 사용하여 필요한 작업 수행
                # ...

                return render(request, 'result.html', {'prediction': prediction})
        else:
            form = ImageUploadForm()

        return render(request, 'upload.html', {'form': form})
    ```

4. **템플릿 작성**: `templates` 폴더에 HTML 템플릿 파일을 작성하여 이미지 업로드 폼과 예측 결과를 표시하는 페이지를 만듭니다.

    - `templates/upload.html`:

    ```html
    <!-- digit_recognizer/templates/upload.html -->

    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form }}
        <button type="submit">Upload</button>
    </form>
    ```

    - `templates/result.html`:

    ```html
    <!-- digit_recognizer/templates/result.html -->

    <p>Prediction: {{ prediction }}</p>
    ```

5. **URL 매핑**: `urls.py` 파일에서 해당 뷰를 URL에 매핑합니다.

    URL 매핑을 위해 `urls.py` 파일을 작성할 건데요, `digit_recognizer` 앱 내에 해당 파일을 만들어봅시다.

    ```python
    # digit_recognizer/urls.py

    from django.urls import path
    from .views import digit_recognizer_view

    urlpatterns = [
        path('recognize/', digit_recognizer_view, name='digit_recognizer'),
    ]
    ```

    이 코드는 `digit_recognizer` 앱의 URL을 정의하고, `digit_recognizer_view` 함수를 호출하는 URL 패턴을 만들어줍니다. 이 경우, 사용자가 `/recognize/` 경로로 접근하면 `digit_recognizer_view` 함수가 실행되어 이미지 업로드 폼이 표시됩니다.


6. **전체 프로젝트의 URL에 앱 URL 매핑**: 프로젝트의 `urls.py` 파일에서 `digit_recognizer` 앱의 URL을 매핑합니다.

    ```python
    # field_project/urls.py

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('digit_recognizer/', include('digit_recognizer.urls')),
    ]
    ```

이렇게 하면 `digit_recognizer` 앱이 PNG 파일을 입력으로 받고 모델을 통해 분류 결과를 받을 수 있는 구조가 됩니다.

7. **INSTALLED_APPS 에 앱(digit_recognizer) 등록하기**:

    `INSTALLED_APPS`에 앱을 등록하는 것은 Django 프로젝트의 설정 파일인 `settings.py`에서 이루어집니다. 아래는 `INSTALLED_APPS`에 `digit_recognizer` 앱을 등록하는 방법입니다.

    1. Django 프로젝트의 `settings.py` 파일을 엽니다.

    2. `INSTALLED_APPS` 리스트에 `digit_recognizer` 앱을 추가합니다. `digit_recognizer`는 앱의 이름이므로, 실제로는 `apps.py` 파일 내의 `DigitRecognizerConfig` 클래스를 지정해야 합니다.

    예시:

        ```python
        # settings.py

        INSTALLED_APPS = [
            # 기존 앱들...
            'digit_recognizer.apps.DigitRecognizerConfig',
        ]
        ```



    3. 변경사항을 저장하고 Django 서버를 재시작합니다. (8번 항목에서 makemigrations 절차 진행)

    이제 `DigitRecognizerModel` 클래스가 정상적으로 등록되어 에러가 사라져야 합니다.

8. **마이그레이션 및 데이터베이스 업데이트**: 앱 내의 모델을 생성했다면, 마이그레이션을 수행하고 데이터베이스를 업데이트합니다.

    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```

9. **체크하기**:
    ```
    python manage.py runserver
    ```

    아래 주소에서 테스트 가능합니다.
    http://127.0.0.1:8000/digit_recognizer/recognize/