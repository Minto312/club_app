# club_app

## 概要
このリポジトリは、Djangoフレームワークを用いたウェブアプリケーションです。Dockerを使用して環境を構築し、アカウント管理、出席管理、ホームページ、情報管理、スコアリングなどの複数のモジュールがあります。各モジュールはDjangoの典型的な構成（モデル、ビュー、テンプレート）を持ち、アプリケーションの様々な機能を提供します。

### 構成図
[構成図](/architecture.png)

### account:
アカウント管理をする機能。

### attendance:
出席管理

### club_app:

### home:
ホームページ

### information:
お知らせ・配布物

### score:
点数の記録


### ディレクトリ構造
```
D:.
│  README.md
│  .gitignore
│  docker-compose.yml
│
├─club_app
│  │  manage.py
│  │  requirements.txt
│  │  uwsgi.ini
│  │  Dockerfile
│  │
│  ├─account
│  │  │  __init__.py
│  │  │  admin.py
│  │  │  apps.py
│  │  │  forms.py
│  │  │  tests.py
│  │  │  urls.py
│  │  │  models.py
│  │  │  NotoSansJP-Medium.ttf
│  │  │  default_icon_generator.py
│  │  │  views.py
│  │  │  
│  │  ├─static
│  │  │  └─account
│  │  │          register.css
│  │  │          sign_in.js
│  │  │          mypage.css
│  │  │          sign_in.css
│  │  │
│  │  ├─templates
│  │  │  └─account
│  │  │          register.html
│  │  │          sign_in.html
│  │  │          sign_out.html
│  │  │          MyPage.html
│  │  │
│  │  │
│  │  └─migrations
│  │      │  __init__.py
│  │
│  ├─attendance
│  │  │  __init__.py
│  │  │  apps.py
│  │  │  admin.py
│  │  │  models.py
│  │  │  urls.py
│  │  │  views.py
│  │  │
│  │  ├─migrations
│  │  │  │  __init__.py
│  │  │
│  │  ├─static
│  │  │  └─attendance
│  │  │          activity.js
│  │  │          attendance.css
│  │  │          attendance.js
│  │  │
│  │  ├─templates
│  │  │  └─attendance
│  │  │          activity.html
│  │  │          attendance.html
│  │  │
│  │  │
│  │  └─tests
│  │      │  __init__.py
│  │      │  test_models.py
│  │      │  test_views.py
│  │      │  test_urls.py
│  │
│  ├─club_app
│  │  │  __init__.py
│  │  │  asgi.py
│  │  │  wsgi.py
│  │  │  urls.py
│  │  │  middleware.py
│  │  │  settings.py
│  │  │
│  │  │
│  │  ├─templates
│  │  │  └─club_app
│  │  │          base.html
│  │  │
│  │  ├─static
│  │  │  └─club_app
│  │  │          club_logo.png
│  │  │          club_logo_min.png
│  │  │          favicon.ico
│  │  │          base.js
│  │  │          base.css
│  │  │
│  │  └─media
│  │      └─profile_icon
│  │              user0.jpg
│  │
│  ├─information
│  │  │  __init__.py
│  │  │  admin.py
│  │  │  apps.py
│  │  │  tests.py
│  │  │  urls.py
│  │  │  models.py
│  │  │  views.py
│  │  │
│  │  ├─migrations
│  │  │  │  __init__.py
│  │  │
│  │  │
│  │  ├─static
│  │  │  └─information
│  │  │          information.js
│  │  │          information.css
│  │  │
│  │  └─templates
│  │      └─information
│  │              information.html
│  │
│  ├─score
│  │  │  __init__.py
│  │  │  admin.py
│  │  │  apps.py
│  │  │  models.py
│  │  │  tests.py
│  │  │  urls.py
│  │  │  views.py
│  │  │
│  │  ├─templates
│  │  │  └─score
│  │  │          recording.html
│  │  │          score.html
│  │  │
│  │  │
│  │  ├─migrations
│  │  │  │  __init__.py
│  │  │
│  │  └─static
│  │      └─score
│  │              recording.css
│  │              recording.js
│  │              score.css
│  │              score.js
│  │
│  ├─home
│  │  │  admin.py
│  │  │  apps.py
│  │  │  models.py
│  │  │  tests.py
│  │  │  __init__.py
│  │  │  urls.py
│  │  │  views.py
│  │  │
│  │  ├─migrations
│  │  │  │  __init__.py
│  │  │
│  │  ├─templates
│  │  │  └─home
│  │  │          home.html
│  │  │
│  │  └─static
│  │      └─home
│  │              attendance-back.png
│  │              certificate-back.png
│  │              home.css
│  │              information-back.png
│  │              score-back.png
│  │
│  └─media
│      ├─profile_image
│      │      user0.jpg
│      │
│      └─message
│          ├─file-message
│          └─image-message
│
└─nginx
   │  entrypoint.sh
   │  Dockerfile
   │  nginx.conf
   │
   ├─static
   └─club-introduction
       │  README.md
       │  icon.ico
       │  index.html
       │  script.js
       │  style.css
       │
       ├─fonts
       └─images
```
