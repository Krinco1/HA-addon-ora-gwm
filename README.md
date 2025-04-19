# ORA GWM MQTT Add-on für Home Assistant

Dieses Add-on verbindet dein ORA-Fahrzeug (z. B. Funky Cat) mit Home Assistant. Es nutzt die offizielle GWM API und überträgt Fahrzeugdaten via MQTT.

## 🔧 Funktionen

- Login mit deinem ORA-Konto (separater Account empfohlen)
- Regelmäßiger Abruf von Fahrzeugdaten (Status, VIN, etc.)
- MQTT-Integration kompatibel mit Mosquitto
- Konfiguration über Home Assistant Add-on Oberfläche

## 📦 Installation

1. Dieses Repository in Home Assistant hinzufügen:
https://github.com/Krinco1/ha-addon-ora-gwm

2. Add-on installieren & konfigurieren
3. MQTT-Verbindung und Fahrzeugdaten prüfen

## ⚠️ Hinweise

- Verwende nach Möglichkeit einen eigenen ORA-Account zur Verknüpfung mit dem Fahrzeug, da du ansonsten immer aus der App abgemeldet wirst.
- 
- WICHTIG: Das Passwort darf KEINE Sonderzeichen enthalten. Mann kann das zwar in der Erstanlage machen, aber für die API darf das nicht sein. Wenn man in der APP einen PW-Wechsel macht, kommt auch der Hinweis, dass es 8 Buchstaben oder Zahlen, davon mind. 1 Zahl und ein Großbuchstabe sein müssen. Aber keine Zeichen, garkeine!! Der PW-Wechsel in der APP funktioniert ohnehin nicht wirklich, wesshalb man das am besten über die PW Vergessen-Funktion macht. dann geht es!
- 
- Das Add-on sendet regelmäßig Daten an MQTT – prüfe dein Topic `ora/<vin>/status`.

## 📁 MQTT-Beispiele

- `ora/LP123456789012345/status`
- `ora/LP123456789012345/info`

## 🙌 Danke an zivillian für die Vorarbeit ([ora2mqtt](https://github.com/zivillian/ora2mqtt))
