import requests

file = open("file_name.txt","r")
content = file.read()
file.close()
print(content)

file = open("file_name.txt","r")
first_lines = file.readline()
second_lines = file.readline()
file.close()
print(first_lines)
print(second_lines)

url = "https://storage.googleapis.com/dqlab-dataset/hello.txt"
response = requests.get(url)
# Cetak kode status dari response
print(response)
# Cetak isi file hello.txt menggunakan method response.iter_lines()
print("\n>> Cetak isi file hello.txt menggunakan method response.iter_lines():")
for baris in response.iter_lines():
	print(baris)
