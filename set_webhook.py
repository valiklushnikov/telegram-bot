import os
import time
import requests

TOKEN = os.getenv("TOKEN")

def get_public_url():
    for _ in range(10):
        try:
            r = requests.get("http://ngrok:4040/api/tunnels")
            tunnels = r.json()["tunnels"]
            for tunnel in tunnels:
                if tunnel["proto"] == "https":
                    return tunnel["public_url"]
        except Exception as e:
            print(f"[Webhook] Retry... {e}")
            time.sleep(2)
    return None

def set_webhook():
    public_url = get_public_url()
    if not public_url:
        print("❌ Cannot get ngrok URL")
        return

    url = f"https://api.telegram.org/bot{TOKEN}/setWebhook"
    webhook_url = f"{public_url}/"
    r = requests.post(url, data={"url": webhook_url})
    print("📡 Set webhook:", webhook_url)
    print("✅ Telegram response:", r.json())