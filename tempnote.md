HGG:
len(df) = 220
'2013' = 20
'tcia' = 200
unique numbers 78 string rep.
unique pid 144 (some has more than 1 entry)

Through an inspection, I found that OT tag is the manual segmentation.
The challenge webpage says tcia/2013 denotes the data source: 2013 being data used in brats 2013, tcia being data by NIH data repo.

Training
hdf(HGG): 220 cases, 144 pid
pid >1:
[('pat314', 4),
 ('pat153', 6),
 ('pat417', 2),
 ('pat396', 7),
 ('pat444', 5),
 ('pat399', 10),
 ('pat370', 7),
 ('pat377', 2),
 ('pat171', 8),
 ('pat260', 6),
 ('pat198', 2),
 ('pat290', 5),
 ('pat447', 3),
 ('pat230', 5),
 ('pat374', 8),
 ('pat280', 2),
 ('pat222', 2),
 ('pat226', 2),
 ('pat309', 6),
 ('pat439', 4)]

ldf(LGG): 54 cases, 54 pid
None of pid occurs more than once

Test
tdf(HGG_LGG):110 cases, 53 pid
pid >1:
[('pat352', 2),
 ('pat484', 11),
 ('pat123', 11),
 ('pat500', 21),
 ('pat114', 5),
 ('pat244', 3),
 ('pat456', 5),
 ('pat457', 3),
 ('pat263', 5)]

 pid Overlaps:
 Between Training HGG and LGG
 There are 10 patients who have both HGG and LGG
 Counter({'pat0001': 1,
         'pat0002': 1,
         'pat0004': 1,
         'pat0006': 1,
         'pat0008': 1,
         'pat0011': 1,
         'pat0012': 1,
         'pat0013': 1,
         'pat0014': 1,
         'pat0015': 1})

Between Training and Test
There is no pid overlap.

Labels in OT:
1 for necrosis
2 for edema
3 for non-enhancing tumor
4 for enhancing tumor
0 for everything else

HGG vs LGG
checked the segmentation label sets and it seemed all labels can show up both cases.
from the web search I learned that usual features of HGG vs LGG is that HGG has higher contrast (white around the edges) and have necrosis in the middle, while LGG appears to be dark and fuzzy. 
