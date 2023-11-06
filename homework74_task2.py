class Channel:
    def __init__(self, name):
        self.name = name
        self.subscribers = set()
        self.videos = []

    def add_subscriber(self, subscriber):
        self.subscribers.add(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)

    def publish_video(self, video_title):
        new_video = Video(video_title)
        self.videos.append(new_video)
        self.notify_subscribers(new_video)

    def notify_subscribers(self, video):
        for subscriber in self.subscribers:
            subscriber.receive_notification(video)

class Subscriber:
    def __init__(self, name):
        self.name = name

    def receive_notification(self, video):
        print(f"{self.name} отримав сповіщення про нове відео: {video.title}")

class Video:
    def __init__(self, title):
        self.title = title


channel = Channel("Мій канал")
subscriber1 = Subscriber("Підписник 1")
subscriber2 = Subscriber("Підписник 2")

channel.add_subscriber(subscriber1)
channel.add_subscriber(subscriber2)

channel.publish_video("Відео 1")

channel.remove_subscriber(subscriber2)

channel.publish_video("Відео 2")

