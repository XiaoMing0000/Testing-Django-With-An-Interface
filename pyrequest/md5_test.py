import hashlib

md5 = hashlib.md5()
sign_str = '@admin'
sign_byte_utf8 = sign_str.encode(encoding='utf-8')
md5.update(sign_byte_utf8)
sign_md5 = md5.hexdigest()
print(sign_md5)
