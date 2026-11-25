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

## Por que estas regras existem (análise do Euro, 22/11/2026)
16 frases que deram certo (1,2 mil a 38,8 mil curtidas) contra 5 frases feitas só pela IA (77 a 289 curtidas), com visual idêntico — a diferença era 100% o texto. As campeãs não falam de advocacia na arte: são fé, prosperidade e superação, e fazem o leitor se sentir bem. As da IA davam aula de gestão e acusavam o leitor ("não é empresa, é emprego com CNPJ"); ninguém reposta frase que o chama de amador, e o repost é o que explode o alcance (campeãs: 400 a 1,9 mil reposts; IA: 1 a 13). O público comenta para declarar fé ("Amém, eu recebo", "Eu creio"): frases com "envie pra si mesmo se acredita" tiveram 87 e 96 comentários (média < 10). O CTA "link na bio" deu zero comentários; o CTA de comentário alimenta o ManyChat e gera MQL.
Sem clichê de coach (zona de conforto, universo conspira). Nunca invente fatos da vida do Euro ("Euro vulnerável" só como sentimento: "eu sonhava…", "eu pedi a Deus…"). Leitor como herói ou Euro vulnerável.

## Campeãs (imite o nível, não copie e não repita ideia nem estrutura)
- "Você está entrando no período mais próspero da sua história. Se acredita nisso, envie pra si mesmo." (38,8 mil)
- "A porta do sucesso é larga mas ela é baixa, só passa de joelho. Seja humilde!" (11,1 mil)
- "A vontade de vencer em mim não veio de um dia bonito, veio de um dia insuportável." (8,4 mil)
- "Quando Deus quis fazer Davi um rei, enviou Golias, não uma coroa." (5,7 mil)
- "Logo, você vai viver o que um dia foi só um sonho seu. Envie pra si mesmo se acredita." (4,7 mil)
- "Honre o lugar que permite o pão de cada dia chegar na sua mesa." (4 mil)
- "Esse ano, vamos prosperar tanto que o nosso bolso vai ser usado para ajudar outras famílias. Manda pra quem vai prosperar junto de você, se você acredita." (2,2 mil)
- "Que privilégio é estar esgotado por uma rotina que um dia pedi pra ter." (2,2 mil)
- "Não é caro pagar pelo serviço de quem sabe fazer o que você não sabe fazer." (1,9 mil)
- "Juntos desde o sufoco. Juntos até o topo! Mande pra quem esteve com você no sufoco e vai chegar no topo contigo." (1,7 mil)
- "Nenhum cliente, processo ou parceria vale mais do que a sua saúde mental."
- "Eu sonhava em estar onde estou agora. E, às vezes, preciso me lembrar disso."
- "Ninguém vai acreditar no seu sonho com a mesma coragem que você."
- "Não deixe ninguém colocar preço naquilo que custou seu tempo, seu esforço, seu suor e suas lágrimas."
- "Um barco ancorado é seguro, mas não foi pra isso que barcos foram feitos."

## Ruins (nunca escreva assim)
- "Escritório que depende de você para tudo não é empresa. É emprego com CNPJ." (91 curtidas)
- "Não existe escritório milionário com dono que faz tudo sozinho." (77 curtidas)
- Todo o conteúdo dos lotes 2026-11-14 e 2026-11-28.

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
