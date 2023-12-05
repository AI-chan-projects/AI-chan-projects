this document is about Django project to test in field ai models 
* python==3.11.5, django==4.2.6
* 프로젝트 폴더`field`의 `settings.py`에는 Secret Key가 비어 있습니다.
* https://djecrety.ir/ 에서 django의 key를 발급받아 복사한 다음,
* 아래 양식으로 json 파일을 작성하여 `field` 프로젝트 베이스 루트에 작성해 주세요.
  
```secrets.json
{
	"SECRET_KEY": "djecrety.ir에서복사한 key를 여기에 붙여주세요."
}
```

## Django 프로젝트 구성하는 방법(프로세스)

1. **가상 환경 설정**: 레포지토리 내에서 가상 환경을 생성합니다.

   ```bash
   python -m venv venv
   ```

2. **가상 환경 활성화**: 가상 환경을 활성화합니다.

   - Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

3. **Django 설치**: 가상 환경에서 Django를 설치합니다.

   ```bash
   pip install django
   ```

4. **Django 프로젝트 생성**: Django 프로젝트를 생성합니다.

   ```bash
   django-admin startproject field_project
   ```

5. **App 생성**: Django 앱을 생성합니다.

   ```bash
   cd field_project
   python manage.py startapp field_test
   ```

6. **모델 정의**: `field_test` 앱 내의 `models.py`에서 모델을 정의합니다.

   ```python
   from django.db import models

   class FieldTestModel(models.Model):
       # 필드 정의
       name = models.CharField(max_length=100)
       description = models.TextField()

       def __str__(self):
           return self.name
   ```

7. **Migration 생성 및 적용**: 모델 변경사항을 데이터베이스에 적용합니다.

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

8. **서버 실행**: Django 서버를 실행하여 웹 어플리케이션을 테스트합니다.

   ```bash
   python manage.py runserver
   ```

9. **웹 브라우저에서 확인**: 브라우저에서 `http://127.0.0.1:8000/`에 접속하여 웹 어플리케이션을 확인합니다.

## Django 프로젝트를 레포지토리에 구성했을 때의 장단점 분석

### 장점:

1. **프로젝트 단일화**: Django 프로젝트를 레포지토리에 구성하면 프로젝트의 소스 코드와 관련 파일들이 한 곳에 단일화되어 있습니다.
  
2. **배포 용이성**: 레포지토리를 클론하면 프로젝트 설정과 의존성을 쉽게 구축할 수 있어 배포가 간편합니다.

### 단점:

1. **레포지토리 용량 증가**: Django 프로젝트는 많은 파일과 디렉토리를 포함하므로 레포지토리의 용량이 증가할 수 있습니다.

2. **가상 환경 중복**: 여러 프로젝트에서 같은 가상 환경을 사용하는 경우 중복이 발생할 수 있습니다.

3. **환경별 설정 복잡성**: 여러 개발자가 동일한 프로젝트에 참여하는 경우 각자의 환경에 따른 설정 복잡성이 증가할 수 있습니다.

4. **프로젝트 특정 설정 파일**: 프로젝트에 특정한 설정 파일 등이 레포지토리에 저장되어 있을 경우 보안 문제가 발생할 수 있습니다.

종합적으로, 작은 규모의 프로젝트에서는 편리할 수 있지만, 대규모 프로젝트의 경우 환경 구성의 복잡성과 레포지토리 용량 증가 등의 문제가 발생할 수 있습니다. 각 프로젝트의 규모와 요구사항에 따라 결정하는 것이 중요합니다.
