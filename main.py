from kivy.app import App
from android_webview import WebView  # Or kivy_garden.xcamera.WebView on some builds

class PlayerApp(App):
    def build(self):
        webview = WebView()
        webview.open_url("file:///android_asset/player.html")
        return webview

PlayerApp().run()
