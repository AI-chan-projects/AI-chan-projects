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
