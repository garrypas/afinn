from afinn import Afinn
from builtins import str
afinn = Afinn()
score = afinn.score('this site is not very good')
print(score)
