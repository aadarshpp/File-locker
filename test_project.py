import pytest
import tempfile
import os

from project import encrypt_file, decrypt_file, clone_file

@pytest.fixture
def test_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, "test_file.txt")
        with open(file_path, "w") as f:
            f.write("The code is 4455")
        password = "password@2255.com"
        yield file_path, password  # returning tuple

def test_clone_file(test_file):
    file_path, _ = test_file  # unpacking
    clone_filename = clone_file(file_path)
    clone_filepath = os.path.join(os.path.dirname(file_path), clone_filename)

    assert os.path.exists(clone_filepath)
    with open(clone_filepath, "rb") as f1, open(file_path, "rb") as f2:
        assert f1.read() == f2.read()

def test_encrypt_file(test_file):
    file_path, password = test_file
    original_dir = os.path.dirname(file_path)

    # Clone the original file
    clone_filename = clone_file(file_path)
    clone_filepath = os.path.join(original_dir, clone_filename)

    # Encrypt the clone
    encrypt_file(clone_filepath, password)
    encrypted_path = f"{clone_filepath}.locked"

    # Assertions
    assert os.path.exists(encrypted_path)

    with open(encrypted_path, "rb") as f_enc, open(file_path, "rb") as f_original:
        assert f_enc.read() != f_original.read()  # Encrypted content should differ

    # Cleanup
    if os.path.exists(encrypted_path):
        os.remove(encrypted_path)
    if os.path.exists(clone_filepath):
        os.remove(clone_filepath)

def test_decrypt_file(test_file):
    file_path, password = test_file
    original_dir = os.path.dirname(file_path)

    # Clone the original file
    clone_filename = clone_file(file_path)
    clone_filepath = os.path.join(original_dir, clone_filename)

    # Encrypt the clone
    encrypt_file(clone_filepath, password)
    encrypted_path = f"{clone_filepath}.locked"

    # Decrypt the encrypted clone
    decrypt_file(encrypted_path, password)
    decrypted_path = clone_filepath  # It should revert to original name

    assert os.path.exists(decrypted_path)

    with open(decrypted_path, "rb") as f_dec, open(file_path, "rb") as f_original:
        assert f_dec.read() == f_original.read()

    # Cleanup
    if os.path.exists(decrypted_path):
        os.remove(decrypted_path)
