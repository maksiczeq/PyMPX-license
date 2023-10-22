# KOD (B) WER. PERSONALNA

# Zasoby (Import bibliotek, tytuły, stringi.)
from pytube import YouTube
from colorama import init, Fore, Style
from bs4 import BeautifulSoup
import os
import time
import sys
import re


# Inicjcja Coloramy
init()
# Tytuł ASCII
tytul_ascii = r'''
    ____        __  _______ _  __    
   / __ \__  __/  |/  / __ \ |/ /    
  / /_/ / / / / /|_/ / /_/ /   /     
 / ____/ /_/ / /  / / ____/   |      
/_/    \__, /_/  /_/_/   /_/|_|      
      /____/                         
      '''


tytul_ascii_mini = r'''
   ___       __  ______  _  __  
  / _ \__ __/  |/  / _ \| |/_/  
 / ___/ // / /|_/ / ___/>  <    
/_/   \_, /_/  /_/_/  /_/|_|    
     /___/                      
     '''

tytul = Style.BRIGHT + Fore.CYAN + tytul_ascii + Style.RESET_ALL
## tytul_opis = Style.DIM + Fore.BLUE + tytul_opis_tekst + Style.RESET_ALL

tytul_info = Style.NORMAL + Fore.CYAN + tytul_ascii_mini + Style.RESET_ALL

opis_info_tekst = "The python YouTube to MP3 / MP4 converter."
opis_info = Style.NORMAL + Fore.BLUE + opis_info_tekst + Style.RESET_ALL

# Tekst ostrzeżeniowy
uwaga_plen = (
    "UWAGA! Właściciel programu nie odpowiada za ewentualne szkody "
    "oraz problemy w przyszłości. "
    "\n──────────────────────────────────────────────────────────────"
    "\nWARNING! The owner of the program is not responsible for any "
    "damage or problems in the future."
)

uwaga = Style.BRIGHT + Fore.RED + uwaga_plen + Style.RESET_ALL

wybor_zamk_tekst = (
    "Jeśli się pomyliłeś to możesz zamknąć program w dowolnym momencie. Nawet przy "
    "konwertowaniu. (Nie w trakcie tylko gdy jest pole tekstowe)"
    "\n──────────────────────────────────────────────────────────────"
    "\nIf you make a mistake you can close the program at any time. Even when "
    "you're converting. (Not during only when there is a text box)"
)

pow_dt_zamk = Style.BRIGHT + Fore.LIGHTYELLOW_EX + wybor_zamk_tekst + Style.RESET_ALL

wybr_en_tekst = "Selected English Language."
wybr_en = Style.BRIGHT + Fore.GREEN + wybr_en_tekst + Style.RESET_ALL

wybr_en_MP3_tekst = "Selected MP3 format."
wybr_en_MP3 = Style.BRIGHT + Fore.GREEN + wybr_en_MP3_tekst + Style.RESET_ALL

wybr_en_MP4_tekst = "Selected MP4 format."
wybr_en_MP4 = Style.BRIGHT + Fore.GREEN + wybr_en_MP4_tekst + Style.RESET_ALL


wybr_pl_tekst = "Wybrano Język Polski."
wybr_pl = Style.BRIGHT + Fore.GREEN + wybr_pl_tekst + Style.RESET_ALL

wybr_pl_MP3_tekst = "Wybrano format MP3."
wybr_pl_MP3 = Style.BRIGHT + Fore.GREEN + wybr_pl_MP3_tekst + Style.RESET_ALL

wybr_pl_MP4_tekst = "Wybrano format MP4."
wybr_pl_MP4 = Style.BRIGHT + Fore.GREEN + wybr_pl_MP4_tekst + Style.RESET_ALL

# Powitanie i wybór języka (EN lub PL)
print(tytul)
print("    ")
print(uwaga)
print("    ")
print(pow_dt_zamk)
time.sleep(5)
print("    ")
print("    ")
print("Witaj! / Welcome!")
print("────────────────────")

