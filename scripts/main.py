
from load_audio import load_audio
from feature_extraction import extract_features
from display import display_features

# Load the audio file
music, sr = load_audio('data/testAudio.mp3', offset=81, duration=10)

# Extract features
features = extract_features(music, sr)

#Display features
display_features(features)
