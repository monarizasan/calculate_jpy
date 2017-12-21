# calculate_jpy

取引所から取得できるBTC取引履歴のcsvファイルに日本円換算の金額の列を追加します。

日本円換算は https://www.cryptocompare.com/api/ のAPIを利用しています。

mac-OSXで動作確認。pandasを利用しています。

`pip3 install pandas`

Poloniex用とBittrex用のスクリプトがあります。Bittrex用のスクリプトでは、日本円換算に"Opened"の時刻を利用しています。

`git clone https://github.com/monarizasan/calculate_jpy.git`

このリポジトリをgit cloneしたら、それぞれCSVファイルをダウンロードして同じフォルダ内に入れます。

`python3 calculate_jpy_poloniex.py --file tradeHistory.csv`

`python3 calculate_jpy_bittrex.py --file fullOrders.csv`

を実行するとそれぞれ

`poloniex_result20171221230101.csv`

`bittrex_result20171221230101.csv`

と日付と時間情報がついた名前のファイルが同じフォルダ内に作成され、CSVファイルにUNIXTIME、同時刻の1BTCあたりの日本円価格、取引で動いた量の日本円価格の列が追加されています。

このスクリプトは現段階では作者が自身の取引の計算のために実験的に作成したもので、実際に税金計算などに使用して仮に損害が発生しても作者は責任を負えません。
