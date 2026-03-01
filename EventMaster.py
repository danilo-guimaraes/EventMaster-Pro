# ==========================================
# EVENTMASTER PRO v5.0 - INTERFACE DINÂMICA
# DESENVOLVEDOR: DANILO (ADS ESTÁCIO)
# ==========================================

# --- CONFIGURAÇÕES E BANCO DE ITENS ---
itens_casamento = [
    "Buffet", "Salão", "Vestido", "Maquiadora", "Arte do casamento",
    "Fotógrafo", "Celebrante", "Banda", "Orquestra", "Chinelos",
    "Bem casados", "Doces de fora", "Lembranças madrinhas",
    "Lembranças padrinhos", "Lembranças pais", "Lembranças daminhas",
    "Lembranças pajens", "Fogos", "Alianças", "Terno", "Buquê", "Ensaio Externo"
]

gastos_detalhados = {}  # {"Item": [Valor, Forma, Parcelas, Juros]}


# --- MOTOR DE CÁLCULO ---
def calcular_financeiro():
    vista, parc_juros, juros_total = 0, 0, 0
    for item, dados in gastos_detalhados.items():
        v_base, f_pagto, qtd_p, tx_j = dados
        if f_pagto == "2":
            v_final = v_base * (1 + (tx_j / 100) * qtd_p)
            parc_juros += v_final
            juros_total += (v_final - v_base)
        else:
            vista += v_base
    return vista, parc_juros, juros_total


# --- MENU PRINCIPAL ---
while True:
    print("\n" + "=" * 40)
    print("      EVENTMASTER PRO - DASHBOARD")
    print("=" * 40)
    print("1. Lançar Item Específico (Livre)")
    print("2. Ver Extrato e Saldo Final")
    print("3. Sair")

    opcao = input("\nSelecione: ")

    # --- BLOCO 1: LANÇAMENTO LIVRE (SEM FILA INDIANA) ---
    if opcao == "1":
        while True:
            print("\n--- ITENS DISPONÍVEIS PARA LANÇAR ---")
            for i, nome in enumerate(itens_casamento):
                # Mostra o status: [OK] se já foi lançado, [ ] se está vazio
                status = "[OK]" if nome in gastos_detalhados else "[  ]"
                print(f"{i + 1:02d}. {status} {nome}")

            escolha = input("\nDigite o número do item para lançar/editar (ou 'S' para voltar): ")

            if escolha.upper() == 'S': break

            try:
                indice = int(escolha) - 1
                item_escolhido = itens_casamento[indice]

                print(f"\n>>> CONFIGURANDO: {item_escolhido}")
                v_item = float(input("Valor do item: R$ "))
                f_pagto = input("Forma (1-À Vista / 2-Parcelado): ")

                if f_pagto == "2":
                    p = int(input("Parcelas: "))
                    j = float(input("Taxa de Juros (%): "))
                    gastos_detalhados[item_escolhido] = [v_item, f_pagto, p, j]
                else:
                    gastos_detalhados[item_escolhido] = [v_item, f_pagto, 1, 0]

                print(f"✅ {item_escolhido} salvo com sucesso!")
            except (ValueError, IndexError):
                print("❌ Escolha inválida! Digite o número da lista.")

    # --- BLOCO 2: RELATÓRIO E SALDO ---
    elif opcao == "2":
        if not gastos_detalhados:
            print("\n⚠️ Nada lançado ainda.")
            continue

        v_vista, v_parc, v_juros = calcular_financeiro()
        total = v_vista + v_parc

        print("\n--- EXTRATO DETALHADO ---")
        for it, d in gastos_detalhados.items():
            tipo = f"Parcelado {d[2]}x" if d[1] == "2" else "À Vista"
            print(f"{it:.<20} R$ {d[0]:>10.2f} ({tipo})")

        print("-" * 40)
        orc = float(input("Orçamento da Noiva: R$ "))
        print(f"CUSTO TOTAL REAL: R$ {total:.2f}")
        print(f"SALDO: R$ {orc - total:.2f}")

    elif opcao == "3":
        break