import argparse
import itertools
import string
# Gerekli kütüphaneleri tanımladık.

# Wordlist oluşturulması gerekli fonksiyon işlemlerini gerçekleştiriyoruz.
def generate_wordlist(chars, min_length, max_length, output_file):
    with open(output_file, 'w') as f:
        for length in range(min_length, max_length+1):
            for word in itertools.product(chars, repeat=length):
                f.write(''.join(word) + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fenrir Wordlist Generator") # Başlık ekliyoruz.
    parser.add_argument("-c", "--characters", type=str, default=string.ascii_letters + string.digits,
                        help="Wordlist karakterleri (varsayılan: tüm harf ve rakamlar)") # harfler ve rakamları tanımlatıyoruz.
    parser.add_argument("-min", "--min_length", type=int, default=4, help="Minimum karakter uzunluğu") # Dosya içerisindeki karakterin en az miktarını belirtiyoruz.
    parser.add_argument("-max", "--max_length", type=int, default=8, help="Maksimum karakter uzunluğu") # Dosya içerisindeki karakterlerin fazlalığını belirtiyoruz.
    parser.add_argument("-o", "--output_file", type=str, default="wordlist.txt", help="Çıktı dosya adı") # Kaydedilecek dosya adını belirtiyoruz.
    parser.add_argument("Kullanım Örneği: python3 wordlist_generator.py -c abc123 -min 3 -max 5 -o custom_wordlist.txt") # Kullanım örneğini belirtiyoruz.
    
    args = parser.parse_args() # parametreyi bastırıyoruz.
    
    generate_wordlist(args.characters, args.min_length, args.max_length, args.output_file) # Dosya oluşturma işlemini başlatıp işlem sürecini bitiriyoruz.
    
    print(f"[+] Wordlist oluşturuldu ve {args.output_file} dosyasına kaydedildi.") # Süreç bittiğinde bize bilgi vermesi amacıyla bir çıktı yolluyoruz.
