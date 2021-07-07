

class sortAlphabetically:
    ''' Ordena lista de objetos solicitada alfabeticamente. '''
    
    def __init__(self, list_of_objects, field):
        self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.ordered_list = []
        self.list_of_objects = list_of_objects
        self.order_by = field
    
    def sort(self):
        for letra in self.alphabet:
            for usuario in self.list_of_objects:
                if letra == usuario[self.order_by][0].lower():
                    self.ordered_list.append(usuario)
        return self.ordered_list


class sortNumerically:
    ''' Ordena lista de objetos solicitada de menor a mayor numericamente. '''

    def __init__(self, list_of_objects, field):
        self.ordered_list = []
        self.list_of_objects = list_of_objects
        self.age_cout = 0
        self.order_by = field

    def sort(self):
        while self.age_cout < 150:
            self.age_cout = self.age_cout + 1

            for usuario in self.list_of_objects:    
                if self.age_cout == int(usuario[self.order_by]):
                    self.ordered_list.append(usuario)
        return self.ordered_list