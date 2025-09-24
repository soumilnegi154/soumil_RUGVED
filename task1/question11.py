def liau(sentence):
    sum=0
    words=sentence.split()
    for i in words[:100]:
        sum+=len(i)
    senlen=sentence.index(words[99])+len(words[99])+1
    L=sum
    print(L)
    S=sentence[:senlen].count(".")
    print(S)
    CLI=0.0588*L-0.296*S-15.8
    return CLI

print(liau("Existing computer programs that measure readability are based largely upon " \
     "subroutines which estimate number of syllables, usually by counting vowels. T" \
     "he shortcoming in estimating syllables is that it necessitates keypunching the " \
     "prose into the computer. There is no need to estimate syllables since word length "
     "in letters is a better predictor of readability than word length in syllables. Therefore, " \
     "a new readability formula was computed that has for its predictors letters per 100 words and " \
     "sentences per 100 words. Both predictors can be counted by an optical scanning device, and thus the " \
     "formula makes it economically feasible for an organization such as the U.S. Office of Education to " \
     "calibrate the readability of all textbooks for the public school system."))