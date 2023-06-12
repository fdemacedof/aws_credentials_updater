## AWS Credentials Updater

This script updates the AWS credentials file with session credentials obtained by providing an MFA token. It allows you to specify the MFA device serial number and the AWS profile name.

### Prerequisites

- AWS CLI installed and configured with profiles
- Python 3.x installed

### Usage

1. For the first use, you need to specify the MFA device serial number and AWS profile name as command-line arguments:

```bash
python update_aws_credentials.py --serial-number <MFA_DEVICE_SERIAL_NUMBER> --profile <AWS_PROFILE_NAME>
```

2. Enter your six-digit MFA token when prompted.

3. The script will obtain session credentials using the provided MFA token and update the AWS credentials file (`~/.aws/credentials`) with the new credentials.

4. Subsequent uses of the script will automatically use the stored parameters from the `settings.ini` file. If the parameters are not provided, an error message will be displayed.

### Notes

- The `settings.ini` file stores the MFA device serial number and AWS profile name for future use. It is created automatically after the first successful run of the script.

- If you want to update the stored parameters, you can delete the `settings.ini` file and provide the parameters as command-line arguments again.

- Make sure you have the necessary permissions and privileges to update the AWS credentials file.

- To use the script for the first time, please provide the `--serial-number` and `--profile` arguments as shown in Step 1 of the usage instructions.

---

## Atualizador de Credenciais AWS

Este script atualiza o arquivo de credenciais da AWS com as credenciais de sessão obtidas ao fornecer um token MFA. Ele permite que você especifique o número de série do dispositivo MFA e o nome do perfil da AWS.

### Pré-requisitos

- AWS CLI instalado e configurado com perfis
- Python 3.x instalado

### Uso

1. Para a primeira utilização, você precisa especificar o número de série do dispositivo MFA e o nome do perfil da AWS como argumentos de linha de comando:

```bash
python update_aws_credentials.py --serial-number <NUMERO_DE_SERIE_MFA> --profile <NOME_PERFIL_AWS>
```

2. Insira o seu token MFA de seis dígitos quando solicitado.

3. O script irá obter as credenciais de sessão usando o token MFA fornecido e atualizar o arquivo de credenciais da AWS (`~/.aws/credentials`) com as novas credenciais.

4. Nas utilizações posteriores do script, ele automaticamente usará os parâmetros armazenados no arquivo `settings.ini`. Se os parâmetros não forem fornecidos, uma mensagem de erro será exibida.

### Notas

- O arquivo `settings.ini` armazena o número de série do dispositivo MFA e o nome do perfil da AWS para uso futuro. Ele é criado automaticamente após a primeira execução bem-sucedida do script.

- Se você deseja atualizar os parâmetros armazenados, você pode excluir o arquivo `settings.ini` e fornecer os parâmetros novamente como argumentos de linha de comando.

- Certifique-se de ter as permissões e privilégios necessários para atualizar o arquivo de credenciais da AWS.

- Para utilizar o script pela primeira vez, por favor, forneça os argumentos `--serial-number` e `--profile` como mostrado no Passo 1 das instruções de uso.
