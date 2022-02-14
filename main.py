import argparse
import hashlib


def algorithm_check(algorithm: str) -> bool:
    """
    Args:
        algorithm (str): algorithm name

    Returns:
        bool: True if algorithm is supported, False otherwise

    Examples:
        >>> algorithm_check('sha256')
    """
    if algorithm in hashlib.algorithms_available:
        return True

def file_to_hash(algorithm, file_path: str) -> str:
    """
    Args:
        algorithm (str): algorithm name
        file_path (str): file path
    
    Returns:
        str: hash of file
    
    Examples:
        >>> file_to_hash('sha256', './test.txt')
    """
    with open(file_path, 'rb') as f:
        hash_str = hashlib.new(algorithm, f.read()).hexdigest()
    return hash_str

def compare(hash_1: str, hash_2: str) -> bool:
    """
    Args:
        hash_1 (str): hash of file
        hash_2 (str): hash of file

    Returns:
        bool: True if hashes are the same, False otherwise
    
    Examples:
        >>> compare('a', 'b')
    """

    return hash_1 == hash_2

def main():
    parser = argparse.ArgumentParser(description='Hash file')
    parser.add_argument('--algorithm', help='', type=str, default='sha256')
    parser.add_argument('file_path_1', help='', type=str)
    parser.add_argument('file_path_2', help='', type=str)
    args = parser.parse_args()
    if algorithm_check(args.algorithm):
        hash_1 = file_to_hash(args.algorithm, args.file_path_1)
        hash_2 = file_to_hash(args.algorithm, args.file_path_2)
        if compare(hash_1, hash_2):
            print('Files are the same')
        else:
            print('Files are different')
    else:
        print('Wrong algorithm')


if __name__ == '__main__':
    main()
