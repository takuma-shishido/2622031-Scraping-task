# 2622031-Scraping-task

武蔵野大学Webサイト（https://www.musashino-u.ac.jp/）のサイトマップを抽出するスクリプトです。

## 内容

- トップページから同一ドメイン内のリンクを幅優先で辿ります
- 全ページの URL を key、`<title>` の文字列を value として辞書型変数に格納します
- 辞書型変数をもとに `sitemap.csv` に保存します
- サーバーへの負荷を減らすため、アクセスごとに `time.sleep(1)` で待機します

## 実行方法

```bash
pip install -r requirements.txt
python scraping.py
```

## ファイル

| ファイル | 内容 |
|---|---|
| `scraping.py` | クローラー本体 |
| `sitemap.csv` | 抽出結果（url, title） |
