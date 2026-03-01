import streamlit as st
from fpdf import FPDF
import time


# --- 1. DESIGN ---
def aplicar_estilo_v52():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }
    .stApp { background-color: #f8f9fa; }
    div[data-testid="stForm"] {
        background-color: white !important;
        border-radius: 15px !important;
        padding: 30px !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05) !important;
    }
    .item-card {
        background: white; padding: 15px; border-radius: 10px;
        border-left: 5px solid #b8860b; margin-bottom: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.02);
    }
    .total-card {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        color: white; padding: 20px; border-radius: 12px;
        text-align: center; margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)


st.set_page_config(page_title="EventMaster Pro", page_icon="💍", layout="wide")
aplicar_estilo_v52()

if 'gastos' not in st.session_state: st.session_state.gastos = {}
if 'config_feita' not in st.session_state: st.session_state.config_feita = False
if 'item_editando' not in st.session_state: st.session_state.item_editando = None


# --- 2. CONFIGURAÇÃO INICIAL ---
@st.dialog("🎯 Configure seu Evento")
def configuracao_inicial():
    n_p = st.session_state.get("nome_evento", "Meu Grande Dia")
    t_p = st.session_state.get("tipo_evento", "Casamento")
    nome = st.text_input("Nome do Evento:", value=n_p)
    tipo = st.selectbox("Tipo de Evento:", ["Casamento", "15 Anos", "Formatura", "Evento Social"],
                        index=["Casamento", "15 Anos", "Formatura", "Evento Social"].index(t_p))
    if st.button("Salvar e Abrir", use_container_width=True):
        st.session_state.update({"nome_evento": nome, "tipo_evento": tipo, "config_feita": True})
        st.rerun()


if not st.session_state.config_feita:
    configuracao_inicial()
    st.stop()

# --- 3. INTERFACE ---
c_h1, c_h2 = st.columns([8, 2])
c_h1.markdown(f"<h1>✨ {st.session_state.nome_evento} ({st.session_state.tipo_evento})</h1>", unsafe_allow_html=True)
if c_h2.button("⚙️ Editar Evento"): configuracao_inicial()

# Usaremos o placeholder apenas para SUCESSO agora
msg_sucesso = st.empty()

with st.container():
    base = ["Buffet", "Salão", "Vestido", "Maquiadora", "Fotógrafo", "Banda", "Alianças", "Terno", "Decoração", "Doces",
            "Lembranças", "Outro..."]
    it_disp = [i for i in base if i not in st.session_state.gastos or i == "Outro..."]
    item_sel = st.selectbox("Selecione o serviço:",
                            [st.session_state.item_editando] if st.session_state.item_editando else it_disp)

    n_final = item_sel
    if item_sel == "Outro...": n_final = st.text_input("Qual o nome do item?")

    forma = st.radio("Como pretende pagar?", ["À Vista", "Parcelado"], horizontal=True)

    with st.form("form_v52", clear_on_submit=True):
        v_in = st.text_input("Valor Bruto:", placeholder="Ex: 5000", key="v_k")
        n_p, j_in = 1, "0"

        if forma == "Parcelado":
            col1, col2 = st.columns(2)
            n_p = col1.number_input("Nº Parcelas:", min_value=1, value=1)
            j_in = col2.text_input("Juros Totais (%):", value="0", key="j_k")

        if st.form_submit_button("✅ Adicionar ao Orçamento", use_container_width=True):
            # Captura segura dos dados
            v_val = st.session_state.v_k.strip()
            j_val = st.session_state.get("j_k", "0").strip()
            if not j_val: j_val = "0"

            if v_val:
                try:
                    v_c = float(v_val.replace(".", "").replace(",", "."))
                    j_c = float(j_val.replace(",", "."))
                    v_total = v_c * (1 + (j_c / 100))
                    v_parc = v_total / n_p

                    if forma == "À Vista":
                        desc, t_str = "Pagamento à Vista", f"R$ {v_total:.2f}"
                    else:
                        desc, t_str = f"{n_p}x de {v_parc:.2f} (c/ {j_c}%)", f"R$ {v_total:.2f}"

                    st.session_state.gastos[n_final] = [v_c, v_total, desc, t_str]
                    st.session_state.item_editando = None

                    # MOSTRA APENAS O SUCESSO
                    msg_sucesso.success(f"✔️ {n_final} adicionado!")
                    time.sleep(0.5)
                    st.rerun()
                except:
                    # Se der erro no cálculo, ele só não adiciona. Sem mensagem vermelha chata.
                    pass

# --- 4. EXTRATO, SALDO E PDF ---
if st.session_state.gastos:
    st.divider()
    total = sum(d[1] for d in st.session_state.gastos.values())
    for it, d in list(st.session_state.gastos.items()):
        st.markdown(f"<div class='item-card'><b>{it}</b> • {d[2]}<br><span style='color:#1e3a8a'>{d[3]}</span></div>",
                    unsafe_allow_html=True)
        e, r = st.columns(2)
        if e.button("✏️", key=f"e_{it}"): st.session_state.item_editando = it; st.rerun()
        if r.button("🗑️", key=f"r_{it}"): del st.session_state.gastos[it]; st.rerun()

    st.markdown(f"<div class='total-card'>TOTAL ACUMULADO: R$ {total:.2f}</div>", unsafe_allow_html=True)

    # Consulta Saldo
    st.divider()
    limite = st.text_input("Limite de Orçamento (R$):", value="0,00", key="s_k")
    try:
        l_v = float(limite.replace(".", "").replace(",", "."))
        if l_v > 0:
            sobra = l_v - total
            if sobra >= 0:
                st.success(f"💰 Sobra: R$ {sobra:.2f}")
            else:
                st.error(f"🚨 Estourou: R$ {abs(sobra):.2f}")
    except:
        pass


    # PDF
    def gerar_pdf(nome, lista, total_valor):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_draw_color(184, 134, 11);
        pdf.rect(5, 5, 200, 287)
        pdf.ln(35);
        pdf.set_fill_color(184, 134, 11);
        pdf.set_text_color(255);
        pdf.set_font("Arial", "B", 16)
        pdf.cell(190, 15, f"ORCAMENTO: {nome.upper()}", 1, 1, "C", 1)
        pdf.ln(10);
        pdf.set_text_color(0);
        pdf.set_font("Arial", "B", 10)
        for it_n, d_n in lista.items():
            pdf.cell(70, 10, f" {it_n}", 1);
            pdf.cell(70, 10, f" {d_n[2]}", 1);
            pdf.cell(50, 10, f" {d_n[3]}", 1, 1, "R")
        pdf.ln(10);
        pdf.cell(140, 12, "TOTAL FINAL", 1, 0, "R");
        pdf.cell(50, 12, f" R$ {total_valor:.2f}", 1, 1, "C")
        return pdf.output(dest="S").encode("latin-1", "ignore")


    pdf_file = gerar_pdf(st.session_state.nome_evento, st.session_state.gastos, total)
    st.download_button("📥 Baixar Orçamento PDF", pdf_file, "Orcamento.pdf", "application/pdf", use_container_width=True)