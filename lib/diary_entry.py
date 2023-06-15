class DiaryEntry:
    def __init__(self, title, contents):
        self._title = title
        self._contents = contents

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
        chunk = words[:words_user_can_read]
        return ' '.join(chunk)
        
    