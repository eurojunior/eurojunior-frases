# Frases diárias — @dr.eurojunior

Post estático diário no Instagram do @dr.eurojunior, às **08:00 (America/Sao_Paulo)**, todos os dias, incluindo fim de semana. Publicação **sem aprovação prévia do Euro**: ele revisa no perfil e volta para ajustar quando quiser.

## Visual (não mudar sem pedido do Euro)
- Card estilo Threads, 1080×1350, fundo `#101010`, texto `#F3F5F7`, Roboto (pasta `fonts/`).
- Avatar (`avatar.png`), "dr.eurojunior", selo azul de verificado, "now" em cinza, frase, ícones (curtir, comentar, repost, enviar).
- Gerado por `python3 render.py lotes/<AAAA-MM-DD>` a partir de `lotes/<data>/posts.json`.

## Conteúdo
- Público: donos de escritório de advocacia. Voz: direta, provocativa, inspiradora — gestão, precificação, cliente ideal, time, processos, vendas, disciplina, crescimento (Método EURO / Manual do Advogado Empreendedor).
- Frase da arte: 1 a 2 frases, até ~110 caracteres, em português do Brasil, sem hashtags.
- Legenda: 2 parágrafos curtos desenvolvendo a ideia + linha final fixa:
  `É advogado e fatura mais de 30 mil por mês? Minha dica: clica no link da bio!👀`
- Nunca repetir frase já usada: ler todos os `lotes/*/posts.json` antes de escrever.
- Sem números de faturamento inventados, sem promessas de resultado, sem citar clientes, pessoas reais ou concorrentes.

## `posts.json`
Lista na ordem dos dias, começando na data do nome da pasta:
`[{"quote": "...", "caption": "<2 parágrafos, sem a linha de CTA>"}]`

## Publicação (Supermetrics `manage_social_media`)
- ds_id `IGI`, account_id `17841404174004174`, content_type `IMAGE`.
- media_url fixado no commit: `https://raw.githubusercontent.com/eurojunior/eurojunior-frases/<sha>/lotes/<data>/post_NN.jpg`.
- caption = legenda + `\n\n` + CTA; alt_text = frase; publish_at `AAAA-MM-DDT08:00`, timezone `America/Sao_Paulo`.
- Antes de agendar, listar os já agendados (`status`, sem alvo) e só preencher os dias vazios.

## Histórico
- 2026-11-13: projeto criado; lote 2026-11-14 (14 posts, 14/11 a 27/11).
- 2026-11-18: lote 2026-11-28 (5 posts, 28/11 a 02/12), agendados sem aprovação (scheduled_id 19345–19349).
