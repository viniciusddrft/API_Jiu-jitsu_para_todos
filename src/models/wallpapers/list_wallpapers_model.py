class ListWallpapersModel:

    def __init__(self, wallpapers):
        self.wallpapers = wallpapers

    def toJson(self):
        listWallpapers = []
        for wallpaper in self.wallpapers:
            listWallpapers.append(wallpaper.toJson())
        return listWallpapers
