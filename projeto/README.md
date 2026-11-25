# Kit de compartilhamento — Frases diárias @dr.eurojunior

Duas formas de a equipe usar a rotina:

## 1. Skill (rodar a rotina inteira no Cowork ou no Claude Code)
- Arquivo: `SKILL.md`. Cada colaborador salva como skill (se a organização permitir) ou o admin publica para a organização.
- Cada pessoa precisa de: push no repositório `eurojunior/eurojunior-frases` (convite de colaborador no GitHub), GitHub conectado no Claude, e conector Supermetrics com acesso à conta do Instagram do @dr.eurojunior.
- Peça: "roda a rotina de frases diárias do @dr.eurojunior".

## 2. Projeto do claude.ai (escrever e revisar frases)
1. Crie um Projeto, por exemplo "Frases diárias @dr.eurojunior".
2. Cole o conteúdo de `INSTRUCOES-DO-PROJETO.md` em "Instruções do projeto".
3. Suba os 3 arquivos de `conhecimento/` como conhecimento do projeto.
4. Compartilhe o Projeto com a organização.

## Manter atualizado
Os arquivos de `conhecimento/` são uma foto do repositório. Depois de cada lote novo, rode
`python3 projeto/gerar_conhecimento.py` e substitua os arquivos no Projeto.
A fonte da verdade continua sendo o `CLAUDE.md` da raiz.

## Cuidado com agendamento em dobro
A tarefa agendada do Euro roda todo dia e também preenche a agenda. Quem rodar a rotina manualmente deve listar a agenda do Supermetrics logo antes de agendar e só preencher dias vazios.
