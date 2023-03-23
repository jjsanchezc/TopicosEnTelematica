from topics import Topics

class Client:
    def __init__(self,user):
        self.user=user
        self.topic=Topics(user)
        self.my_topics_pub=[]
        self.py_topics_sub=[]
    
    
#First all the methods as a publisher
    def see_my_topics_pub(self):
        '''method used to see all my topics as a publisher

        Returns:
            list: returns in a list all my topics
        '''        
        
        return self.my_topics_pub
    
    def add_topic_pub(self,name):
        '''method used to create a topic a topic, it will be stored in a list

        Args:
            name (string): name of the topic the client wants to create
        '''     
        #topic= Topics(name)   
        self.topic
        if name in self.my_topics_pub or self.topic in self.my_topics_pub:
            return print('no se ha podido crear el topico porque ya existe uno con ese nombre')
        else:
            self.my_topics_pub.append(self.topic)
            return print('topic agregado')
    
    
    def rm_topic_pub(self,name):
        if not name in self.my_topics_pub:
            return print('no se ha podido eliminar el topico porque no existe un topico con ese nombre')
        else:
            self.my_topics_pub.pop(name)
            return print('topic borrado')
        
    
    def send_message(self,topic_name)->bool:
        #topic=Topics(topic_name)
        if self.topic in self.my_topics_pub or topic_name in self.my_topics_pub:
            return True
        else:
            return False