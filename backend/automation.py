import os
import webbrowser
import datetime
import urllib.parse
from backend.browserControl import openYoutube,searchYoutube, open_youtube_video,openGoogle,searchGoogle,open_first_website, scroll_down, scroll_up,start_whatsapp,send_whatsapp_message


def handle_command(text):
    text = text.lower()

    if "open youtube" in text:
        return openYoutube()
    if "search in youtube for" in text:
        query = text.replace("search in youtube for", "").strip()
        if query:
            return searchYoutube(query)
    if "play video"  in text:
        video_name = text.replace("play video", "").strip()
        if video_name:
            return open_youtube_video(video_name)
    

    if "open google" in text:
        openGoogle()
        return "Opening Google"
    if "search in google for" in text:
        query = text.replace("search in google for", "").strip()
        if query:
            return searchGoogle(query)
    if "open website" in text:
        query = text.replace("open website", "").strip()
        if query:
            return open_first_website(query)
    
    if "scroll down" in text:
        return scroll_down()
    if "scroll up" in text:
        return scroll_up()
    if "open whatsapp" in text:
        print("Opening Whatsapp")
        return start_whatsapp()
    if "send whatsapp message to" in text.lower():
        try:
            parts = text.lower().split("to")[1]
            contact, message = parts.split("saying")
            contact = contact.strip()
            message = message.strip()
            return send_whatsapp_message(contact, message)

        except:
            return "Sorry, I could not understand the contact or message."    

    if "open vs code" in text or "open visual studio" in text:
        os.system("code")
        return "Opening VS Code"

    if "time" in text:
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {now}"

    if "shutdown" in text:
        os.system("shutdown /s /t 5")
        return "Shutting down in 5 seconds"

    return None
