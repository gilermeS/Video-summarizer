# SumarIA 🤖

Um aplicativo web inteligente que transforma vídeos longos do YouTube em resumos concisos e práticos. Utilizando tecnologias de ponta em IA, o SumarIA transcreve o áudio do vídeo e gera um resumo em bullet points, tornando o consumo de conteúdo mais eficiente.

## 🌟 Sobre

SumarIA é a solução perfeita para quem precisa extrair informações importantes de vídeos do YouTube de forma rápida e eficiente. Combinando o poder do Whisper para transcrição de áudio e o modelo DeepSeek para geração de resumos, o aplicativo oferece uma experiência simplificada para usuários que desejam economizar tempo sem perder conteúdo relevante.

## 🚀 Funcionalidades

- 🎥 Suporte para vídeos e shorts do YouTube
- 🎯 Transcrição precisa usando OpenAI Whisper
- 📝 Resumos concisos em formato de bullet points
- 🌐 Interface web amigável construída com Streamlit
- ⚡ Processamento rápido e eficiente

## 🛠️ Tecnologias Utilizadas

- Python
- Streamlit
- OpenAI Whisper
- DeepSeek Chat
- yt-dlp
- FFmpeg

## 📋 Pré-requisitos

- Python 3.8 ou superior
- FFmpeg instalado no sistema
- Chave de API da OpenRouter (para o DeepSeek)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/sumaria.git
cd sumaria
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
   - Crie um arquivo `.streamlit/secrets.toml`
   - Adicione sua chave da OpenRouter:
     ```toml
     deepseek_key = "sua-chave-aqui"
     ff_path = "caminho-do-ffmpeg"
     ```

## 🎮 Como Usar

1. Inicie o aplicativo:
```bash
streamlit run app.py
```

2. Abra seu navegador em `http://localhost:8501`
3. Cole a URL do vídeo do YouTube
4. Aguarde o processamento
5. Receba a transcrição e o resumo!

## 📝 TODO List

- [ ] Adicionar suporte para mais plataformas de vídeo além do YouTube
- [ ] Implementar cache para evitar reprocessamento de vídeos já analisados
- [ ] Adicionar opção para escolher o idioma do resumo
- [ ] Implementar sistema de feedback para melhorar os resumos
- [ ] Adicionar opção para exportar resumos em diferentes formatos
- [ ] Criar testes automatizados
- [ ] Implementar sistema de autenticação
- [ ] Adicionar análise de sentimento do vídeo
- [ ] Criar uma API REST para o serviço
- [ ] Adicionar suporte para processamento em lote de múltiplos vídeos

## 🤝 Contribuindo

Contribuições são sempre bem-vindas! Sinta-se à vontade para:

1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abrir um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📬 Contato

Guilherme de Souza Ramos Cardoso - guilhermesouza1302@gmail.com

Link do Projeto: [SumarIA](https://github.com/gilermeS/Video-summarizer)
