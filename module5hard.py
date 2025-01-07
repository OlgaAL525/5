import time

class User:
    def __init__(self, nickname, password, age) :
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'{self.nickname}'


class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title


class UrTube:
    def __init__(self):
        self.users = list()
        self.videos = list()
        self.current_user = None

    def add(self, *args):
        for i in args:
            if i not in self.videos:
                self.videos.append(i)

    def get_videos(self, word):
        k = list()
        for i in self.videos:
            if word.lower() in i.title.lower():
                k.append(i.title)
        return k

    def register(self, nickname, password, age):
        us = User(nickname, password, age)
        name = list()
        for i in self.users:
            name.append(str(i))
        if str(us) not in name:
            self.users.append(us)
            self.current_user = us
        else:
            print(f'Пользователь {str(us)} уже существует')

    def log_out(self):
        self.current_user = None
        return self.current_user

    def log_in(self, nickname, password):
        for i in self.users:
            if i.nickname == nickname and i.password == hash(password):
                self.current_user = i

    def watch_video(self, name_film):
        for i in self.videos:
            if name_film == i.title:
                if self.current_user == None:
                    print('Войдите в аккаунт, чтобы смотреть видео')
                if self.current_user != None and self.current_user.age < 18 and i.adult_mode == True:
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                    self.log_out()
                if self.current_user != None and (self.current_user.age > 18 or i.adult_mode == False):
                    j = 1
                    while j <= i.duration:
                        time.sleep(0.1)
                        print(j, end = ' ')
                        j += 1
                    print('Конец видео')



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode = True)

ur.add(v1, v2)
print(ur.get_videos('лучший'))
print(ur.get_videos('прог'))


ur.watch_video('Для чего девушкам парень программист?')
ur.register('Вася', 'rere', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('Коля', ';lsfdjs0e', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('Вася', 'dht6edh', 55)
print(ur.current_user)

ur.watch_video('Для чего девушкам парень программист??')

ur.log_in('Вася','rere')
print(ur.current_user)