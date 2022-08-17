from datetime import datetime

# Reddit markdown is used in this string
comment_reply = f"\n\n\n\n*Bu yorum (bir bot tarafından) otomatik olarak bırakıldı." \
                f" Bunu doğru anlamadıysam, bana kızmayın, hala öğreniyorum!*\n\n" \
                f"[^(listeden çık)](https://np.reddit.com/r/VikipediBot/comments/wpslrb/listeden_%C3%A7%C4%B1kma_ba%C5%9Fl%C4%B1%C4%9F%C4%B1/)" \
                f" ^(|) [^r/VikipediBot" \
                f" ^(|) [^(GitHub)](https://github.com/muhammedaksam/VikipediBot)"


def few_meanings_reply(text):
    return f'Bu kelime/ifadenin({text.strip()}) birkaç farklı anlamı vardır.'


def festivity_reply():
    now = datetime.now()
    if datetime.date(now) == datetime(now.year, 12, 25).date():
        return "\n\nMutlu Noeller! <3"
    elif datetime.date(now) == datetime(now.year, 12, 31).date():
        return "\n\nMutlu bir Yılbaşı Gecesi dilerim, Redditor!"
    elif datetime.date(now) == datetime(now.year, 1, 1).date():
        return "\n\nMutlu yıllar, Redditor!"

    return ""
