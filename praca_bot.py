import requests
from bs4 import BeautifulSoup
import json
import os
import time
import random
from dotenv import load_dotenv  # Biblioteka do obsługi .env

# 1. Ładowanie zmiennych środowiskowych
load_dotenv()

# 2. Dynamiczna konfiguracja
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# Dynamiczna ścieżka do bazy (zadziała na każdym komputerze)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PLIK_BAZA = os.path.join(BASE_DIR, "wyslane_ogloszenia.json")

URLS_LISTA = [
    "https://it.pracuj.pl/praca/devops;kw/gliwice;wp?rd=30&et=17",
    "https://it.pracuj.pl/praca/gliwice;wp?rd=30&its=it-admin",
    "https://it.pracuj.pl/praca/gliwice;wp?rd=30&et=17&its=devops",
    "https://it.pracuj.pl/praca/gliwice;wp?rd=30&et=17&its=it-admin",
    "https://it.pracuj.pl/praca?its=ai-ml"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

# --- FUNKCJE (bez zmian logicznych, używamy tylko PLIK_BAZA i WEBHOOK_URL) ---

def wczytaj_baze():
    if not os.path.exists(PLIK_BAZA): return []
    try:
        with open(PLIK_BAZA, 'r', encoding='utf-8') as f: return json.load(f)
    except: return []

def zapisz_baze(lista):
    with open(PLIK_BAZA, 'w', encoding='utf-8') as f: json.dump(lista[-500:], f, ensure_ascii=False)

def powiadom_discord(tytul, link, firma):
    if not WEBHOOK_URL:
        print("BŁĄD: Brak WEBHOOK_URL w pliku .env")
        return
    try:
        msg = f"**Nowa oferta!** 🚀\n**Stanowisko:** {tytul}\n**Firma:** {firma}\n**Link:** {link}"
        requests.post(WEBHOOK_URL, json={"content": msg})
        time.sleep(1)
    except: pass

def main():
    print("--- START BOTA ---")
    wyslane = wczytaj_baze()
    pierwszy_raz = (len(wyslane) == 0)
    
    if pierwszy_raz:
        print("--> Tryb INICJALIZACJI (Zapełniam bazę bez wysyłania powiadomień)")
    
    nowe_liczb = 0
    
    for url in URLS_LISTA:
        print(f"Sprawdzam link: {url[:40]}...")
        try:
            r = requests.get(url, headers=HEADERS, timeout=10)
            soup = BeautifulSoup(r.text, 'html.parser')
            
            oferty = soup.find_all('div', attrs={'data-test': 'default-offer'})
            if not oferty:
                oferty = soup.find_all('div', attrs={'data-test': 'job-offer'})
            
            for o in oferty:
                link_tag = o.find('a', attrs={'data-test': 'link-offer'})
                if not link_tag: continue
                link = link_tag['href']
                
                if link in wyslane: continue
                
                title_tag = o.find('h2', attrs={'data-test': 'offer-title'})
                tytul = title_tag.text.strip() if title_tag else "Stanowisko"
                
                company_tag = o.find('h4', attrs={'data-test': 'text-company-name'})
                firma = company_tag.text.strip() if company_tag else "Firma"
                
                if pierwszy_raz:
                    print(f"   [Baza] Dodano: {tytul}")
                else:
                    print(f"   [DISCORD] Wysyłam: {tytul}")
                    powiadom_discord(tytul, link, firma)
                
                wyslane.append(link)
                nowe_liczb += 1
                
        except Exception as e:
            print(f"   Błąd: {e}")
        
        time.sleep(2)

    if nowe_liczb > 0:
        zapisz_baze(wyslane)
        print(f"--- KONIEC. Zapisano {nowe_liczb} ofert. ---")
    else:
        print("--- KONIEC. Brak nowych ofert. ---")

if __name__ == "__main__":
    main()