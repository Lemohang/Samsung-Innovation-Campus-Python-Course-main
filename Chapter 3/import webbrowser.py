import webbrowser
import requests
import re
import time

def is_connected():
    """Check if we have internet access by pinging Google."""
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def get_first_youtube_video(query):
    """Scrape YouTube search results and return the first video URL."""
    search_url = "https://www.youtube.com/results?search_query={}".format(query.replace(" ", "+"))
    response = requests.get(search_url).text

    # Find first video ID using regex (YouTube video IDs are 11 chars long)
    match = re.search(r"watch\?v=(\S{11})", response)
    if match:
        video_id = match.group(1)
        return "https://www.youtube.com/watch?v={}".format(video_id)
    return None

def open_youtube_video(query):
    """Open the first video from a YouTube search."""
    video_url = get_first_youtube_video(query)
    if video_url:
        webbrowser.open(video_url)
        print("✅ Playing:", video_url)
    else:
        print("❌ Could not find a video.")

if __name__ == "__main__":
    print("🔍 Checking internet connection...")
    time.sleep(2)

    if is_connected():
        open_youtube_video("Joshua Selman teachings")
    else:
        print("❌ No internet connection. Please connect to Wi-Fi and try again.")
