# Piteira — Site oficial

Site de página única da banda **Piteira** (tributo a Pitty, Florianópolis/SC).
Estático, sem build. Audiência: produtores/contratantes + fãs. **PT-BR.**

## Editar
Edite `index.html` (conteúdo), `styles.css` (visual) e `main.js` (menu/galeria).
`stageplot.py` gera `assets/stageplot.svg`. `rider.html` é o rider técnico (não indexado, `/rider`).
`presskit.html` é o press kit / material de divulgação (não indexado; logos ficam no Google Drive).
Sem build — basta salvar.

**Crédito de fotos:** as fotos originais dos membros são de @manufaverofoto; a do Pedro e as próximas são de @joao_azuos.
Ao trocar/adicionar fotos, manter o `.m-credit` (seção "Membros") de acordo.

## TODO (decididos em 2026-07, aguardando material/ação)
- **Vídeo ao vivo** — maior alavanca de conversão p/ contratantes. Aguardando a banda gravar de novo (troca de baixista em 2026-07).
- **Domínio próprio** (ex.: `piteira.com.br`, ~R$40/ano no Registro.br) — depois atualizar `og:url`, `og:image` e os URLs do JSON-LD em `index.html`.
- **Depoimentos** — pedir 1 frase p/ Loud Fest, Haoma e Bar do Castelo; adicionar em "Ao Vivo" com faixa de números (shows/cidades).
- **Agenda / próximos shows** — quando houver datas; fallback "últimos palcos" quando vazia.
- **Painel Cloudflare (sem código)**: ativar *Web Analytics* e o *managed robots.txt* (bloqueia crawlers de IA; NÃO criar robots.txt no repo — o gerenciado da Cloudflare sobrescreve na borda).

## Pré-visualizar localmente
    python3 -m http.server 8000
    # abra http://localhost:8000

## Marca
- Cores (`:root`): `--purple:#CA88F1` · `--green:#8cfa8c` · `--ink:#0b0a0d` · `--cream:#f3eef7` · `--plum:#1c1022`.
- Fontes: Playfair Display (títulos) + Inter (corpo). Nome da banda = logo (imagem).
