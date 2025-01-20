# Limpeza de Arquivos Temporários e Lixeira no Windows  

Este script em Python automatiza a limpeza de arquivos temporários do sistema e do usuário, além de esvaziar a lixeira no Windows. Ele foi projetado para melhorar o desempenho e liberar espaço em disco, facilitando a manutenção do sistema.  

## Funcionalidades  
- **Limpeza da pasta Temp do sistema**: Remove arquivos e pastas temporários localizados em `C:\Windows\Temp`.  
- **Limpeza da pasta Temp do usuário**: Remove arquivos e pastas temporários localizados no perfil do usuário.  
- **Esvaziamento da lixeira**: Limpa a lixeira do Windows sem exibir confirmações.  
- **Execução como administrador**: Garante que o script tenha permissões suficientes para realizar as operações necessárias.  

## Requisitos  
- Python 3.x  
- Sistema operacional Windows  
- Permissões de administrador  

## Como usar  
1. Certifique-se de que o Python está instalado no seu sistema.  
2. Execute o script em um terminal com privilégios administrativos:  
   ```bash  
   python main.py  
