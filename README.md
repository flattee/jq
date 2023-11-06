# jq



# set
https://github.com/J-Quants/jquants-api-client-python

設定
認証用のメールアドレス/パスワードおよびリフレッシュトークンは設定ファイルおよび環境変数を使用して指定することも可能です。 設定は下記の順に読み込まれ、設定項目が重複している場合は後に読み込まれた値で上書きされます。

/content/drive/MyDrive/drive_ws/secret/jquants-api.toml (Google Colab のみ)
${HOME}/.jquants-api/jquants-api.toml
jquants-api.toml
os.environ["JQUANTS_API_CLIENT_CONFIG_FILE"]
${JQUANTS_API_MAIL_ADDRESS}, ${JQUANTS_API_PASSWORD}, ${JQUANTS_API_REFRESH_TOKEN}


[jquants-api-client]
mail_address = "*****"
password = "*****"
refresh_token = "*****"
