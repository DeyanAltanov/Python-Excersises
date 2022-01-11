class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = []
        for page in range(self.pages):
            self.photos.append([])

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(int(photos_count / 4))

    def add_photo(self, label):
        if len(self.photos[-1]) == 4:
            return "No more free spots"
        for page in range(0, len(self.photos) + 1):
            if len(self.photos[page]) < 4:
                current_slot = len(self.photos[page]) + 1
                for slot in range(current_slot + 1, 6):
                    self.photos[page].append(label)
                    return f"{label} photo added successfully on page {page + 1} slot {slot - 1}"

    def display(self):
        result = ''
        for page in range(len(self.photos)):
            is_result = False
            result += "-----------\n"
            for slot in range(len(self.photos[page])):
                if self.photos[page][slot]:
                    result += "[] "
                    is_result = True
            result = result.rstrip()
            result += '\n'
        if not is_result:
            result += '\n'
        result += "-----------\n"
        return result