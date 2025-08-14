#!/usr/bin/env python3
import os

env_path = os.environ.get('VIRTUAL_ENV', 'не найдено')
print(f"Your current virtual env is {env_path}")