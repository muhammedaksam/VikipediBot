# Questions with the words that are used in the daily questions like:
# "What's the reason/matter?", "What's up?", "What's the reason/point?" and others
# should be ignored because the bot can't answer the right

# Excluding words for the first pattern
excluding_words1 = {}

# Fuck NLTK, all my homies use self-made adjectives set
adjectives = {}

# Excluding words for the second pattern
excluding_words2 = {}.union(adjectives)

quotes = ('"', "“")

to_replace1 = (" nedir", " ne demektir", " ne demek"," nelerdir", " kimdir", " kim", " kimlerdir", " kimler")
to_replace2 = (" an ", " a ")

link_only = ("anlamına gelebilir", "anlamına da gelebilir", "kastedilmiş olabilir", "kastedilmiş olabilir", "anlamlara gelebilir", "anlamlara da gelebilir")
