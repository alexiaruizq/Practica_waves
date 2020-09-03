import sys

sys.path.insert(1,"dsp-modulo")

from thinkdsp import SinSignal
from thinkdsp import decorate

from thinkdsp import read_wave
from thinkdsp import play_wave

import matplotlib.pyplot as plt

seno = SinSignal(freq=440, amp=1.0, offset=0)
segundo_seno = SinSignal(freq=340, amp=1, offset=0)
tercer_seno = SinSignal(freq=600, amp=0.7, offset=0)


wave_seno = seno.make_wave(duration=1.0, start=1, framerate=44100)
wave_segundo_seno = segundo_seno.make_wave(duration=1.0, start=2, framerate=44100)
wave_tercer_seno =  tercer_seno.make_wave(duration=1.0, start=3, framerate=44100)


resultante = wave_seno + wave_segundo_seno + wave_tercer_seno


decorate(xLabel="Tiempo (s)")
decorate(yLabel="Amplitud")

resultante.plot()

resultante.write("Sonido.wav")

plt.show()