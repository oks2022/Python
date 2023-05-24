#!/usr/bin/env python3
import hashlib

def calculate_checksum(file_path, algorithm):
    hash_object = hashlib.new(algorithm)
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            hash_object.update(chunk)
    return hash_object.hexdigest()

def compare_checksums(file_path, provided_checksum, algorithm='md5'):
    calculated_checksum = calculate_checksum(file_path, algorithm)
    if calculated_checksum.lower() == provided_checksum.lower():
        print("Checksums match! The file is valid.")
    else:
        print("Checksums do not match. The file may be altered or corrupted.")

# Prompt the user to input the file path, provided checksum, and algorithm
file_path = input("Enter the file path: ")
provided_checksum = input("Enter the provided checksum: ")
algorithm = input("Enter the algorithm (default is 'md5'): ") or 'md5'

compare_checksums(file_path, provided_checksum, algorithm)

