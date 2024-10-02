import pickle

def view_pickle_file(file_path):
    """Read and return the contents of a pickle file."""
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data

def view_text_file(file_path):
    """Read and return the contents of a text file."""
    with open(file_path, 'r') as file:
        return file.read()

def print_file_contents():
    """Print the contents of both pickle and text files."""
    # File paths (update the paths as needed)
    compressed_lz77_file = 'data/compressed_lz77.pkl'
    compressed_lzw_file = 'data/compressed_lzw.pkl'
    decompressed_shannon_fano_file = 'data/decompressed_shannon_fano.txt'
    decompressed_lz77_file = 'data/decompressed_lz77.txt'
    decompressed_lzw_file = 'data/decompressed_lzw.txt'
    input_file = 'data/input.txt'

    # Read and print .pkl files
    print("\nThe contents of compressed_lz77_file:")
    lz77_data = view_pickle_file(compressed_lz77_file)
    print(lz77_data)
    print()

    print("The contents of compressed_lzw_file:")
    lzw_data = view_pickle_file(compressed_lzw_file)
    print(lzw_data)
    print()

    # Read and print text files
    print(f"The contents of decompressed_shannon_fano_file:")
    print(view_text_file(decompressed_shannon_fano_file))
    print()

    print(f"The contents of decompressed_lz77_file:")
    print(view_text_file(decompressed_lz77_file))
    print()

    print(f"The contents of decompressed_lzw_file:")
    print(view_text_file(decompressed_lzw_file))
    print()

    print(f"The contents of input_file:")
    print(view_text_file(input_file))
