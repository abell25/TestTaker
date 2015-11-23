#TestTaker

## Summary

NLP class project for answering multiple choice questions using IR and NLP techniques.

## Techniques

### IR system
  
Lucene is used to generate indexes over wikipedia/wikibooks/CK12 open-source text books.  This allows relevent documents to be searched for by relavent keywords.

### NLP system

#### Statistical techniques

Simple statistical measure is to use work closeness between each answer's terms and the questions term's in the most relevent documents they share.

Various statistical methods of this type would output features that a classifier could be trained on.  The model would learn what statistical measures are most important then.

