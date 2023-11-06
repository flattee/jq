import jquantsapi


cli = jquantsapi.Client()
listed_info = cli.get_listed_info()
listed_info.to_csv("info.csv")