# ~~ ~~ ~~ ~~ ~~ ~~ ~~ KOD ŹRÓDŁOWY ~~ ~~ ~~ ~~ ~~ ~~ ~~


def is_valid_filename(name):
    # Sprawdzanie, czy nazwa pliku zawiera nieprawidłowe znaki
    return not re.search(r'[<>:"/\\|*?]', name)

def sanitize_filename(name):
    # Usuwanie nieprawidłowych znaków z nazwy pliku
    return re.sub(r'[<>:"/\\|*?]', '', name)

def paczki_pl():
    print("    ")
    print("Wykorzystane paczki i biblioteki do programu:")
    print(
                    
        "PyTube (pytube.io)"
        "\ntartley / Colorama"  
        "\n    "
        "\nBiblioteki Python:"
        "\nsys, os, time, re"
                      
         )
    time.sleep(3)
  # continue

def licencja_programu_pl():
    print("    ")
    print(
        "Licencja Creative Commons - Uznanie autorstwa"
        "\n --- (Licencja zostanie dodana niedługo) --- "
                      
         )
    time.sleep(3)
  # continue

def paczki_en():
    print("    ")
    print(
        "Used packages and libraries for the program:"
        "\nPyTube (pytube.io)"
        "\ntartley / Colorama"
        "\n    "
        "\nPython libraries:"
        "\nsys, os, time, re"
                      
         )
    time.sleep(3)
  # continue

def licencja_programu_en():
    print("    ")
    print(
        "Creative Commons License - Attribution"
        "\n --- (License will be added soon) --- "
                      
         )
    time.sleep(3)
  # continue




