from collections import defaultdict


class Hub:
    def __init__(self):
        self.response_mapper = defaultdict(set)

    def subscribe_dec(self, *topics):
        def __subscribe(subscriber_function):
            for topic in topics:
                self.response_mapper[topic].add(subscriber_function)
            return subscriber_function

        return __subscribe

    def subscribe(self, func, *topics):
        for topic in topics:
            if func not in self.response_mapper[topic]:
                self.response_mapper[topic].add(func)
        return func

    def unsubscribe(self, func, *topics):
        print('Unsubbing' + str(topics))
        for topic in topics:
            self.response_mapper[topic].remove(func)
        return func

    def publish(self, *topics, **kwargs):
        for subscriber in self.response_mapper['DEFAULT']:
            subscriber(**kwargs)
        for topic in topics:
            for subscriber in self.response_mapper[topic]:
                subscriber(**kwargs)


eventHub = Hub()
