from pathlib import Path

INPUT_PATH = Path('./data/raw_images')
PREPROCESSED_PATH = Path('./data/processed_images')
OUTPUT_PATH = Path('./data/outputs')
DEFAULT_OUTPUT_SIGNATURE = 'DEYE_RUN_XX'

DEVICE = 'cpu'
MODELS_PATH = Path('./src/models')
SEGMENTATION_MODEL = 'coverage_segmentator.pt'
BM_REGRESSOR_MODEL = 'BM_regressor.pt'
TARGET_SIZE = (512, 256) # width, height