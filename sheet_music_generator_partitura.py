import partitura as pt

my_xml_file = pt.EXAMPLE_MUSICXML

score = pt.load_score(my_xml_file)

part = score.parts[0]
print(part.pretty())

# qué es musescore?????

pt.render(part, fmt='png', out='C:/Users/bpart/Desktop/sheet_music_generator/part.png')
