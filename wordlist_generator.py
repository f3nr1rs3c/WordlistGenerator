import argparse
import itertools
import string

def generate_wordlist(chars, min_length, max_length, output_file):
    with open(output_file, 'w') as f:
        for length in range(min_length, max_length+1):
            for word in itertools.product(chars, repeat=length):
                f.write(''.join(word) + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fenrir Wordlist Generator")
    parser.add_argument("-c", "--characters", type=str, default=string.ascii_letters + string.digits,
                        help="Wordlist karakterleri (varsayılan: tüm harf ve rakamlar)")
    parser.add_argument("-min", "--min_length", type=int, default=4, help="Minimum karakter uzunluğu")
    parser.add_argument("-max", "--max_length", type=int, default=8, help="Maksimum karakter uzunluğu")
    parser.add_argument("-o", "--output_file", type=str, default="wordlist.txt", help="Çıktı dosya adı")
    parser.add_argument("Kullanım Örneği: python3 wordlist_generator.py -c abc123 -min 3 -max 5 -o custom_wordlist.txt")
    
    args = parser.parse_args()
    
    generate_wordlist(args.characters, args.min_length, args.max_length, args.output_file)
    
    print(f"[+] Wordlist oluşturuldu ve {args.output_file} dosyasına kaydedildi.")
