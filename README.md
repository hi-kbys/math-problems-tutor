# Math Problem Tutorについて
数学の問題を解くのに役立つアプリです。
わからないところや気になる点について質問するとChatGPTによる回答を得ることができます。

# 依存関係
## バックエンド
- 言語:Python 3.11
- パッケージ管理: Poetry 
- フレームワーク: FastAPI
- テストフレームワーク: Pytest
## フロントエンド
- 言語: TypeScript
- パッケージ管理: Yarn
- フレームワーク: React
## データベース
- MySQL
## 開発基盤
- Docker

# Getting Started
## 1. Install
現状WSLで開発してますが、Macでも動く…はずです。
1. Docker Desktopをインストール
1. Docker Composeをインストール
1. 動作確認
    ```bash
    docker-compose up
    ```
    で起動できればOKです。
1. データベースの初期化
    db_migrate.pyを実行してデータベースを作成します。
    ```bash
    docker-compose exec 
    mpt_app poetry run python -m mpt_app.migrate_db
    ```
1. アクセスの確認
    フロントはhttp://localhost:3000 にアクセスして、Reactの画面が表示されればOKです。
    バックエンドはhttp://localhost:8000/docs にアクセスして、FastAPIのOpenAPIの管理画面が表示されればOKです。

## 2.VsCodeでの開発
Remote Containerを使用して開発しています。

1. Remote Containerをインストール
1. >Remote-Containers: Open Folder in Container... でこのリポジトリを開く
### 注意点
1. GitはRemote Container内ではなく、ホスト側で行う(この辺は後でできるようになるかも？？)


# 開発ルールについて
## prefixについて
コミットメッセージのprefixについては以下のようにします。
- feat: A new feature
- fix: A bug fix
- docs: Documentation only changes 
- style: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- refactor: A code change that neither fixes a bug nor adds a feature
- perf: A code change that improves performance
- test: Adding missing or correcting existing tests
- chore: Changes to the build process or auxiliary tools and libraries such as documentation generation