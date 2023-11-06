import jquantsapi

code = "13210"  # 野村アセットマネジメント株式会社　ＮＥＸＴ　ＦＵＮＤＳ　日経２２５連動型上場投信

cli = jquantsapi.Client()
df = cli.get_prices_daily_quotes(code)
df.to_csv(code + ".csv")
