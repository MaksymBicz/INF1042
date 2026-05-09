from chat import Chat
class Lion(Chat):
    def parler(self):
        return super().parler() + ' (roar)'
