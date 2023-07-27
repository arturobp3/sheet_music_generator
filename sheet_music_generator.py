import sys
import librosa

import audio_to_midi as am


print("Starting...")

y, sr = librosa.load('River-flows-in-you.wav', sr=None)

print("Audio file loaded!")

midi = am.wave_to_midi(y, sr=sr)

print("Conversion finished!")

with open ('river-flows-in-you.mid', 'wb') as f:
    midi.writeFile(f)

print("Done. Exiting!")