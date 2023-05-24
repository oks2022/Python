# Python
Compare the calculated checksum with the provided checksum.

    For MD5: Compare the calculated MD5 checksum with the provided MD5 checksum. They should be exactly the same, consisting of 32 characters.
    For SHA1: Compare the calculated SHA1 checksum with the provided SHA1 checksum. They should be exactly the same, consisting of 40 characters.
    The code will convert both the calculated checksum and the provided checksum to lowercase using the lower() method. This ensures a case-insensitive comparison.
    #!/usr/bin/env python3 This line specifies the interpreter to use when executing the script (in this case, Python 3). It ensures that the script can be executed directly from the command line without explicitly invoking the Python interpreter.
chmod +x checksum_script.py  This command grants execute permissions to the file.
export PATH=$PATH:$(pwd)
This command adds the current directory to the PATH temporarily for the current session. If you want to make it permanent, you can add this line to your shell profile file (e.g., ~/.bashrc for Bash).
