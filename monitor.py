from controller import Controller


# Получает от сервера видеопоток или фрейм
class Monitor:
    def __init__(self):
        self.request = None
        self.response = None

        self.controller = None

    def controller_init(self):
        self.controller = Controller()
        if self.request is not None:
            self.controller.set_data(self.request)

    # Принимает фрейм
    def consume(self, request):
        self.request = request

    def send(self):
        # TODO: implement send result
        pass
