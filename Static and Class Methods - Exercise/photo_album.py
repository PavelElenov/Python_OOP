from math import ceil


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = []
        for i in range(self.pages):
            self.photos.append([])

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label):
        for pages in range(len(self.photos)):
            if len(self.photos[pages]) < 4:
                self.photos[pages].append(label)
                return f"{label} photo added successfully on page {pages + 1} " \
                       f"slot {len(self.photos[pages])}"
        return "No more free slots"

    def display(self):
        ll = ['-' * 11]
        for pages in self.photos:
            if len(pages) > 0:
                result = ''
                for photo in pages:
                    result += "[]" + " "
                ll.append(result.strip())
            else:
                ll.append('')
            ll.append('-' * 11)

        return '\n'.join(str(x) for x in ll)


# album = PhotoAlbum.from_photos_count(12)
# print(album.pages)
# print(album.photos)