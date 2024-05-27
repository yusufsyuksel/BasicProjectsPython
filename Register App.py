import json
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        # load users from .json file
        self.loadUser()

    def loadUser(self):
        if os.path.exists('73-users.json'):
            with open('73-users.json','r',encoding='utf-8') as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username = user['username'], password = user['password'], email = user['email'])
                    self.users.append(newUser)
            print(self.users)

    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print('Kullanıcı Oluşturuldu')

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print('login yapıldı.')
                break

    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        return 'Çıkış Yapıldı'

    def identity(self):
        if self.isLoggedIn:
            return f'username:{self.currentUser.username}'
        else:
            return 'Giriş yapılmadı.'


    
    def savetoFile(self):
        list = []

        for user in self.users:
            list.append(json.dumps(user.__dict__))

        with open('73-users.json','w') as file:
            json.dump(list, file)

repository = UserRepository()

while True:
    print('Menü' .center(50,'*'))
    secim = input('1-Register\n2-Login\n3-Logout\n4-identity\n5-Exit\nseçiminiz: ')
    if secim == '5':
        break
    elif secim == '1':
        username = input('username: ')
        password = input('password: ')
        email = input('email: ')

        user = User(username=username, password=password, email=email)
        repository.register(user)
    elif secim == '2':
        if repository.isLoggedIn:
            print('zaten girdin amcık')
        else:
            username = input('username: ')
            password = input('password: ')
            repository.login(username, password) 

    elif secim == '3':
        print(repository.logout())
    elif secim == '4':
        print(repository.identity())
    else:
        print('yanlış seçim')