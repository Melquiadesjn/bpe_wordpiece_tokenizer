"""
Laboratório 6 - P2: Tokenizador BPE e WordPiece
"""

# ============================================================
# Tarefa 1: Motor de Frequências
# ============================================================

vocab = {
    'l o w </w>': 5,
    'l o w e r </w>': 2,
    'n e w e s t </w>': 6,
    'w i d e s t </w>': 3
}

def get_stats(vocab):
    pairs = {}
    for word, freq in vocab.items():
        symbols = word.split()  # divide em lista de símbolos: ['l', 'o', 'w', '</w>']
        
        # zip(symbols, symbols[1:]) gera todos os pares adjacentes de uma vez
        for sym_a, sym_b in zip(symbols, symbols[1:]):
            pair = (sym_a, sym_b)
            # dict.get(key, 0) retorna 0 se a chave não existe ainda
            pairs[pair] = pairs.get(pair, 0) + freq
    return pairs

stats = get_stats(vocab)
print("=" * 55)
print("TAREFA 1 — Validação do Motor de Frequências")
print(f"  Par ('e', 's') -> {stats[('e', 's')]}  (esperado: 9)")
print("=" * 55)



# ============================================================
# Tarefa 2: Loop de Fusão
# ============================================================

def merge_vocab(pair, vocab_in):
    sym_a, sym_b = pair
    merged_token = sym_a + sym_b  # ex: ('e','s') -> 'es'
    vocab_out = {}

    for word, freq in vocab_in.items():
        symbols = word.split()
        fused = []  
        i = 0
        while i < len(symbols):
            if i < len(symbols) - 1 and symbols[i] == sym_a and symbols[i + 1] == sym_b:
                fused.append(merged_token)
                i += 2  
            else:
                fused.append(symbols[i])
                i += 1
        vocab_out[' '.join(fused)] = freq

    return vocab_out


def encontrar_par_mais_frequente(stats):
    melhor_par = None
    melhor_contagem = -1
    for par, contagem in stats.items():
        if contagem > melhor_contagem:
            melhor_contagem = contagem
            melhor_par = par
    return melhor_par


print("\nTAREFA 2 — Loop de Fusão (K=5 iterações)")
print("=" * 55)

for iteracao in range(1, 6):
    stats = get_stats(vocab)
    best = encontrar_par_mais_frequente(stats)
    vocab = merge_vocab(best, vocab)

    print(f"\nIteração {iteracao} | Par fundido: {best[0] + best[1]!r}  {best}")
    for token, freq in vocab.items():
        print(f"  {freq}x  '{token}'")

print("\n" + "=" * 55)


# ============================================================
# Tarefa 3: WordPiece com BERT Multilingual
# ============================================================

from transformers import AutoTokenizer

print("\nTAREFA 3 — WordPiece (bert-base-multilingual-cased)")
print("=" * 55)

tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")

frase = "Os hiper-parâmetros do transformer são inconstitucionalmente difíceis de ajustar."
tokens = tokenizer.tokenize(frase)

print(f"Frase original:\n  {frase}")
print(f"\nTokens WordPiece ({len(tokens)} tokens):")

# Exibe com índice para facilitar leitura
for idx, tok in enumerate(tokens):
    marcador = "  ##" if tok.startswith("##") else "   >"
    print(f"  [{idx:02d}] {marcador} {tok}")

print("=" * 55)
# ajuste: descricao inicial do tokenizer
# ajuste: explicacao da funcao get_stats
# ajuste: explicacao da funcao merge_vocab
# ajuste: selecao do par mais frequente
# ajuste: inicio do loop de treinamento
