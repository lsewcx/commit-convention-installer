import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from src import github

def test_create_cz_config_js():
    assert github.create_cz_config_js() == None

def test_write_commitlint_config():
    assert github.write_commitlint_config() == None

if __name__=='__main__':
    test_create_cz_config_js()
    test_write_commitlint_config()