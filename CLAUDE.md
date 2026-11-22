# Frases diárias — @dr.eurojunior

Post estático diário no Instagram do @dr.eurojunior, às **08:00 (America/Sao_Paulo)**, todos os dias, incluindo fim de semana. Publicação **sem aprovação prévia do Euro**: ele revisa no perfil e volta para ajustar quando quiser.

## Visual (não mudar sem pedido do Euro)
- Card estilo Threads, 1080×1350, fundo `#101010`, texto `#F3F5F7`, Roboto (pasta `fonts/`).
- Avatar (`avatar.png`), "dr.eurojunior", selo azul de verificado, "now" em cinza, frase, ícones (curtir, comentar, repost, enviar).
- Gerado por `python3 render.py lotes/<AAAA-MM-DD>` a partir de `lotes/<data>/posts.json`.

## Layout (render.py — não mexer sem pedido do Euro)
- Canvas 1080×1350.
- Tudo que é essencial fica dentro da safe area central 1080×1080 (y 135–1215), porque o Explorar corta para 1:1.
- Nome, texto e ícones na mesma margem esquerda, com o avatar (132 px) à esquerda dessa coluna.
- Entrelinha 1,45; bloco centralizado na vertical.
- Fonte = maior tamanho (até 62 px) em que a frase mais longa do histórico cabe (todas as frases de `lotes/*/posts.json` são medidas, inclusive a altura dos parágrafos), calculada a cada render.
- O script falha se algo sair da safe area.
- Use `\n\n` na quote para separar frases em parágrafos e antes do CTA de envio, como nos posts humanos.

## Conteúdo (regras da rotina diária, atualizadas em 2026-11-22)
- Público: donos de escritório de advocacia. **A ARTE EMOCIONA, A LEGENDA ENSINA.**
- Arte: fé, prosperidade, humildade, gratidão, superação ou parceria — NUNCA gestão, processos, CNPJ, delegação, marketing, escala, funil, margem. Nunca acusa nem corrige o leitor. 8 a 25 palavras + CTA de envio opcional, com imagem concreta ou contraste. Sem hashtags.
- Use `\n\n` na quote para separar frases em parágrafos e antes do CTA de envio (ver seção Layout).
- Padrões (alternar, respeitando a proporção): 1 BOTAFÉ ACREDITA 35% ("Envie pra si mesmo se acredita."), 2 BOTAFÉ HUMILDE 30%, 3 PRECIFICAÇÃO VALORIZADORA 20%, 4 JUNTOS 15% ("Manda pra quem está/esteve com você…").
- Legenda 5 a 10 linhas: eco emocional → ponte para a dor do escritório (a lição de gestão entra aqui) → repete o CTA de envio se houver → linha final fixa:
  `Se você é advogado, fatura mais de 30 mil por mês e quer traçar um plano de escala com meu time, comenta DIAGNÓSTICO aqui embaixo 👇`
- O CTA antigo "clica no link da bio" está PROIBIDO. Os lotes 2026-11-14 e 2026-11-28 são contraexemplos (tom de bronca/aula de gestão na arte); seus agendamentos de 23/11 em diante foram cancelados em 2026-11-22.
- `lotes/_descartado-2026-11-23` NÃO foi publicado (substituído pelo lote 2026-11-23 aprovado pelo Euro), mas suas frases não devem ser reaproveitadas literalmente.
- Nunca repetir ideia nem estrutura: ler todos os `lotes/*/posts.json` antes de escrever. Banco de ganchos: ainda não existe.
- Sem números de faturamento inventados, sem promessas de resultado, sem citar clientes, pessoas reais ou concorrentes.

## `posts.json`
Lista na ordem dos dias, começando na data do nome da pasta:
`[{"padrao": 1-4, "origem": "original"|"<gancho>", "quote": "...", "caption": "<legenda, sem a linha final fixa>"}]`

## Publicação (Supermetrics `manage_social_media`)
- ds_id `IGI`, account_id `17841404174004174`, content_type `IMAGE`.
- media_url fixado no commit: `https://raw.githubusercontent.com/eurojunior/eurojunior-frases/<sha>/lotes/<data>/post_NN.jpg`.
- caption = legenda + `\n\n` + linha final fixa; alt_text = frase; publish_at `AAAA-MM-DDT08:00`, timezone `America/Sao_Paulo`.
- Antes de agendar, listar os já agendados (`status`, sem alvo) e só preencher os dias vazios.

## Histórico
- 2026-11-13: projeto criado; lote 2026-11-14 (14 posts, 14/11 a 27/11).
- 2026-11-18: lote 2026-11-28 (5 posts, 28/11 a 02/12), agendados sem aprovação (scheduled_id 19345–19349).
- 2026-11-22: feedback do Euro (queda de views). Regras, CTA DIAGNÓSTICO e layout reescritos. Agendamentos antigos de 23/11 a 02/12 cancelados. Lote 2026-11-23 (14 posts, 23/11 a 06/12, aprovado pelo Euro) no layout novo.
