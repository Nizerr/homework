import logging

"""" 
Модуль logging в Python використовується для реалізації логування, тобто запису подій і інформації в лог-файл.
У контексті патерну Proxy, логування
використовується для реєстрації звернень до проксі-класу DataSourceProxy та класу DataSource.
В коді, який я надав, logging.basicConfig встановлює конфігурацію логування, 
включаючи ім'я файлу для логування та рівень логування 
(у цьому випадку, INFO, що означає запис лише повідомлень рівня INFO і вище).
Всі логи створюються за допомогою logging.info, інформація про події записується в лог-файл.
Це допомагає відстежувати звернення до даних та події, що стосуються доступу до даних.
Логування допомагає при налагодженні та моніторингу програми, 
а також при відлагодженні можливих проблем або незрозумілих поведінок."""

class DataSource:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataSource, cls).__new__(cls)
            cls._instance._data = []
            cls._instance._observers = []
        return cls._instance

    def update_data(self, new_data):
        self._data = new_data
        logging.info("Data updated")
        self.notify_observers()

    def get_data(self):
        logging.info("Accessed data")
        return self._data

    def attach(self, observer):
        self._observers.append(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update()

class DataSourceProxy:
    def __init__(self):
        self._real_data_source = DataSource()

    def update_data(self, new_data):
        self._real_data_source.update_data(new_data)

    def get_data(self):
        return self._real_data_source.get_data()

    def attach(self, observer):
        self._real_data_source.attach(observer)

class DataObserver:
    def __init__(self, data_source):
        self._data_source = data_source
        self._data_source.attach(self)

    def update(self):
        logging.info("Data has been updated: %s", self._data_source.get_data())

if __name__ == "__main__":
    logging.basicConfig(filename="data_access.log", level=logging.INFO)

    data_source_proxy = DataSourceProxy()
    observer = DataObserver(data_source_proxy)

    data = data_source_proxy.get_data()
    print("Data:", data)

    new_data = [1, 2, 3, 4, 5]
    data_source_proxy.update_data(new_data)

    data = data_source_proxy.get_data()
    print("Data (after update):", data)
