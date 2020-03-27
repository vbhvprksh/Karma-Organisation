import sqlite3
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import  ObjectProperty

class MainWindow(Screen):
    n=ObjectProperty(None)
    l = ObjectProperty(None)

    e= ObjectProperty(None)
    a = ObjectProperty(None)
    def btn(self):
        dbase = sqlite3.connect('try2.db')
        # print("Database Opened")

        dbase.execute(''' CREATE TABLE IF NOT EXISTS try3(
                                Reg_NO TEXT  NOT NULL,
                                 Gender TEXT NOT NULL,Location  TEXT NOT NULL,Cremation_Day TEXT NOT NULL) ''')
        dbase.execute(''' INSERT INTO try2(Reg_No,Gender,Location,Cremation_day) VALUES(?,?,?,?)''', (self.n.text,self.l.text,self.e.text,self.a.text))
        dbase.commit()
        dbase.close()


class SecondWindow(Screen):
    pass


class ThirdWindow(Screen):
    pass

class FourthWindow(Screen):
    n = ObjectProperty(None)
    l = ObjectProperty(None)
    b = ObjectProperty(None)

    # e = ObjectProperty(None)
    def btn(self):
        dbase = sqlite3.connect('register.db')
        # print("Database Opened")

        dbase.execute(''' CREATE TABLE IF NOT EXISTS register(
                                    Name TEXT  NOT NULL,
                                    Contact TEXT NOT NULL) ''')
        dbase.execute(
            ''' INSERT INTO register(Name,Contact) VALUES(?,?,?)''',
            (self.n.text, self.l.text,))
        dbase.commit()
        dbase.close()

class FifthWindow(Screen):
    pass

class SixWindow(Screen):
    pass

class SeventhWindow(Screen):
    n = ObjectProperty(None)
    l = ObjectProperty(None)
    b=ObjectProperty(None)
    #e = ObjectProperty(None)
    def btn(self):
        dbase = sqlite3.connect('ybvp2.db')
        # print("Database Opened")

        dbase.execute(''' CREATE TABLE IF NOT EXISTS ybvp3(
                                Name_of_the_CORPSE TEXT  NOT NULL,
                                Location_of_the_CORPSE TEXT NOT NULL, 
                                Belonging_of_the_CORPSE  TEXT NOT NULL) ''')
        dbase.execute(''' INSERT INTO ybvp3(Name_of_the_CORPSE,Location_of_the_CORPSE,Belonging_of_the_CORPSE) VALUES(?,?,?)''', (self.n.text,self.l.text,self.b.text))
        dbase.commit()
        dbase.close()

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("yv.kv")


class   YVApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    YVApp().run()