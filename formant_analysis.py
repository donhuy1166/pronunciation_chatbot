import parselmouth

def extract_formants(wav_path):
    snd = parselmouth.Sound(wav_path)
    formant = snd.to_formant_burg()
    t = snd.get_total_duration() / 2
    f1 = formant.get_value_at_time(1, t)
    f2 = formant.get_value_at_time(2, t)
    f3 = formant.get_value_at_time(3, t)
    return round(f1), round(f2), round(f3)
