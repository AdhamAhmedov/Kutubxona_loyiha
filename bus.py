import queue

class EventBus:
    def __init__(self):
        # Voqealarni navbatga qo'yish uchun xizmat qiladi
        self.event_queue = queue.Queue()
        # Voqeani eshituvchi handlerlar ro'yxati
        self.handlers = []

    def register_handler(self, handler):
        # Yangi handlerlarni ro'yxatdan o'tkazish[cite: 1]
        self.handlers.append(handler)

    def post_event(self, event):
        # Yangi voqeani navbatga qo'shish[cite: 1]
        self.event_queue.put(event)

    def start(self):
        # Voqealarni navbatdan olib, handlerlarga tarqatish[cite: 1]
        while True:
            event = self.event_queue.get()
            for handler in self.handlers:
                handler.handle(event)
            self.event_queue.task_done()