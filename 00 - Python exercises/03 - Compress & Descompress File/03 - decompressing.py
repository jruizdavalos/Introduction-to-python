import zlib, base64

open
data= open('compressed.txt','r').read()
data_bytes= bytes(data,'utf-8')


descompressed_data= zlib.decompress(base64.b64decode(data_bytes))

print(descompressed_data)