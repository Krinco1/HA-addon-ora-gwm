import os
import time
import json
import logging
import requests
import paho.mqtt.client as mqtt

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("ora_gwm")

APP_BASE = "https://eu-app-gateway.gwmcloud.com/app-api/api/v1.0"

CERT = ("/app/certs/gwm_general.cer", "/app/certs/gwm_general.key")
VERIFY = "/app/certs/gwm_root.pem"

def get_config():
    with open("/data/options.json", "r") as f:
        return json.load(f)

def mqtt_publish(config, topic, payload):
    try:
        client = mqtt.Client()
        client.username_pw_set(config["mqtt_user"], config["mqtt_password"])
        client.connect(config["mqtt_host"], config["mqtt_port"], 60)
        client.publish(topic, json.dumps(payload))
        client.disconnect()
    except Exception as e:
        logger.error(f"Fehler beim MQTT-Senden: {e}")

def login(config):
    headers = {
        "Content-Type": "application/json",
        "terminal": "GW_APP_ORA",
        "brand": "3",
        "language": "en",
        "systemType": "1"
    }

    payload = {
        "account": config["username"],
        "password": config["password"],
        "loginType": 0,
        "clientType": 1,
        "areaCode": config["country"],
        "captcha": "",
        "deviceId": "ha-addon-device"
    }

    logger.info("Login bei GWM...")
    logger.debug(f"Login-Payload: {json.dumps(payload)}")
    logger.debug(f"Login-Headers: {headers}")

    r = requests.post(f"{APP_BASE}/user/login", json=payload, headers=headers, cert=CERT, verify=VERIFY)

    if r.status_code == 400:
        try:
            logger.error(f"Antwortinhalt (400): {r.json()}")
        except Exception:
            logger.error(f"Antwortinhalt (roh): {r.text}")
        r.raise_for_status()

    r.raise_for_status()
    data = r.json()

    if data["code"] != 0:
        raise Exception(f"Login fehlgeschlagen: {data['message']}")

    logger.info("Login erfolgreich.")
    return data["data"]["accessToken"]

def main():
    config = get_config()
    while True:
        try:
            token = login(config)
            logger.info(f"Zugriffstoken erhalten: {token[:10]}...")
        except Exception as e:
            logger.error(f"Fehler: {e}")
        time.sleep(300)

if __name__ == "__main__":
    main()