def main():
    while True:
        # Proszę wybrać język (EN lub PL)
        print(
            "Proszę o wybranie języka (PL lub EN), albo napisz END, by zakończyć program."
            "\nPlease select a language (PL or EN), or type END to exit the program."
            "\n    "
            "\nJeśli oczekujesz lub potrzebujesz informacji o programie, jego wykorzystanych paczkach, licencji i tym podobne. Napisz INFO iPL."
            "\nIf you expect or need information about the program, its used packages, licenses and the like. Type iEN."
            )
        
        wybor_jezyka = input("[PL / EN] || [END] || [iPL / iEN] >> ").lower()

        if wybor_jezyka in ["en", "eng", "english"]:
            kod_en()
            break  # Wyjście z pętli po poprawnym wyborze

        elif wybor_jezyka in ["pl", "pol", "polski"]:
            kod_pl()
            break  # Wyjście z pętli po poprawnym wyborze

        elif wybor_jezyka in ['end', ' end', 'end ']:
            print("    ")
            print("Zamykam program. Dziękuję za użycie!")
            time.sleep(2)
            sys.exit(0)
        
        elif wybor_jezyka in ['ipl', ' ipl', 'ipl ']:
                for i in range(80):
                    print("    ")
                print(tytul_info)
                print(opis_info)
                time.sleep(0.5)
                print("Stworzone z <3 przez maksiqa_")
                time.sleep(1.35)
                print(
                "    "
                "\nProgram został stworzony tylko w celach pobierania muzyki"
                " lub materiałów wideo tylko dla DJ'i lub dla użytku domowego. "
                "\nNie legalne jest pobieranie treści powyżej i rozpowrzechnianie tego w internecie, kopiowania materiałów w rzeczywistości itp. "
                )
                time.sleep(3)
                print(
                "    "
                "\nWłaściciel programu (maksiq_) nie odpowiada za ewentualne szkody lub problemy prawne związane z artykułem 116 Ustawy o prawie autorskim i prawach pokrewnych" 
                "\ndot. Rozpowszechnianie cudzego utworu bez uprawnienia."
                "\n(Kto bez uprawnienia albo wbrew jego warunkom rozpowszechnia cudzy utwór w wersji oryginalnej albo w postaci opracowania, "
                "artystyczne wykonanie, "
                "fonogram, wideogram lub nadanie, podlega grzywnie, "
                "\nkarze ograniczenia wolności albo pozbawienia wolności do lat 2.)"
                    )

                time.sleep(6)
                
                while True:    
                    print("    ")
                    print("Jeśli chciałbyś się czegoś więcej dowiedzieć napisz LIC po licencje, PACK po użyte paczki.")
                    wybor_info_opcji = input("[LIC / PACK] >> ").lower()
           
                    if wybor_info_opcji == 'lic':
                        licencja_programu_pl()
                        continue

                    elif wybor_info_opcji == 'pack':
                        paczki_pl()
                        continue

                    else:
                        print("    ")
                        print("Nieznane polecenie.")
                        time.sleep(2)
                        print("Wpisz LIC po informacje o licencji lub PACK po wykorzystane paczki do produkcji programu.")
                        time.sleep(1)
                        print("    ")
                        print("Albo napisz END by zakończyć program lub PASS by przejść dalej do pobierania. (Wyborem języka będzie poprzednio wpisane INFO PL lub INFO EN)")
                        blad_wybor_opcji_info = input("[END / PASS] >> ").lower()

                        if blad_wybor_opcji_info == 'end':
                            print("    ")
                            print("Program został zamknięty. Dziękuję za użycie!")
                            time.sleep(1)
                            sys.exit(0)

                        elif blad_wybor_opcji_info == 'pass':
                            print("    ")
                            print("Dobra. Za chwilę zostaniesz przeniesiony do pobierania.")
                            time.sleep(1)
                            kod_pl()

                        else:
                            print("    ")
                            print("Nieznane polecenie.")
                            time.sleep(2)
                            print("W takim razie zostaniesz przeniesiony do pobierania.")
                            time.sleep(2)
                            for i in range(40):
                                print("    ")
                            kod_pl()

        elif wybor_jezyka in ['ien', ' ien', 'ien ']:
                for i in range(80):
                    print("    ")
                print(tytul_info)
                print(opis_info)
                time.sleep(0.5)
                print("Made with <3 by maksiq_")
                time.sleep(1.35)
                print(
                "    "
                "\nThe program was created only for the purpose of downloading music"
                " or video content only for DJs or for home use. It is not legal to download "
                "\nthe content above and distribute it on the Internet, copy the material in fact, etc. "
                )
                time.sleep(3)
                print(
                "    "
                "\nThe owner of the program (maksiq_) shall not be liable for any damages or legal problems related to Article 116 of the Polish law on Copyright and Related Rights " 
                "\nregarding Dissemination of another's work without authorization. "
                "\n(transl. Whoever, without authorization or contrary to its terms, disseminates another's work in the original version or in the form of a development, "
                "artistic performance, phonogram, videogram or broadcast, "
                "\nshall be subject to a fine, restriction of freedom or imprisonment for up to 2 years.)"
                    )

                time.sleep(6)
                
                while True:    
                    print("    ")
                    print("If you would like to learn more write LIC for licenses, PACK for used packages.")
                    wybor_info_opcji = input("[LIC / PACK] >> ").lower()
           
                    if wybor_info_opcji == 'lic':
                        licencja_programu_en()
                        continue

                    elif wybor_info_opcji == 'pack':
                        paczki_en()
                        continue

                    else:
                        print("    ")
                        print("Unknown command.")
                        time.sleep(2)
                        print("Enter LIC for license information or PACK for used packages.")
                        time.sleep(1)
                        print("    ")
                        print("Or type END to end the program or PASS to continue with the download. (The language selection will be the previously typed INFO EN).")
                        blad_wybor_opcji_info = input("[END / PASS] >> ").lower()

                        if blad_wybor_opcji_info == 'end':
                            print("    ")
                            print("The program is now closed. Thank you for using it!")
                            time.sleep(1)
                            sys.exit(0)

                        elif blad_wybor_opcji_info == 'pass':
                            print("    ")
                            print("Right. You will be transferred to the download in a moment.")
                            time.sleep(1)
                            kod_pl()

                        else:
                            print("    ")
                            print("Unknown command.")
                            time.sleep(2)
                            print("In that case, you will be moved to download.")
                            time.sleep(2)
                            for i in range(40):
                                print("    ")
                            kod_en()

        else:
            print("    ")
            print(f"Nieznany język {wybor_jezyka}. Proszę wybrać EN lub PL.")
            print(f"Unknown language {wybor_jezyka}. Please select EN or PL.")
            time.sleep(2)
            print("──────────────────────────────────────────────────────")
            print("    ")



