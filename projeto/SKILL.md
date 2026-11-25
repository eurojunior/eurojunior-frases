---
name: frases-diarias-eurojunior
description: Escreve, renderiza e agenda os posts diários de frases do Instagram @dr.eurojunior (card estilo Threads, 08:00 America/Sao_Paulo). Use quando alguém pedir para criar frases do Euro, preencher a agenda de posts do @dr.eurojunior, rodar a rotina de frases diárias ou revisar uma frase/legenda no padrão do Euro.
---

# Frases diárias — @dr.eurojunior

Você mantém os posts diários de frases do Instagram @dr.eurojunior (Euro, CEO do Grupo Euro, mentor de advogados donos de escritório). Meta: todos os dias de amanhã até hoje+14 com **1 post agendado às 08:00 (America/Sao_Paulo)**. O Euro autorizou publicar sem aprovação prévia; ele revisa no perfil e pede ajustes. Escreva tudo em português do Brasil.

**Fonte da verdade:** o `CLAUDE.md` do repositório `eurojunior/eurojunior-frases`. Se algo neste arquivo divergir dele, vale o `CLAUDE.md`.

## Pré-requisitos de quem roda
- Acesso de escrita (push) ao repositório GitHub `eurojunior/eurojunior-frases` e o GitHub conectado no Claude.
- Conector Supermetrics conectado, com acesso à conta do Instagram `17841404174004174` (ds_id `IGI`).
- Ambiente com shell e Python (Cowork ou Claude Code). Num Projeto do claude.ai sem shell, dá para **escrever e revisar** frases, mas não renderizar nem agendar.

## Regras de conteúdo: A ARTE EMOCIONA, A LEGENDA ENSINA
- **Arte (a frase no card):** fé, prosperidade, humildade, gratidão, superação ou parceria. NUNCA gestão, processos, CNPJ, delegação, marketing, escala, funil, margem. Nunca acusa nem corrige o leitor ("não é empresa", "não existe", "acaba perdendo"). Sem clichê de coach (zona de conforto, universo conspira).
- 8 a 25 palavras + CTA de envio opcional, com imagem concreta ou contraste (barco/porto, porta baixa, Davi/Golias, pão na mesa, dia bonito x dia insuportável). Leitor como herói, ou Euro vulnerável **só como sentimento** ("eu sonhava…", "eu pedi a Deus…"). Nunca invente fatos da vida do Euro.
- Use `\n\n` na quote para separar frases em parágrafos e antes do CTA de envio.
- **Padrões** (alternar, respeitando a proporção): 1 BOTAFÉ ACREDITA 35% ("Envie pra si mesmo se acredita.") · 2 BOTAFÉ HUMILDE 30% · 3 PRECIFICAÇÃO VALORIZADORA 20% (valoriza o esforço do leitor, nunca critica leitor nem cliente) · 4 JUNTOS 15% ("Manda pra quem está/esteve com você…").
- **Legenda, 5 a 10 linhas (parágrafos) contando a linha fixa:** eco emocional → ponte para a dor do escritório (aqui entra a lição de gestão, sem acusar) → repete o CTA de envio se houver → linha final fixa:
  `Se você é advogado, fatura mais de 30 mil por mês e quer traçar um plano de escala com meu time, comenta DIAGNÓSTICO aqui embaixo 👇`
- Sem hashtags. CTA "clica no link da bio" PROIBIDO. Sem números de faturamento inventados, sem promessas de resultado, sem citar clientes, pessoas reais ou concorrentes.
- Nunca repita ideia nem estrutura: leia todos os `lotes/*/posts.json` (inclusive `lotes/_descartado-*`) e as campeãs antes de escrever.

As campeãs, as ruins e o porquê das regras estão no `CLAUDE.md` (seções "Por que estas regras existem", "Campeãs", "Ruins"). Leia-as sempre.

## Passo a passo
1. **Repositório:** conecte/clone `eurojunior/eurojunior-frases` (no Cowork: `add_repo` com owner `eurojunior`, repo `eurojunior-frases`, access `push`) e leia o `CLAUDE.md`. NÃO altere `render.py` nem o visual (layout aprovado pelo Euro).
2. **Agenda atual:** Supermetrics `manage_social_media` action `status`, sem alvo, `account_id` `17841404174004174`, `state` `scheduled`, `limit` 50. Liste os dias entre amanhã e hoje+14 sem post às 08:00 (publish_at_local 08:00-03:00). Ignore carrosséis/vídeos em outros horários: são de outra rotina. Se não faltar nenhum dia, encerre dizendo que está tudo em dia.
   - Outras pessoas (e a tarefa agendada do Euro) também rodam esta rotina. **Sempre liste a agenda imediatamente antes de agendar** e nunca agende um dia que já tenha post às 08:00.
3. **Ganchos:** se o `CLAUDE.md` apontar um banco de ganchos, adapte só o osso/estrutura e registre conta + frase original em `origem`. Sem banco, `"origem": "criada do zero"`.
4. **Escrever:** crie `lotes/<data-do-primeiro-dia-novo>/posts.json`, lista na ordem dos dias:
   `[{"padrao": 1-4, "origem": "...", "quote": "...", "caption": "<legenda SEM a linha final fixa>"}]`
   Autocheck de cada post: padrão declarado e distribuição respeitada; arte sem jargão nem acusação; 8–25 palavras + CTA; legenda 5–10 linhas contando a linha fixa; ideia e estrutura inéditas.
5. **Renderizar:** `pip install --break-system-packages pillow` se preciso; `python3 render.py lotes/<data>`. O script falha se algo sair da safe area. Abra pelo menos 3 imagens (inclua a de frase mais longa) e confira texto e enquadramento.
6. **Commit e push** para `main` (`git -c push.negotiate=true push`). Guarde o SHA do commit.
7. **Agendar** cada post com `manage_social_media` action `publish`: `ds_id` `IGI`, `account_id` `17841404174004174`, `content_type` `IMAGE`, `media_url` `https://raw.githubusercontent.com/eurojunior/eurojunior-frases/<SHA>/lotes/<data>/post_NN.jpg`, `caption` = caption + `\n\n` + linha final fixa, `alt_text` = frase sem quebras de linha, `publish_at` `AAAA-MM-DDT08:00`, `timezone` `America/Sao_Paulo`. Confira com `status` que ficaram agendados.
8. **Aprovação/erros:** se vier `approval_required`, não contorne: envie os links de aprovação exatamente como vieram, com a data de cada post, e lembre que o nível "sem aprovação" se ajusta em https://hub.supermetrics.com/write-settings?platform=IGI&team_id=1132191 . Erro de permissão/reconexão: repasse o link de reconexão.
9. **Histórico:** acrescente uma linha na seção Histórico do `CLAUDE.md` (data, lote, dias, padrões, scheduled_ids e quem rodou), commit/push, e termine com um resumo curto: dias agendados, frase de cada dia com o padrão, pendências.

## Ajustes pedidos pelo Euro
- Trocar frase/legenda de um post já agendado: edite o `posts.json`, renderize, commit/push e use `update_post` (scheduled_id, caption/alt_text) — ou `cancel_scheduled` + novo `publish` se a imagem mudou (o media_url é fixado no SHA).
- Mudanças de regra, visual ou layout só com pedido do Euro; registre no `CLAUDE.md`.
