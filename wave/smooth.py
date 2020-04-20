import wave

wave_fd =  wave.open("mix.wav", "r")
(nchannels, sampwidth, framerate, nframes, comptype, compname) = wave_fd.getparams()
samples = wave_fd.readframes(nframes)
print(len(samples))
print(samples[0])
smooth_begin = [ i * 0.01 for i in list(range(50))]
print(len(smooth_begin))
#samples = samples *
