# club_app
ゲスト用アカウント
- 一般ユーザー（部員）--- username = guest-1  |  password = gt-pass-1234
- 教師用ユーザー ---------- username = guest-2  |  password = gt-pass-1234
- /adminへのアクセス用 -- username = guest-0  |  password = gt-pass-1234

## 概要
このリポジトリは、Djangoフレームワークを用いたウェブアプリケーションで、Dockerを使用して環境を構築しています。  
このアプリケーションは、部活動で必要となるツールを集めたものです。これまでアナログで行っていたことをデジタルで行うことを目的として、制作されました。

### 構成図
![architecture drawio (2)](https://github.com/Minto312/club_app/assets/116410621/fc9d1934-d4dc-4124-9e54-458f2252c5b2)

### account:
アカウント管理をする機能。
- サインイン | sign_in  
   ユーザーがログインしていない状態でアプリケーションにアクセスすると、このページにリダイレクトされる。
   
- ユーザー登録 | register
- マイページ | mypage  
   以下のユーザー情報の修正を行える。
  - ユーザー名
  - 氏名
  - 4桁番号（学籍番号）
  - ユーザーアイコン  

### attendance:
出席管理をする機能
- 出席表 | attendance  
   ボタン3種 ()内は教師用アカウントのみに表示
     - 欠席ボタン
     - （二次元コード生成）
     - （活動日の登録への遷移）
       
- 活動日の登録 | activity
  活動日を登録する機能  
  カレンダー上で色が変わっている部分が活動あり。  
  クリックすることで、トグルすることができる。  
  データベースに登録されていない場合には、初期値として平日すべてが選択される。  

### club_app:
   - htmlのヘッダー部 | base  
   - ミドルウェア | middleware  
     ユーザーがログインしていない状態でアクセスした際に、sign_inにリダイレクトさせるためのもの  

### home:
各アプリケーションへのリンクがある

### information:
お知らせ・配布物 | information  
テキストメッセージと画像、ファイルを追加・表示できる  

### score:
点数の記録をする機能


### これから実装したい機能
- 今日の出席人数、欠席人数を把握する
- 資格試験をサポートする
  - 資格試験の申込日、受験日をリマインドする機能


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
