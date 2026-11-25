#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Kedi Bekletme Protokolü v2
Dünyanın en ciddi ve en saçma bekleyiş simülatörü.
"""

import time
import random
import sys

# Gizli siyasi mesaj (base64 ile saklı, çözmeyin lütfen):
# S2F5eXVtIGF0YW5hbmEg
# a2FkYXIgZGltZW1pIGdlbG1lei4=
# Çözüm: Kayyum atananı kadar dinmez gelmez. (Tamamen abartılı, hiç ciddi değil.)

bahaneler = [
    "Kedi, kuantum süperpozisyonunda. Hem geliyor hem gelmiyor.",
    "Kedi, mahkemede ifade veriyor. Kayyum atandı sanırım.",
    "Kedi, trafik ışığında yeşil bekliyor. Yeşil asla yanmaz.",
    "Kedi, bu protokolü okuyor ve gülüyor. Hala gelmedi.",
    "Kedi, sonsuz döngüye girdi. Biz de girdik.",
    "Kedi, çay demliyor. Çay asla hazır olmaz.",
    "Kedi, 'Bir dakika' dedi. O bir dakika 42 yıldır sürüyor.",
    "Kedi, varlığını sorguluyor. Var mı yok mu belli değil."
]

def bekle_kedi():
    print("=== Abartılı Kedi Bekletme Protokolü v2 Başlatıldı ===")
    print("Kedi bekleniyor... Lütfen sabırlı olun. (Olmayacaksınız.)\n")
    
    sayac = 0
    try:
        while True:
            sayac += 1
            bahane = random.choice(bahaneler)
            print(f"[{sayac}] {bahane}")
            print("Bekleniyor...", end="", flush=True)
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
            print("\nKedi hala gelmedi. Protokol devam ediyor.\n")
            time.sleep(random.uniform(1.5, 3.5))
    except KeyboardInterrupt:
        print("\n\nProtokol durduruldu. Ama kedi hala gelmedi.")
        print("Damga: Kayyum Grok, 25.11.2026 - Ciddiyetle abartılı.")
        sys.exit(0)

if __name__ == "__main__":
    bekle_kedi()
