from textblob import TextBlob

article = 'After his defeat at the Battle of Waterloo, instead of remaining in the field with his shattered army, ' \
          'Napoleon returned to Paris in the hope of retaining political support for his position as Emperor of the ' \
          'French. He hoped, with his political base secured, to then be able to continue the war. It was not to be; ' \
          'instead the members of the two chambers created a Provisional Government and demanded that Napoleon ' \
          'abdicate. Napoleon toyed with the idea of a coup d''état similar to Eighteenth of Brumaire but decided ' \
          'against it. On 25 June Napoleon left Paris for the final time and after staying at the Palace of Malmaison, ' \
          'left for the coast hoping to reach the United States of America. In the meantime, the Provisional Government' \
          ' deposed his son and tried to negotiate a conditional surrender with the Coalition powers. They failed to' \
          ' obtain any significant concessions from the Coalition who insisted on a military surrender and the ' \
          'restoration of Louis XVIII. Napoleon, realising he could not hope to evade the Royal Navy, surrendered to ' \
          'Captain Maitland upon placing himself under his protection on board HMS Bellerophon. The British Government' \
          ' refused to allow Napoleon to set foot in England and arranged for his exile to the remote South Atlantic ' \
          'island of Saint Helena where he died in 1821.'

summary = TextBlob(article).noun_phrases
summary = list(dict.fromkeys(summary))

print('This article is about:')
for noun in summary:
    print(f'- {noun}')

