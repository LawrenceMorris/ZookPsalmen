
from sacrebleu.metrics import CHRF

# Create metric instance; ignore letter case
chrf = CHRF(lowercase=True)

base_text = input ("Enter the 'idea' translation, e.g. the base or reference text: ")
references = [[base_text]]


done = 'y'
while done != 'n':
    system_output = input ('Enter text to check here: ')

    # Compute score
    score = chrf.corpus_score([system_output], references)
    print(score)  # chrF2 = XX.X
