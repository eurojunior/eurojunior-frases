"""Atualiza projeto/conhecimento/ a partir do repositório. Rode: python3 projeto/gerar_conhecimento.py"""
import json, glob, os, datetime
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = os.path.join(R, 'projeto', 'conhecimento')
os.makedirs(out, exist_ok=True)
open(os.path.join(out, 'regras-e-campeas.md'), 'w').write(open(os.path.join(R, 'CLAUDE.md')).read())
L = ['# Frases já usadas (não repetir ideia nem estrutura)', '',
     f'Gerado em {datetime.date.today().isoformat()} a partir de lotes/*/posts.json.', '']
for f in sorted(glob.glob(os.path.join(R, 'lotes', '*', 'posts.json'))):
    lote = os.path.basename(os.path.dirname(f))
    nota = ' (descartado, não publicado)' if lote.startswith('_') else ''
    if lote in ('2026-11-14', '2026-11-28'): nota = ' (CONTRAEXEMPLO: tom de bronca/aula de gestão, não imitar)'
    L += [f'## Lote {lote}{nota}', '']
    base = None if lote.startswith('_') else datetime.date.fromisoformat(lote)
    for i, p in enumerate(json.load(open(f))):
        q = (p.get('quote') or p.get('frase') or '').replace('\n\n', ' ')
        d = (base + datetime.timedelta(days=i)).strftime('%d/%m') + ' · ' if base else ''
        pad = f"padrão {p['padrao']} · " if 'padrao' in p else ''
        L.append(f'- {d}{pad}{q}')
    L.append('')
open(os.path.join(out, 'frases-ja-usadas.md'), 'w').write('\n'.join(L))
print('ok')
