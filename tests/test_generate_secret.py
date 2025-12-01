import pytest
import string
from ..generate_secret import generate_secret

def test_default_length():
    """Test that the default length is 32."""
    assert len(generate_secret()) == 32

@pytest.mark.parametrize("length", [1, 8, 16, 64, 128])
def test_custom_length(length):
    """Test generating secrets with various custom lengths."""
    assert len(generate_secret(length)) == length

def test_default_characters():
    """Test that default characters are alphanumeric (letters + digits)."""
    # Generate a large sample to ensure we check the pool effectively
    secret = generate_secret(500)
    allowed_chars = string.ascii_letters + string.digits
    
    # Check that all characters are in the allowed set
    assert all(c in allowed_chars for c in secret)

def test_symbols_included():
    """Test that symbols are included when requested."""
    secret = generate_secret(500, symbols=True)
    allowed_chars = string.ascii_letters + string.digits + string.punctuation
    
    # Check validity of characters
    assert all(c in allowed_chars for c in secret)
    
    # Check that at least one symbol is present (probabilistic, but highly likely for n=500)
    # If this flakes, the length can be increased or the check removed.
    assert any(c in string.punctuation for c in secret)

def test_uppercase_flag():
    """Test the uppercase flag behavior."""
    # The current implementation adds uppercase letters to the pool.
    # Since the default pool already has uppercase, this just changes probability weights,
    # but we verify the output is still valid.
    secret = generate_secret(500, uppercase=True)
    allowed_chars = string.ascii_letters + string.digits
    
    assert all(c in allowed_chars for c in secret)

def test_return_type():
    """Test that the function returns a string."""
    assert isinstance(generate_secret(), str)

@pytest.mark.parametrize("kwargs, expected_pool_subset", [
    ({}, string.ascii_letters + string.digits),
    ({"symbols": True}, string.punctuation),
])
def test_character_pool_content(kwargs, expected_pool_subset):
    """
    Check that the generated secret contains characters from the expected pool subsets.
    This is a probabilistic test.
    """
    secret = generate_secret(1000, **kwargs)
    # We expect at least some overlap with the specific subset we enabled/expected
    assert any(c in expected_pool_subset for c in secret)
