import json


def readAppConfig():
    try:
        with open("appconfig.json", "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        with open("appconfig.json", "w") as f:
            data = {
                "app_name": "FastCode.Ninja LockDown",
                "app_version": "0.0.1",
                "app_author": "Emir Tunahan Alim",
                "app_author_email": "emrtnhalim@gmail.com",
                "app_description": "Cross-platform multi-lingual screen locker app for computers and smart boards.",
                "github_user": "https://github.com/Eta06",
                "github_repo": "https://github.com/Eta06/LockDown",
                "app_license": "Apache License 2.0",
                "app_license_url": "https://github.com/Eta06/LockDown/blob/main/LICENSE",
                "app_language": "",
            }
            json.dump(data, f, indent=4)
            return data


def updateAppConfig(key, value):
    data = readAppConfig()
    data[key] = value
    with open("appconfig.json", "w") as f:
        json.dump(data, f, indent=4)