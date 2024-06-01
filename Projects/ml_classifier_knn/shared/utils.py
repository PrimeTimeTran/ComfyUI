import os
import shutil
import logging
import keras

def setup_save_directory(save_dir):
  if os.path.exists(save_dir):
      shutil.rmtree(save_dir)
  os.makedirs(save_dir, exist_ok=True)

class CustomLoggerCallback(keras.callbacks.Callback):
    def __init__(self, logger):
        super().__init__()
        self.logger = logger

    def on_epoch_end(self, epoch, logs=None):
        if logs:
            self.logger.info("Epoch %d - loss: %.4f - accuracy: %.4f", epoch, logs['loss'], logs['accuracy'])

def create_log_file(name):
  logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
  file_handler = logging.FileHandler(name)
  file_handler.setLevel(logging.INFO)

  formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
  file_handler.setFormatter(formatter)
  logger = logging.getLogger()
  logger.addHandler(file_handler)

  console_handler = logging.StreamHandler()
  console_handler.setLevel(logging.INFO)
  console_handler.setFormatter(formatter)
  logger.addHandler(console_handler)

  return [file_handler,logger]
