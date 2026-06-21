import pandas as pd
from fuzzy_matching import *


def ouvrir_base() -> pd.DataFrame:
    """Ouvre la base de données de mots français"""
    lexique = pd.read_csv("Lexique4.tsv", sep="\t", encoding="utf-8", low_memory=False)

    return lexique



# Ouverture de la base de données
lexique = ouvrir_base()
print(lexique)

mots = lexique["1_Mot"]


