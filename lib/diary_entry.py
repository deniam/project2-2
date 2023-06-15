class DiaryEntry:
    def __init__(self, title, contents):
        self._read_so_far = 0
        self._title = title
        self._contents = contents
        if title == "" or contents == "":
            raise Exception("Please enter a title and contents!")

    def format(self):
        return f"{self._title}: {self._contents}"

    def count_words(self):
        return len(self._contents.split())

    def reading_time(self, wpm):
        self.wpm = wpm
        return len(self._contents.split()) / wpm

    def reading_chunk(self, wpm, minutes):
        words_user_can_read = wpm * minutes
        words = self._contents.split()
        start_chunk = self._read_so_far
        end_chunk = self._read_so_far + words_user_can_read
        chunk = words[start_chunk:end_chunk]
        self._read_so_far = end_chunk
        return ' '.join(chunk)
        
    