import json

# Clave en una sola línea continua, sin espacios ni \n internos
pk_body = ("MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDIoGobzZ6wo9U9"
"Ts/Iqr5x47BcaT8nzpPmnamDu+ZEx3tlXkitcWAQoPJht7B+r4EkfXe+QyCRKkLH"
"VVy0d8e8aXEp4gZkYZi2hzF8tYRntMjiLhEQTgC0oRPPLY3BDzG6RTPHcegqcN8R"
"mI6UDPECt0c9Xo9ftHDIDqouf9/tm9ncTcOuTKu8H3OThJv6u2KAoNkkkSUYHjW1"
"uJOQUp4+tUQgxZLRgdk5SXKjfB58tmEdQo6uctJ1a3ksS3Q9z923m+kb7Y09ti3J"
"0rI3/TwGIeHo9InKqEVqJFiDYwuLuPdErV4/z7jtVKhKVSiNRNsy1Xp8jZ9GOzYT"
"NS7FzhkFAgMBAAECggEAAySgqkS7c/41FL2GSe51FQOTVFraavC7u+MgU63X3INu"
"bL4SHjCb59bJNxiVOeJrOM1ng5BkNtWLmmP2IeZTKVqn+tANhiOfuq9vahhb52Q+"
"8okQ/7QBIyiiMmzicM5ZhXp8LXWq4RNV8YiSX0H1wcGiwAZvf5Wd0Zj7cI3Uo1GS"
"6x2bAeFvv6KxHLBbdhS4IcmvXVs6hhuiUhrybmfG/8LUwSNFHi+pjJ99W2spGBpw"
"DlltX/JLpBLJj+vsyFW9ro45G39uv5KJ65W8yU1UP/wOtfNn9FTeE+bnU2RW64IT"
"OWfoI6WWqBqy+vQ95RuYRkgj0FrHS+93rtex5EqsVwKBgQDmoNgCPQdaVpjeaZ6N"
"8gijSSyQEawW0GAohCxfd4gaMj2Xv5NhWjOuEvnvFRtu/RX3aAn+BnsfO/yeORdV"
"hE0MKYT45rbB6D9uxRVKeWwHaLfJwMh4h/nwty2ustYRnDjTKkumtIf1xv7tlAQE"
"AfKk3tfuCP+Hx5C3krhNj1YCLwKBgQDesqMeQTfV3Bmy+a/wXUoRt74GBP3hfudL"
"Bl+QI5ldZFFsh4hRKBlAF5N9rZT83aV/mw7+mo7RdF0eV/d67a+Vkih516IkTe0O"
"+DEvaXybv5gMYW9l8rrOdfa0GjBInJjg15iPVP4h1gBL4pogF/pA1L0uk8sguOrV"
"zaycZijPCwKBgQDB1Fy3RONxIWbJRqtjUQ/BbDZvvuqLIgYvBybj9WoF2kO5zeDn"
"6Q+WNYypS2wLE9nqXR5IyNmhnqDpucHKta6rkhmXtw/SWIc3aZxDQ1lvwKr2fXf/"
"FQkTLmDOeq8/jbSUhO+f5AqAngaTVdsqIxjzR/bir91TGH6gSkdrqBP5MQKBgD0o"
"dd+DLaBPt8cNByJNnF/NRCRHDqn0vfQ+pdPh0uZw/GN/vRH8nyKY1up21ymyfRbU"
"MIP/UiV3fXMt2UsrJ0M+RltfuqmZtPaddnR81bm4HjuYLo2i4WZ9wuinIIdwahOl"
"YcJLJxeHu8EbVBRoQVO4mNPHxssPvX5F45d3/tENAoGBAMkRmjgyoSxz+m8WYX8T"
"nqZy+Iq6Odl8Jiq8pipDsCo4kcdGFvNpDlypX/HucCv+SSrWv608zIryraO3UzKk6"
"oGg5xsZxrbzxCi4PihHnvn6enlJTJPpdzVqu9rPJPk1a2YLWnfH6czJbbGcOT7vb"
"sOgQUpSC+0Zonu08K4mjGVAR")

# Reconstruimos el formato PEM oficial
full_pk = "-----BEGIN PRIVATE KEY-----\n" + pk_body + "\n-----END PRIVATE KEY-----\n"

data = {
    "type": "service_account",
    "project_id": "loveplay-7b8cc",
    "private_key_id": "403ef718934b81517c03d65339e54f9d4c55e6ac",
    "private_key": full_pk,
    "client_email": "firebase-adminsdk-fbsvc@loveplay-7b8cc.iam.gserviceaccount.com",
    "client_id": "117739387027839464991",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fbsvc%40loveplay-7b8cc.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

with open('firebase-key.json', 'w') as f:
    json.dump(data, f)
print("🎯 Llave generada en formato compacto. ¡A probar!")
