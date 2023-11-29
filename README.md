# fastAPIのCI環境を構築
pytestとflake8、blackを使用してFastAPIのCI環境を構築。<br />
Qiita記事のために作成したリポジトリです。<br />


## 技術詳細
- Python
- FastAPI
- pytest(test用ライブラリ)
- flake8(linter)
- black(formatter)

## セットアップ方法

Dockerイメージをビルドする。<br />
```
make build
```

Dockerコンテナ起動。<br />
```
make up
```

依存ライブラリのインストール。<br />
```
make install
```

テーブル作成。<br />
```
①コンテナに入る
make shell

②databasesディレクトリに移動
cd src/databases

③alembicコマンドの実行
poerty run alembic upgrade head

```
## テスト実行
コンテナ起動中にのみ以下のコマンドで実行可能です。<br />
- `black`の実行
```
make fmt
```

- `flake8`の実行
```
make lint
```

- `pytest`の実行
```
make test
```



