# SanskritMark

A specification guideline for using the benifits of Sanskrit tools available at http://sanskrit.inria.fr.

The guideline is important to maintain uniformity.

#####Transliteration - SLP1



# Noun form generator

## Suggested format

```
noun.gender.case.vacana
```

where

'gender' takes 'm' for musculine, 'f' for feminine, 'n' for neuter and 'a' for any gender.

'case' takes '1' for nominative, '2' for accusative, '3' for instrumental, '4' for dative, '5' for ablative, '6' for genitive, '7' for locative and '0' for sambodhana.

'vacana' takes '1' for ekavacana, '2' for dvivacana and '3' for bahuvacana respectively.

e.g. `Davala.m.1.1` signifies that the noun 'Davala' has to be declined with musculine, nominative ekavacana i.e. DavalaH

# Verb form generator

## Suggested format

```
verb.gana.pada.lakara.vacya.purusa.vacana
```

where

'gana' takes '1' to '10' where they are usual gaNas in pANini's grammar. Use '0' for secondary verbs.

'pada' takes 'p'/'a' for parasmaipada and Atmanepada respectively.

'lakara' takes 'law'/'laN'/'viliN'/'low'/'lfw'/'lfN'/'luw'/'liw'/'luN'/'aluN'/'AliN'. viliN stands for viDiliN. aluN stands for AgamAbhAvayuktaluN, AliN stands for ASIrliN. All others have their usual notations in pANini's grammar.

'vacya' takes 't' / 'm' for kartari and karmaNi respectively.

'purusa' takes 'p'/'m'/'u' for prathama, madhyama, uttama respectively.

'vacana' takes '1'/'2'/'3' for ekavacana, dvivacana and bahuvacana respectively.

e.g. `BU.1.p.low.t.1.1` signifies that the verb 'BU' has to be declined with 1st gana, parasmaipada, low lakara, kartari vacya, prathama purusa, ekavacana e.g. aBUt
