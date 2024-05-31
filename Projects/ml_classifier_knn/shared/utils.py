import os
import shutil

def setup_save_directory(save_dir):
  if os.path.exists(save_dir):
      shutil.rmtree(save_dir)
  os.makedirs(save_dir, exist_ok=True)


def create_log_file(name):
    return open(name, "w")
