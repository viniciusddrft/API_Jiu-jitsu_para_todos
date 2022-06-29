class WallpaperModel:
    def __init__(self, url):
        self.url = url

    def toJson(self):
        return {
            'url': self.url
        }
