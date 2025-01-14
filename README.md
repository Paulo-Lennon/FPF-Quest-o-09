# FPF-Quest-o-09

Documentação para Configuração e Execução dos Testes
Os passos a seguir detalham os pré-requisitos, a configuração necessária, e o processo de execução dos testes automatizados para verificar o comportamento do aplicativo "Triângulo" disponível em http://www.vanilton.net/triangulo/.
________________________________________
1. Pré-requisitos
Certifique-se de que seu ambiente de desenvolvimento está configurado com as seguintes ferramentas e dependências:
1.1. Ferramentas Necessárias
•	Python 3.x: Linguagem de programação para implementar os testes.
•	Selenium WebDriver: Biblioteca para automação de navegadores.
•	PyTest: Framework de teste unitário para execução e organização dos casos de teste.
•	Navegador e WebDriver Compatível:
o	Por exemplo, Google Chrome e ChromeDriver. Ambos usados nesse projeto.
1.2. Instalar Dependências
Execute o seguinte comando para instalar as bibliotecas necessárias:
pip install selenium pytest

1.3. Configurar o WebDriver
Baixe o WebDriver adequado para o navegador que será usado nos testes. Abaixo estão os links para os principais navegadores:
•	ChromeDriver
•	GeckoDriver (Firefox)
•	EdgeDriver
Após o download, coloque o executável em um diretório que esteja no PATH do sistema operacional ou forneça o caminho completo no script.
________________________________________
2. Implementação do Código
Crie um arquivo chamado test_triangulo.py com o seguinte conteúdo: Usar código disponível no folder “Codigo” 

3. Execução dos Testes
3.1. Executar os Testes
No terminal, navegue até o diretório onde o arquivo test_triangulo.py está salvo e execute o seguinte comando:
bash
Copiar código
pytest test_triangulo.py
3.2. Interpretação dos Resultados
•	Caso todos os testes passem, a saída será similar a:
diff
Copiar código
======== test session starts ========
collected 5 items

test_triangulo.py .....                             [100%]

======== 5 passed in 2.34s ========
•	Se algum teste falhar, o terminal exibirá detalhes sobre o erro.
