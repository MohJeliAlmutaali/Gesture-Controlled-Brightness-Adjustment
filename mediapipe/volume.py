import pulsectl

def set_volume(volume):
    with pulsectl.Pulse('set-volume-example') as pulse:
        for sink in pulse.sink_list():
            pulse.volume_set_all_chans(sink, volume)

# Contoh penggunaan: atur volume menjadi 50% dari maksimum
set_volume(0.2)  # Volume dalam rentang 0.0 hingga 1.0
