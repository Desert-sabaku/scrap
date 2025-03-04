# つかいかた

`scrapy crawl scrap -a url="<いい感じのurl> -a depth="<適当な深さ> -o dist/<いい感じのファイル名>.jsonl"`

e.g.: `scrapy crawl scrap -a url="https://qiita.com/" -a depth=0  -O dist/data.jsonl`

動いてほしい（希望的観測）
僕のとこでは動いた

Tips: 形式は`jsonl`以外でもいい。`json`, `csv`, etc.

# 環境構築

1. `Python`をインストールしてね（[公式](https://www.python.org/downloads/)からinstallerを落とすか、Microsoft Storeで検索するのが楽、現在3.12以上じゃないと動かないよ）
2. [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)をインストールしてね
   1. 上のリンクは公式のインストーラーだよ
   2. 見るのがめんどくさい人は`(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -`を`Powershell`上で叩いてね
   3. 無事インストールできたら`%APPDATA%\pypoetry`を[環境変数](https://wa3.i-3-i.info/word11027.html)に追加してね。僕らの界隈ではよく「パスを通す」って表現するよ
   4. WSLを使ってる人はdocs読みつつ別個対応してね
3. このリポジトリをローカルにクローンしてね（下参照）
4. クローンしたディレクトリに入って`poetry install`を叩いてね
5. とりま完成！

## 参考文献、リンク
* [Python](https://www.python.org/): Python is a programming language that lets you work quickly and integrate systems more effectively.
* [Scrapy](https://scrapy.org/): A Fast and Powerful Scraping and Web Crawling Framework
* [Poetry](https://python-poetry.org): Python packaging and dependency management made easy
* etc.

`git clone https://github.com/Desert-sabaku/scrap.git`

`clone`したディレクトリ内で`git pull`を叩くとクラウドにアップされた変更がローカルにも反映される。
