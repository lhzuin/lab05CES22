from abc import ABC, abstractmethod

class State(ABC): #classe abstrata representando um estado e seus métodos (interface)
    @abstractmethod
    def render(self): #documento submetido para moderação
        pass
    @abstractmethod
    def publish(self, user, approved_status): #documento é publicado ou rejeitado no site
        pass
    @abstractmethod
    def expire(self): #licensa do documento é expirada
        pass

class Document(): # documento criado pelo usuário
    def __init__(self):
        print('Document was just created')
        self.state = Draft(self)
    def render(self):
        self.state.render()
    def publish(self, user, approved_status):
        self.state.publish(user, approved_status)
    def expire(self):
        self.state.expire()
    def _change_state(self, new_state):
        self.state = new_state

class Draft(State):
    def __init__(self, document):
        self.document = document
        print("The document is in Draft state")
    def expire(self):
        pass
    def render(self):
        self.document._change_state(Moderation(self.document))
    def publish(self, user, approved_status):
        if (user.is_adm and approved_status):
            self.document._change_state(Published(self.document))


class Moderation(State):
    def __init__(self, document):
        self.document = document
        print("The document is in Moderation state")
    def render(self):
        self.document._change_state(Moderation(self.document))
    def publish(self, user, approved_status):
        if approved_status:
            self.document._change_state(Published(self.document))
        else:
            self.document._change_state(Draft(self.document))
    def expire(self):
        pass

class Published(State):
    def __init__(self, document):
        self.document = document
        print("The document is in Published state")
    def expire(self):
        self.document._change_state(Draft(self.document))
    def render(self):
        pass
    def reject(self):
        pass
    def publish(self, user, approved_status):
        pass


class User: # usuário que tenta modificar status do documento
    def __init__(self, is_adm):
        self.is_adm = is_adm

if __name__ == '__main__': # implementação de um teste
    d = Document()
    d.render()
    d.publish(User(False), True)
    d.expire()
    d.publish(User(False), True)
    d.render()
    d.publish(User(True), False)


