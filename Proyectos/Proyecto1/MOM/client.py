from topics import Topics


class Client:
    def __init__(self, user):
        self.user = user
        self.my_topics_pub = ['Musica']
        self.py_topics_sub = []


# First all the methods as a publisher


    def see_my_topics_pub(self):
        '''method used to see all my topics as a publisher

        Returns:
            list: returns in a list all my topics
        '''
        print(f'esta es la lista de topicos que tienes{self.my_topics_pub}')
        return self.my_topics_pub

    def add_topic_pub(self, name)-> bool:
        '''method used to create a topic a topic, it will be stored in a list

        Args:
            name (string): name of the topic the client wants to create
        '''
        if name in self.my_topics_pub:
            print('no se ha podido crear el topico porque ya existe uno con ese nombre')
            return False
        else:
            self.my_topics_pub.append(name)
            print('topic agregado')
            return True

    def rm_topic_pub(self, name):
        if not name in self.my_topics_pub:
            return print('no se ha podido eliminar el topico porque no existe un topico con ese nombre')
        else:
            self.my_topics_pub.pop(name)
            return print('topic borrado')

    def send_message(self, topic_name) -> bool:
        # topic=Topics(topic_name)
        if topic_name in self.my_topics_pub:
            return True
        else:
            return False