# def download_cda_video(url, destination):
#    try:
#        video_url = url  # Użyj bezpośredniego linku do filmu z iframe
#
#        # Opcjonalnie, możesz również wydobyć nazwę filmu z linku (np. 57476126c)
#        video_id = url.split('/')[-1]
#
#        video_title = f"video_{video_id}.mp4"  # Możesz dostosować nazwę pliku
#
#        video_file = os.path.join(destination, video_title)
#
#        with requests.get(video_url, stream=True) as r:
#            r.raise_for_status()
#            with open(video_file, 'wb') as f:
#                for chunk in r.iter_content(chunk_size=8192):
#                    f.write(chunk)
#
#        return video_title
#    except Exception as e:
#        print(f"Błąd podczas pobierania pliku: {str(e)}")
#        return None

def kod_pl():
        print("    ")
        print(wybr_pl)
        while True:
            print(
                "Wybierz rozszerzenie zapisania pobranego pliku (MP3 lub MP4):"
                  
                  
                  )
            wybor_formatu = input(">> ").lower()

            if wybor_formatu in ['mp3', ' mp3', 'mp3 ']:
                kod_pl_mp3()

            elif wybor_formatu in ['mp4', ' mp4', 'mp4 ']:
                kod_pl_mp4()
                
def kod_pl_mp3():
    while True:
        print("────────────────────────────────────────────────")
        print("Wprowadź prawidłowy link filmu YouTube, który chcesz pobrać: ")
        url = input(">> ")

        if url.lower() == 'end':
            print("    ")
            print("Zamykam program. Dziękuję za użycie!")
            time.sleep(2)
            break

        try:
            yt = YouTube(url)
        except Exception as e:
            print("    ")
            print("Błędny link.")
            time.sleep(2)
            print("    ")
            continue

        print("    ")
        print("Proszę czekać...")

        # Wykorzystaj tylko audio // POL
        video = yt.streams.filter(only_audio=True).first()

        # Sprawdź po ścieżkę zapisania pliku // POL
        dst = input(
            "    "
            "\nWybierz ścieżkę zapisania pliku "
            "(puste jeśli ścieżka ma być w tym miejscu): "
            "\n>> ") or '.'

        if dst.lower() == 'end':
            print("    ")
            print("Zamykam program. Dziękuje za użycie!")
            time.sleep(2)
            break

        destination = dst

        # Pobierz ten plik // POL
        out_file = video.download(output_path=destination)

        # Zapisz ten plik (kryteria) // POL
        base, ext = os.path.splitext(out_file)
        new_file_name = f"{yt.title} (Autor - {yt.author}).mp3"
        new_file_name = sanitize_filename(new_file_name)  # Zdezyfekowanie nazwy

        if sanitize_filename(new_file_name):
            time.sleep(0.3)
            print("    ")
            print("Potencjalne znaki specjalne z nazwy pliku zostały usunięte.")
            time.sleep(1)

        new_file = os.path.join(destination, new_file_name)
        os.rename(out_file, new_file)

        # Rezultat pobrania // POL
        print("    ")
        print(f"Plik audio {yt.title} (Autor: {yt.author}) został pomyślnie pobrany.")
            
                    # Autor // POL
        print("────────────────────────────────────────────────")
        print("Stworzone z <3 przez maksiqa_")
        print("    ")

        time.sleep(2.5)
        # Zamknięcie programu przez naciśnięcie klawisza // POL
        print(
        "Napisz END, aby zamknąć program"
        ", RPT aby rozpocząć ponownie program, albo MP4 by powtórzyć działanie programu i pobrać plik wideo .")

        while True:
            koniec = input("[END / RPT / MP4] >> ")

            if koniec.lower() == 'end':
                print("    ")
                print("Program został zamknięty. Dziękuję za użycie!")
                time.sleep(1)
                sys.exit(0)

            elif koniec.lower() == 'rpt':
                print("    ")
                print("Dobrze, za chwilę program uruchomi się ponownie.")
                time.sleep(2)
                for i in range(70):
                    print("    ")
                break

            elif koniec.lower() == 'mp4':
                print("Dobrze, za chwilę przeniosę ciebie do pobierana pliku MP4.")
                time.sleep(2)
                for i in range(70):
                    print("    ")
                kod_pl_mp4()

            else:
                print("    ")
                print("Błąd.")
                time.sleep(1.4)
                print("Napisz END, aby zakończyć program, RPT, by powtórzyć działanie programu lub MP4 by ponowić program i pobrać plik wideo.")
                time.sleep(1)
                continue
            
