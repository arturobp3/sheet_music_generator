import sys
import librosa
import music_neural_network as mnn


print("Starting...")

print("Audio file loaded!")

# crear ruta de salida antes de ejecutar esta funcion
mnn.get_midi_from_audio(input_path='River-flows-in-you.wav', output_path='river-flows-mnn')

model, midi, notes = mnn.predict('River-flows-in-you.wav')

import music21
parsed = music21.converter.parse('river-flows-mnn/River-flows-in-you_basic_pitch.mid')
parsed.show('musicxml.png')

print("Conversion finished!")