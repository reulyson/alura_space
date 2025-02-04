# Alura Space

Projeto desenvolvido durante o curso **"Django: templates e boas práticas"** da Alura. O Alura Space é uma aplicação web que exibe informações sobre a Nebulosa Carina, com funcionalidades como uma barra de busca e uma seção para as imagens mais acessadas.

---

## 🚀 **Funcionalidades**

- **Página inicial**: Exibe a Nebulosa Carina e um texto informativo.
- **Barra de busca**: Permite pesquisar por imagens ou conteúdos específicos.
- **Mais vistas**: Exibe as imagens mais acessadas pelos usuários.
- **Próximas funcionalidades**:
  - Aba "Novas": Exibirá as imagens mais recentes adicionadas ao site.
  - Aba "Surpreenda-me": Mostrará uma imagem aleatória.

---

## 🛠️ **Tecnologias Utilizadas**

- **Django**: Framework web Python para desenvolvimento rápido e seguro.
- **HTML/CSS**: Para a estruturação e estilização das páginas.
- **Templates Django**: Para reutilização de código e organização do projeto.

---

## 📂 **Estrutura do Projeto**

```
alura-space/
├── galeria/
│   ├── migrations/
│   ├── templates/
│   │   ├── galeria/
│   │   │   ├── partials/
│   │   │   │   ├── _footer.html
│   │   │   │   ├── _header.html
│   │   │   ├── base.html
│   │   │   ├── index.html
│   │   │   ├── imagem.html
│   ├── static/
│   │   ├── styles/
│   │   │   ├── style.css
│   │   ├── images/
│   ├── views.py
│   ├── urls.py
│   ├── models.py
├── setup/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py
├── requirements.txt
├── .env
├── .gitignore
```

---

## ⚙️ **Como Executar o Projeto**

### **Pré-requisitos**
- Python 3.x instalado.
- Pip (gerenciador de pacotes do Python).

### **Passos para Configuração**

1. **Clonar o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/alura-space.git
   cd alura-space
   ```

2. **Criar e ativar o ambiente virtual**:
   - No macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - No Windows:
     ```bash
     python -m venv venv
     venv\Scripts\Activate
     ```

3. **Instalar dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variáveis de ambiente**:
   - Crie um arquivo `.env` na raiz do projeto e adicione a `SECRET_KEY` do Django:
     ```
     SECRET_KEY=sua_chave_secreta_aqui
     ```

5. **Aplicar migrações**:
   ```bash
   python manage.py migrate
   ```

6. **Executar o servidor**:
   ```bash
   python manage.py runserver
   ```

7. **Acessar a aplicação**:
   Abra o navegador e acesse:
   ```
   http://127.0.0.1:8000/
   ```

---

## 📝 **Boas Práticas Aplicadas**

- **DRY (Don't Repeat Yourself)**: Reutilização de código com templates e partials.
- **Separação de preocupações**: Uso de views, templates e arquivos estáticos de forma organizada.
- **Segurança**: Uso de variáveis de ambiente para proteger informações sensíveis.
- **Modularização**: Criação de apps específicos para funcionalidades distintas.

---

## 📸 **Capturas de Tela**

### Página Inicial
![Página Inicial](https://github.com/user-attachments/assets/affeb372-f94e-4922-a469-33223734433a)

### Página de Imagem
![Página de Imagem](https://github.com/user-attachments/assets/fb3a0f53-c982-459f-bbbb-c6f9824c1a6a)


---

## 📚 **Aprendizados do Curso**

- Configuração de ambientes virtuais com `venv`.
- Criação de projetos e apps no Django.
- Uso de templates e partials para organizar o código HTML.
- Integração de arquivos estáticos (CSS, imagens) no Django.
- Boas práticas de desenvolvimento, como o princípio DRY.

---

## 📄 **Licença**

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🙌 **Agradecimentos**

Agradeço à Alura pelo curso incrível e à comunidade Django por fornecer uma ferramenta tão poderosa para desenvolvimento web.

---

## 📧 **Contato**

Se tiver dúvidas ou sugestões, sinta-se à vontade para entrar em contato:

- **Email**: reulyson@gmail.com
- **GitHub**: [Reulyson Wanzeler](https://github.com/reulyson)