def kod_pl_mp4():
    print("    ")
    print(wybr_pl_MP4)
    while True:
        ## KOD WYŁĄCZONY Z UŻYCIA (Może w następnej aktualizacji)
        # print("Wybierz usługę z której zostanie pobrany plik wideo: ")
        # while True:    
        #    usluga_mp4 = input("[CDA / YT] >> ").lower()
        #
        print("────────────────────────────────────────────────")
        print("Wprowadź prawidłowy link filmu YouTube, który chcesz pobrać: ")
        url = input(">> ")

        if url.lower() == 'end':
            print("    ")
            print("Zamykam program. Dziękuję za użycie!")
            time.sleep(2)
            break

        try:
            yt = YouTube(url)
        except Exception as e:
            print("    ")
            print("Błędny link.")
            time.sleep(2)
            print("    ")
            continue

        print("    ")
        print("Proszę czekać...")

        # Wykorzystaj tylko audio // POL
        video = yt.streams.filter(only_video=True, file_extension="mp4").order_by("resolution").desc().first()

        if video:
            # Ograniczenie do 1080p
            max_resolution = video.resolution
            if "4320p" in max_resolution or "2160p" in max_resolution:
                max_resolution = "1080p"
            video = yt.streams.filter(only_video=True, resolution=max_resolution, file_extension="mp4").first()

        # Sprawdź po ścieżkę zapisania pliku // POL
        dst = input(
        "    "
        "\nWybierz ścieżkę zapisania pliku "
        "(puste jeśli ścieżka ma być w tym miejscu): "
        "\n>> ") or '.'

        if dst.lower() == 'end':
            print("    ")
            print("Zamykam program. Dziękuje za użycie!")
            time.sleep(2)
            break

        destination = dst

        # Pobierz ten plik // POL
        out_file = video.download(output_path=destination)

        # Zapisz ten plik (kryteria) // POL
        base, ext = os.path.splitext(out_file)
        new_file_name = f"{yt.title} (Autor - {yt.author}).mp4"
        new_file_name = sanitize_filename(new_file_name)  # Zdezyfekowanie nazwy

        if sanitize_filename(new_file_name):
            time.sleep(0.3)
            print("    ")
            print("Potencjalne znaki specjalne z nazwy pliku zostały usunięte.")
            time.sleep(1)

        new_file = os.path.join(destination, new_file_name)
        os.rename(out_file, new_file)

        # Rezultat pobrania // POL
        print("    ")
        print(f"Plik wideo {yt.title} (Autor: {yt.author}) został pomyślnie pobrany.")
    
        # Autor // POL
        print("────────────────────────────────────────────────")
        print("Stworzone z <3 przez maksiqa_")
        print("    ")

        time.sleep(2.5)
        # Zamknięcie programu przez naciśnięcie klawisza // PL
        print(
        "Napisz END, aby zamknąć program"
        ", RPT aby rozpocząć ponownie program, albo MP3 by powtórzyć działanie programu i pobrać plik audio .")

        while True:
            koniec = input("[END / RPT / MP3] >> ")

            if koniec.lower() == 'end':
                print("    ")
                print("Program został zamknięty. Dziękuję za użycie!")
                time.sleep(1)
                sys.exit(0)

            elif koniec.lower() == 'rpt':
                print("    ")
                print("Dobrze, za chwilę program uruchomi się ponownie.")
                time.sleep(2)
                for i in range(70):
                    print("    ")
                break

            elif koniec.lower() == 'mp3':
                print("Dobrze, za chwilę przeniosę ciebie do pobierana pliku MP3.")
                time.sleep(2)
                for i in range(70):
                    print("    ")
                kod_pl_mp3()

            else:
                print("    ")
                print("Błąd.")
                time.sleep(1.4)
                print("Napisz END, aby zakończyć program, RPT, by powtórzyć działanie programu lub MP3 by ponowić program i pobrać plik audio.")
                time.sleep(1)
                continue
    
       ### KOD WYŁĄCZONY Z UŻYCIA
       ## Kod na pobieranie treści z cda został wyłączony, ponieważ nie działa. Może zmieni się to w następnej aktualizacji
       # elif usluga_mp4 == 'cda':
       #     while True:
       #         print("────────────────────────────────────────────────")
       #         print("Wprowadź prawidłowy link filmu na cda.pl, który chcesz pobrać: ")
       #         url = input(">> ")
       #
       #         if url.lower() == 'end':
       #             print("    ")
       #             print("Zamykam program. Dziękuję za użycie!")
       #             time.sleep(2)
       #             break
       #
       #         print("    ")
       #         print("Proszę czekać...")
       #
       #         # Sprawdź po ścieżkę zapisania pliku
       #         dst = input(
       #             "    "
       #             "\nWybierz ścieżkę zapisania pliku "
       #             "(puste jeśli ścieżka ma być w tym miejscu): "
       #             "\n>> ") or '.'
       #
       #         if dst.lower() == 'end':
       #             print("    ")
       #             print("Zamykam program. Dziękuje za użycie!")
       #             time.sleep(2)
       #             break
       #
       #         destination = dst
       #
       #        # Pobierz ten plik
       #         video_title = download_cda_video(url, destination)
       #
       #                
       #
       #         if video_title is not None:
       #             print("    ")
       #             print(f"Plik wideo {video_title} został pomyślnie pobrany.")
       #             print("────────────────────────────────────────────────")
       #             print("Stworzone z <3 przez maksiqa_")
       #             print("    ")
       #         else:
       #             print("    ")
       #             print("Błąd podczas pobierania pliku.")
       #             time.sleep(2)
       #             print("    ")
       #             print("Program zostanie zamknięty.")
       #             time.sleep(1)
       #             sys.exit(0)
       #
       #         time.sleep(2.5)
       #
       #         print(
       #             "Napisz END, aby zamknąć program"
       #             ", RPT aby rozpocząć ponownie program, albo MP3 by powtórzyć działanie programu i pobrać plik audio."
       #                 )
       #
       #         while True:
       #             koniec = input("[END / RPT / MP3] >> ")
       #
       #             if koniec.lower() == 'end':
       #                         print("    ")
       #                         print("Program został zamknięty. Dziękuję za użycie!")
       #                         time.sleep(1)
       #                         sys.exit(0)
       #
       #             elif koniec.lower() == 'rpt':
       #                 print("    ")
       #                 print("Dobrze, za chwilę program uruchomi się ponownie.")
       #                 time.sleep(2)
       #                 for i in range(70):
       #                     print("    ")
       #                 break
       #
       #             elif koniec.lower() == 'mp3':
       #                 print("Dobrze, za chwilę przeniosę ciebie do pobierana pliku MP3.")
       #                 time.sleep(2)
       #                 for i in range(70):
       #                     print("    ")
       #                 kod_pl_mp3()
       #
       #             else:
       #                 print("    ")
       #                 print("Błąd.")
       #                 time.sleep(1.4)
       #                 print(
       #             "Napisz END, aby zakończyć program, RPT, by powtórzyć działanie programu lub MP3 lub MP4 by ponowić program i pobrać plik audio lub wideo."
       #                     )
       #                 time.sleep(1)
       #                 continue
       # 
       # else:
       #    print("    ")
       #    print("Błąd.")
       #    time.sleep(1.4)
       #    print(
       # "Wybierz usługę pomiędzy CDA.PL a YouTube."
       #        )
       #    time.sleep(1)
       #    continue
        



