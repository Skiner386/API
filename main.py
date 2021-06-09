import requests

class API:
    def __init__(self,key):
        self.key = key
        self.text = 'http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/'
    def function(self):
        if self.response.status_code == 200:
            print('Podano prawidłowy klucz')
        else:
            print('Podano zły klucz')
    def GetNews(self):
        self.text = 'http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/'

        appid = input("Podaj liczbę ")
        count = input("Ilość ")
        maxlenght = input("Maksymalna długość ")
        self.text += '?appid=' + appid + '&count=' + count + '&maxlenght=' + maxlenght
        self.response = requests.get(self.text)
        a = self.response.json()
        try:
            if len(a) > 0:
                print(a['appnews'])
            else:
                print('Nie znaleziono wiadomości')
        except:
            print('błąd')
    def Achievement(self):
        self.text = ' http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/'
        gameid = input("Podaj liczbę ")
        self.text += '?gameid=' + gameid
        self.response = requests.get(self.text)
        try:
            if len(self.response.json()) != 0:
                print(self.response.json())
            else:
                print('Nie znaleziono gry')
        except:
            print('błąd')
    def GetFriendsList(self):
        self.text = 'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=' + self.key
        steamid = input("Podaj ID ")
        relationship = input('Wybierz spośród all-friend ')
        self.text += '&steamid=' + steamid + '&relationship=' + relationship
        self.response = requests.get(self.text)
        #self.function()
        try:
            print(self.response.json())
        except:
            print('błąd')


a = API('C912C2D0B49035D8A7A33F49532DA1A4')
print('GetFriendList','GetNews','Achievement')

while True:
    b = input('Co chcesz wybrać? ')

    if b.upper() == 'GetFriendList'.upper():
        a.GetFriendsList()
    if b.upper() == 'GetNews'.upper():
        a.GetNews()
    if b.upper() == 'Achievement'.upper():
        a.Achievement()
