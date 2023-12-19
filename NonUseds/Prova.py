IngType = {
    "SPOON" : 'yemek kaşığı ',
    "CUPS" : 'çay bardağı ',
    "PIECE" : 'adet ',
    "KG" : 'kg '
}
         
ContentLI = ItemsLI.text
if IngType.SPOON in ContentLI:
    DictForExtract[ContentLI.split(IngType.SPOON)[1]] = ContentLI.split(IngType.SPOON)[0]
elif IngType.CUPS in ContentLI:
    DictForExtract[ContentLI.split(IngType.CUPS)[1]] = ContentLI.split(IngType.CUPS)[0]
elif IngType.PIECE in ContentLI:
    DictForExtract[ContentLI.split(IngType.PIECE)[1]] = ContentLI.split(IngType.PIECE)[0]
elif IngType.KG in ContentLI:
    DictForExtract[ContentLI.split(IngType.KG)[1]] = ContentLI.split(IngType.KG)[0]
else:
    DictForExtract[ContentLI] = True