from bs4 import BeautifulSoup
import requests

url = "http://minecraft-server-list.cz/"
diablo = "https://diablo.gamefan.cz/diablo-3/postavy/"

while True:
    hledac = input("CO CHCEŠ NAJÍT?\nA = 11 nejpopulárnějších CZ/SK MC serverů\nB = postavy v Diablu 3\nQ = Ukončit: ").upper()
    if hledac == "A":
        doc = BeautifulSoup(requests.get(url).text, "html.parser")
        section = doc.section
        post = section.find_all("div", class_="post")
        for i in range(11):
            dalsi_post = post[i].find("div", class_="post-inner")
            header = dalsi_post.find("header")
            nazev_serveru = header.find("h2")
            verze = header.find("p").find("a")
            if i <= 0:
                print(f"CZ/SK MC SERVERY:\n• {nazev_serveru.string}")
            elif i == 10:
                print(f"• {nazev_serveru.string}\n")
            elif i < 10 and i > 0:
                print(f"• {nazev_serveru.string}")
    elif hledac == "B":
        doc = BeautifulSoup(requests.get(diablo).text, "html.parser")
        nadrizeny = doc.ul
        postavy = nadrizeny.find_all("li")
        for postava in postavy:
            if postava == postavy[0]:
                print(f"POSTAVY Z DIABLA 3:\n• {postava.string}")
            elif postava == postavy[-1]:
                print(f"• {postava.string}\n")
            else:
                print(f"• {postava.string}")
    elif hledac == "Q":
        exit()
    else:
        print("WHAT?\n")