def kod_en():
    try:
        print("    ")
        print(wybr_en)

        while True:
            print("────────────────────────────────────────────────"
                  "\nEnter the valid link of the video you want to download: ")

            url = input(">> ")

            if url.lower() == 'end':
                print("    ")
                print("Exiting the program. Thank you for using it!")
                time.sleep(2)
                break

            try:
                yt = YouTube(url)
            except Exception as e:
                print("    ")
                print("Incorrect link.")
                time.sleep(2)
                print("    ")
                continue

            print("    ")
            print("Please wait...")

            # Wykorzystaj tylko audio // ENG
            video = yt.streams.filter(only_audio=True).first()

            # Sprawdź po ścieżkę zapisania pliku // ENG
            dst = input(
                "    "
                "\nEnter the destination "
                "(leave it blank if you want the file to be saved in this location): "
                "\n>> ") or '.'

            if dst.lower() == 'end':
                print("    ")
                print("Exiting the program. Thank you for using it!")
                time.sleep(2)
                break

            destination = dst

            # Pobierz ten plik // ENG
            out_file = video.download(output_path=destination)

            # Zapisz ten plik (kryteria) // ENG
            base, ext = os.path.splitext(out_file)
            new_file_name = f"{yt.title} (Author - {yt.author}).mp3"
            new_file_name = sanitize_filename(new_file_name)  # Zdezyfekowanie nazwy

            if sanitize_filename(new_file_name):
                time.sleep(0.3)
                print("    ")
                print("Potential special characters from the file name have been removed.")
                time.sleep(1)

            new_file = os.path.join(destination, new_file_name)
            os.rename(out_file, new_file)

            # Rezultat pobrania // ENG
            print("    ")
            print(f"Audio file {yt.title} (Author: {yt.author}) has been successfully downloaded.")

            # Autor // ENG
            print("────────────────────────────────────────────────")
            print("Made with <3 by maksiq_")
            print("    ")

            time.sleep(2.5)
            # Zamknięcie programu przez naciśnięcie klawisza // ENG
            print("Type END to close or RPT to restart the program.")

            while True:
                koniec = input("[END / RPT] >> ")

                if koniec.lower() == 'end':
                    print("    ")
                    print("The program has been closed. Thank you for using it!")
                    time.sleep(1)
                    sys.exit(0)

                elif koniec.lower() == 'rpt':
                    print("    ")
                    print("Okay, the program will restart.")
                    time.sleep(2)
                    for i in range(40):
                        print("    ")
                    break

                else:
                    print("    ")
                    print("Error.")
                    time.sleep(1.4)
                    print("Type END or RPT to repeat the program's action.")
                    time.sleep(1)
                    continue

    except FileExistsError:
        print(
            "    "
            "\nA file with the same name in this selected location already exists. (It was assigned with the extension .mp4)"
        )
        time.sleep(1)
        print("The program will now exit.")
        time.sleep(2)
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        time.sleep(1)
        print("The program will now exit.")
        time.sleep(2)
        sys.exit(0)

if __name__ == "__main__":
    main()



# =-=-=-=-=-=-=-= PYYTMP3 ZOSTAŁ STWORZONY PRZEZ maksiqa_, maksiczqa_, Maksymiliana B. =-=-=-=-=-=-=-=