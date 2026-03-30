# Laboratório 6 - P2: Tokenizador BPE e WordPiece

## Estrutura do Projeto

```
lab6/
├── bpe_wordpiece_tokenizer.py   # Implementação das Tarefas 1, 2 e 3
├── requirements.txt             # Dependências
└── README.md
```

---

## Como Executar

```bash
pip install -r requirements.txt
python bpe_wordpiece_tokenizer.py
```

---

## Tarefa 1 — Motor de Frequências

A função `get_stats(vocab)` percorre o corpus tokenizado por caracteres e acumula a frequência de cada par de símbolos adjacentes, ponderada pela frequência da palavra. Utiliza `dict.get(key, 0)` em vez de `defaultdict`, e `zip(symbols, symbols[1:])` para gerar os bigramas sem índice manual. O par `('e', 's')` retorna contagem 9: 6 ocorrências em *newest* + 3 em *widest*.

---

## Tarefa 2 — Loop de Fusão

A função `merge_vocab(pair, v_in)` opera por split/join sem expressão regular: converte cada entrada do vocabulário em lista de símbolos, percorre com índice explícito e funde o par alvo consumindo duas posições de uma vez (`i += 2`). Isso evita fusões indevidas em tokens já consolidados em iterações anteriores.

A função auxiliar `encontrar_par_mais_frequente(stats)` substitui o `max()` com lambda por iteração explícita, tornando o critério de seleção legível.

O loop de K=5 iterações demonstra a formação progressiva de tokens morfológicos: `es` → `est` → `est</w>`.

---

## Tarefa 3 — WordPiece (BERT Multilingual)

### O que significa o prefixo `##`?

O prefixo `##` indica que o token é uma **sub-palavra de continuação**: ele pertence à mesma palavra do token anterior, sem espaço entre eles. Por exemplo, `inconstitucionalmente` pode ser segmentado em `in`, `##constitu`, `##cion`, `##al`, `##mente`.

Esse mecanismo resolve o problema **OOV (*out-of-vocabulary*)**: em vez de emitir `[UNK]` para palavras desconhecidas, o tokenizador WordPiece decompõe a palavra em sub-unidades presentes no vocabulário fixo, preservando informação morfológica e semântica mesmo para neologismos, termos técnicos ou palavras em línguas de baixo recurso.

---

## Uso de Inteligência Artificial

Conforme exigido pelas instruções do laboratório, declaro que **utilizei IA generativa (Claude, da Anthropic)** como auxiliar na construção deste projeto. Os trechos gerados com assistência de IA são:

- A estrutura geral do arquivo `bpe_wordpiece_tokenizer.py` foi gerada com auxílio de IA e revisada para garantir conformidade com os requisitos do laboratório.
- O parágrafo explicativo sobre o prefixo `##` foi redigido com auxílio de IA e revisado para consistência com o conteúdo da disciplina.

Todo o código foi compreendido, testado e validado pelo autor antes da entrega.
