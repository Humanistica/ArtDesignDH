import csv


header = """
# Corpus

Vous trouverez ici les corpus collectés lors de la phase préliminaire du \
Workshop "Fabriquer des jeux de données en art"\n\n\n
"""


with open('./fabriquer_des_jeux_de_donnees_en_art.csv') as f, \
        open('./corpus_list.md', 'w') as md:

    reader = csv.DictReader(f)

    # Writer md's header
    md.write(header)

    # Write corpus list
    for row in csv.DictReader(f):
        link = '### [{titre}]({link})\n'.format(titre=row['Titre'],
                                                link=row['lien de téléchargement'])
        author = 'Auteur : {}\n\n'.format(row['Auteur'])
        date = 'Creation : {}\n\n'.format(row['Date'])
        desc = 'Description : {}\n\n'.format(row['Description'])

        md.write(link)
        md.write(author)
        md.write(date)
        md.write(desc)
        md.write('\n\n---\n\n')
