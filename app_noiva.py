import streamlit as st
import streamlit.components.v1 as components

# Configuração base
st.set_page_config(page_title="EventMaster Pro", layout="wide", initial_sidebar_state="collapsed")

# 🔴 O TRUQUE MÁGICO AQUI: Forçando o Streamlit a apagar as margens padrão dele
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem !important;
            padding-bottom: 0rem !important;
            padding-left: 1rem !important;
            padding-right: 1rem !important;
            max-width: 98% !important; /* Libera a tela toda no monitor do PC */
        }
        iframe {
            width: 100% !important;
        }
    </style>
""", unsafe_allow_html=True)

html_final = """
<!doctype html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.5.28/jspdf.plugin.autotable.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@400;600&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; background-color: #f8fafc; color: #1e293b; }
        .font-display { font-family: 'Playfair Display', serif; }
        .gradient-gold { background: linear-gradient(135deg, #B8860B 0%, #DAA520 100%); }
        .card-shadow { box-shadow: 0 10px 40px rgba(0,0,0,0.06); }
        .modal-backdrop { background: rgba(0, 0, 0, 0.5); backdrop-filter: blur(4px); }
        .btn-primary { background: #d4a017; color: white; font-weight: bold; transition: 0.3s; border-radius: 12px; }
        .btn-primary:hover { background: #b8860b; transform: translateY(-1px); box-shadow: 0 10px 20px rgba(212, 160, 23, 0.2); }
        .servico-card { border: 2px solid #f1f5f9; transition: 0.2s; cursor: pointer; background: white; }
        .servico-card.selected { border-color: #d4a017; background: #fffcf0; border-width: 3px; transform: scale(1.02); }
        .servico-card.disabled { opacity: 0.4; cursor: not-allowed; background: #f8fafc; transform: none; }
        .toast { position: fixed; top: 20px; right: 20px; background: #22c55e; color: white; padding: 12px 24px; border-radius: 12px; display: none; z-index: 1000; }

        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: #f1f5f9; border-radius: 10px; }
        ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
        ::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
    </style>
</head>
<body class="antialiased">

    <div id="toast" class="toast font-semibold shadow-xl border border-green-400">✅ Sucesso!</div>

    <div id="config-modal" class="fixed inset-0 z-50 flex items-center justify-center modal-backdrop p-4">
        <div class="bg-white rounded-3xl p-8 md:p-10 max-w-md w-full card-shadow text-center relative overflow-hidden">
            <div class="absolute top-0 left-0 w-full h-2 gradient-gold"></div>
            <div id="config-icon" class="w-20 h-20 gradient-gold rounded-full flex items-center justify-center mx-auto mb-6 text-white text-3xl shadow-lg">💍</div>
            <h2 class="font-display text-2xl font-bold mb-2 text-gray-800">Acessar Orçamento</h2>
            <p id="modal-desc" class="text-sm text-gray-500 mb-8">Seus dados ficam salvos no seu aparelho.</p>

            <div class="text-left space-y-4">
                <div id="container-celular">
                    <label class="block text-sm font-bold text-gray-700 mb-2">📱 Seu Celular (WhatsApp)</label>
                    <input type="tel" id="input-celular" maxlength="15" class="w-full p-4 border-2 border-amber-200 rounded-xl outline-none focus:border-amber-500 font-bold text-gray-800 transition-colors" placeholder="(21) 90000-0000">
                </div>

                <input type="text" id="input-nome" class="w-full p-4 border-2 border-gray-100 rounded-xl outline-none focus:border-amber-500 transition-colors" placeholder="Nome do Cliente/Evento">
                <select id="input-tipo" onchange="updateConfigUI()" class="w-full p-4 border-2 border-gray-100 rounded-xl bg-white outline-none cursor-pointer">
                    <option value="💍 Casamento">💍 Casamento</option>
                    <option value="🎭 15 Anos">🎭 15 Anos</option>
                    <option value="🎓 Formatura">🎓 Formatura</option>
                    <option value="outro">✨ Outro Evento...</option>
                </select>
                <input type="text" id="input-outro-tipo" class="hidden w-full p-4 border-2 border-gray-100 rounded-xl outline-none focus:border-amber-500" placeholder="Qual o tipo de festa?">

                <button id="btn-modal" onclick="iniciarApp()" class="w-full btn-primary p-4 mt-6 shadow-lg text-lg">Entrar no Sistema →</button>
            </div>
        </div>
    </div>

    <div id="main-app" class="hidden w-full max-w-[96%] mx-auto py-4 px-2 sm:px-4 lg:px-6">
        <header class="flex justify-between items-center mb-8 bg-white p-5 md:p-6 rounded-2xl shadow-sm border border-gray-100">
            <div class="flex items-center gap-4">
                <div id="header-icon" class="w-12 h-12 md:w-14 md:h-14 gradient-gold rounded-xl flex items-center justify-center text-2xl md:text-3xl text-white shadow-inner">💍</div>
                <div>
                    <h1 id="display-titulo" class="font-display text-xl md:text-3xl font-bold text-gray-800">EventMaster Pro</h1>
                    <p id="display-sub" class="text-sm md:text-base text-gray-500 italic"></p>
                </div>
            </div>
            <div class="flex gap-2">
                <button onclick="abrirConfig()" class="bg-gray-100 hover:bg-gray-200 p-2 md:px-5 rounded-xl font-bold text-gray-600 transition-all hidden sm:flex items-center gap-2">⚙️ Editar Título</button>
                <button onclick="sairSessao()" class="bg-red-50 hover:bg-red-100 p-2 md:px-5 rounded-xl font-bold text-red-600 transition-all flex items-center gap-2">🚪 <span class="hidden sm:inline">Sair</span></button>
            </div>
        </header>

        <div class="grid lg:grid-cols-12 gap-6 xl:gap-10">

            <div class="lg:col-span-8 bg-white rounded-3xl p-6 md:p-10 card-shadow border border-gray-50">
                <h3 class="font-display text-2xl mb-8 text-amber-700 font-bold border-b border-gray-100 pb-4">📝 Adicionar Serviço</h3>

                <div id="grid-servicos" class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 xl:grid-cols-5 gap-3 md:gap-4 mb-10"></div>

                <div id="container-nome-servico" class="hidden mb-8 p-5 md:p-6 bg-amber-50 rounded-2xl border border-amber-200 shadow-sm">
                    <label class="block text-sm font-bold text-amber-800 mb-3">Qual o nome deste serviço?</label>
                    <input type="text" id="input-nome-servico" class="w-full p-4 border-2 border-white rounded-xl outline-none focus:border-amber-400 text-lg shadow-sm" placeholder="Ex: Segurança, Garçom, Manobrista...">
                </div>

                <div id="container-convidados" class="hidden grid sm:grid-cols-2 gap-6 mb-8 p-5 md:p-6 bg-blue-50/50 rounded-2xl border border-blue-100">
                    <div>
                        <label class="block text-sm font-bold text-blue-800 mb-3">Qtd de Pessoas/Unidades:</label>
                        <input type="number" id="input-qtd-convidados" class="w-full p-4 border-2 border-white rounded-xl outline-none focus:border-blue-400 text-lg shadow-sm" value="100" min="1">
                    </div>
                    <div>
                        <label class="block text-sm font-bold text-blue-800 mb-3">Valor Unitário (R$):</label>
                        <input type="number" id="input-valor-convidado" class="w-full p-4 border-2 border-white rounded-xl outline-none focus:border-blue-400 text-lg shadow-sm" placeholder="Ex: 80,00">
                    </div>
                </div>

                <div id="container-valor-padrao" class="mb-8">
                    <label class="block text-sm font-bold text-gray-700 mb-3">Valor Fixo do Serviço (R$):</label>
                    <input type="number" id="valor-input" class="w-full p-5 border-2 border-gray-100 rounded-xl text-xl outline-none focus:border-amber-500 shadow-sm transition-colors" placeholder="0,00">
                </div>

                <div class="grid sm:grid-cols-3 gap-4 md:gap-6 mb-10 p-5 md:p-6 bg-gray-50 rounded-2xl border border-gray-100">
                    <div>
                        <label class="block text-sm font-bold text-gray-700 mb-3">Condição de Pagamento:</label>
                        <select id="select-pagamento" onchange="toggleParcelas()" class="w-full p-4 border-2 border-white rounded-xl bg-white outline-none cursor-pointer shadow-sm">
                            <option value="avista">💵 À Vista</option>
                            <option value="parcelado">💳 Parcelado</option>
                        </select>
                    </div>
                    <div id="container-parcelas-1" class="hidden">
                        <label class="block text-sm font-bold text-gray-700 mb-3">Quantidade de Vezes:</label>
                        <select id="qtd-parcelas" class="w-full p-4 border-2 border-white rounded-xl bg-white outline-none cursor-pointer shadow-sm"></select>
                    </div>
                    <div id="container-parcelas-2" class="hidden">
                        <label class="block text-sm font-bold text-gray-700 mb-3">Juros a.m. (%):</label>
                        <input type="number" id="input-juros" class="w-full p-4 border-2 border-white rounded-xl outline-none shadow-sm" value="2" step="0.1" min="0">
                    </div>
                </div>

                <button onclick="adicionarAoOrcamento()" class="w-full btn-primary p-6 text-xl shadow-xl uppercase tracking-wider">Adicionar ao Orçamento</button>
            </div>

            <div class="lg:col-span-4 space-y-6 lg:sticky lg:top-6 self-start">

                <div class="bg-slate-900 text-white p-6 md:p-8 rounded-3xl shadow-2xl border-b-8 border-amber-500 relative overflow-hidden">
                    <div class="absolute -right-10 -top-10 opacity-10 text-9xl">💰</div>
                    <div class="text-center mb-6 relative z-10">
                        <p class="text-gray-400 text-xs font-bold uppercase tracking-widest mb-2">Total Estimado do Evento</p>
                        <h2 id="total-display" class="text-4xl md:text-5xl font-bold text-amber-400 font-display">R$ 0,00</h2>
                        <p id="itens-count" class="text-gray-400 mt-3 text-sm font-medium">Nenhum serviço incluso</p>
                    </div>

                    <div class="pt-6 border-t border-slate-700/50 relative z-10">
                        <label class="block text-xs font-bold text-gray-400 uppercase tracking-wider mb-3 text-center">Budget Disponível do Cliente (R$):</label>
                        <input type="number" id="input-orcamento-cliente" oninput="calcularSaldo(); salvarSessao();" class="w-full p-4 rounded-xl bg-slate-800/80 text-white border border-slate-600 outline-none focus:border-amber-400 text-center text-xl font-bold placeholder-slate-600 transition-colors" placeholder="Ex: 50000">
                        <div id="saldo-display" class="mt-4 text-sm md:text-base font-bold hidden p-4 rounded-xl text-center transition-all shadow-inner"></div>
                    </div>

                    <button id="btn-pdf" onclick="gerarPDF()" class="hidden relative z-10 mt-8 w-full bg-gradient-to-r from-amber-600 to-amber-500 hover:from-amber-500 hover:to-amber-400 text-white p-4 rounded-xl font-bold text-sm transition-all flex items-center justify-center gap-2 shadow-lg hover:shadow-amber-500/25">
                        <span class="text-lg">📥</span> GERAR PROPOSTA (PDF)
                    </button>
                </div>

                <div class="bg-white p-6 md:p-8 rounded-3xl card-shadow border border-gray-50 flex flex-col max-h-[600px]">
                    <h3 class="font-display text-xl font-bold mb-4 border-b border-gray-100 pb-4 text-gray-800 flex justify-between items-center">
                        Itens Inclusos
                        <span class="text-xs font-normal text-gray-400 bg-gray-100 px-3 py-1 rounded-full">Atualizado agora</span>
                    </h3>
                    <div id="lista-real" class="space-y-3 overflow-y-auto pr-2 pb-2 flex-1"></div>
                </div>
            </div>
        </div>
    </div>

    <script>
        const servicosBase = [
            {id: 'convidados', nome: 'Convidados', icon: '👥'},
            {id: 'buffet', nome: 'Buffet Fixo', icon: '🍽️'},
            {id: 'salao', nome: 'Salão', icon: '🏛️'},
            {id: 'vestido', nome: 'Vestido', icon: '👗'},
            {id: 'foto', nome: 'Fotógrafo', icon: '📸'},
            {id: 'decor', nome: 'Decoração', icon: '🌸'},
            {id: 'lembranca', nome: 'Lembranças', icon: '🎁'},
            {id: 'outro', nome: 'Outro', icon: '✨'}
        ];

        let orcamento = [];
        let selecionadoId = null;
        let totalAtual = 0;
        let telefoneLogado = null;
        let isEditandoConfig = false;

        document.getElementById('input-celular').addEventListener('input', function (e) {
            let x = e.target.value.replace(/\D/g, '').match(/(\d{0,2})(\d{0,5})(\d{0,4})/);
            e.target.value = !x[2] ? x[1] : '(' + x[1] + ') ' + x[2] + (x[3] ? '-' + x[3] : '');
        });

        const selectP = document.getElementById('qtd-parcelas');
        for(let i=1; i<=24; i++) {
            let opt = document.createElement('option');
            opt.value = i; opt.innerHTML = i + 'x vezes';
            selectP.appendChild(opt);
        }

        function updateConfigUI() {
            const val = document.getElementById('input-tipo').value;
            const iconDiv = document.getElementById('config-icon');
            document.getElementById('input-outro-tipo').classList.toggle('hidden', val !== 'outro');
            if (val.includes('Casamento')) iconDiv.innerText = '💍';
            else if (val === 'outro') iconDiv.innerText = '🎉';
            else iconDiv.innerText = '🎭';
        }

        function abrirConfig() { 
            isEditandoConfig = true;
            document.getElementById('config-modal').classList.remove('hidden'); 
            document.getElementById('container-celular').classList.add('hidden'); 
            document.getElementById('modal-desc').innerText = "Atualize os detalhes do evento.";
            document.getElementById('btn-modal').innerText = "Salvar Alterações →";
            document.getElementById('input-nome').value = document.getElementById('display-titulo').innerText;
        }

        function sairSessao() {
            telefoneLogado = null;
            isEditandoConfig = false;
            document.getElementById('input-celular').value = '';
            document.getElementById('container-celular').classList.remove('hidden');
            document.getElementById('btn-modal').innerText = "Entrar no Sistema →";
            document.getElementById('modal-desc').innerText = "Seus dados ficam salvos no seu aparelho.";
            document.getElementById('main-app').classList.add('hidden');
            document.getElementById('config-modal').classList.remove('hidden');
            orcamento = [];
            atualizarUI();
        }

        function iniciarApp() {
            if (!isEditandoConfig) {
                const celularRaw = document.getElementById('input-celular').value.replace(/\D/g, '');
                if(celularRaw.length !== 11) return alert("⚠️ Por favor, digite um celular válido com DDD (Ex: 21988887777).");
                telefoneLogado = celularRaw;

                const savedData = localStorage.getItem('em_data_' + telefoneLogado);
                const savedConfig = localStorage.getItem('em_config_' + telefoneLogado);

                if(savedData && savedConfig) {
                    orcamento = JSON.parse(savedData);
                    const cfg = JSON.parse(savedConfig);
                    document.getElementById('display-titulo').innerText = cfg.nome;
                    document.getElementById('display-sub').innerText = cfg.tipo;
                    document.getElementById('header-icon').innerText = cfg.icone;
                    document.getElementById('input-orcamento-cliente').value = cfg.budget || '';
                    document.getElementById('input-nome').value = cfg.nome; 
                    showToast("Sessão recuperada!");
                } else {
                    aplicarConfigDaTela();
                    orcamento = [];
                    showToast("Sessão iniciada!");
                }
            } else {
                aplicarConfigDaTela();
                showToast("Nome do evento atualizado!");
            }

            document.getElementById('config-modal').classList.add('hidden');
            document.getElementById('main-app').classList.remove('hidden');
            isEditandoConfig = false;
            renderGrid();
            atualizarUI(); 
            salvarSessao();
        }

        function aplicarConfigDaTela() {
            const nome = document.getElementById('input-nome').value || 'Cliente Master';
            const tipoRaw = document.getElementById('input-tipo').value;
            let tipoFinal = tipoRaw; let iconeFinal = '💍';

            if(tipoRaw === 'outro') {
                tipoFinal = document.getElementById('input-outro-tipo').value || 'Evento Especial';
                iconeFinal = '🎉';
            } else {
                iconeFinal = tipoRaw.split(' ')[0];
                tipoFinal = tipoRaw.split(' ')[1];
            }

            document.getElementById('display-titulo').innerText = nome;
            document.getElementById('display-sub').innerText = tipoFinal;
            document.getElementById('header-icon').innerText = iconeFinal;
        }

        function salvarSessao() {
            if(!telefoneLogado) return;
            const config = {
                nome: document.getElementById('display-titulo').innerText,
                tipo: document.getElementById('display-sub').innerText,
                icone: document.getElementById('header-icon').innerText,
                budget: document.getElementById('input-orcamento-cliente').value
            };
            localStorage.setItem('em_config_' + telefoneLogado, JSON.stringify(config));
            localStorage.setItem('em_data_' + telefoneLogado, JSON.stringify(orcamento));
        }

        function toggleParcelas() {
            const modo = document.getElementById('select-pagamento').value;
            const isParc = modo === 'parcelado';
            document.getElementById('container-parcelas-1').style.display = isParc ? 'block' : 'none';
            document.getElementById('container-parcelas-2').style.display = isParc ? 'block' : 'none';
        }

        function renderGrid() {
            const grid = document.getElementById('grid-servicos');
            grid.innerHTML = servicosBase.map(s => {
                const jaTem = (s.id !== 'outro') && orcamento.some(item => item.id === s.id);
                const css = jaTem ? 'disabled' : (selecionadoId === s.id ? 'selected' : '');
                return `<div class="servico-card ${css} p-4 md:p-5 rounded-2xl text-center shadow-sm" onclick="${jaTem ? '' : `setServico('${s.id}')`}">
                            <span class="text-3xl md:text-4xl block mb-2">${s.icon}</span>
                            <span class="text-xs md:text-sm font-bold text-gray-700">${s.nome}</span>
                        </div>`;
            }).join('');
        }

        function setServico(id) { 
            selecionadoId = id; 
            document.getElementById('container-nome-servico').classList.toggle('hidden', id !== 'outro');
            if(id === 'convidados') {
                document.getElementById('container-convidados').classList.remove('hidden');
                document.getElementById('container-valor-padrao').classList.add('hidden');
            } else {
                document.getElementById('container-convidados').classList.add('hidden');
                document.getElementById('container-valor-padrao').classList.remove('hidden');
            }
            renderGrid(); 
        }

        function adicionarAoOrcamento() {
            const modo = document.getElementById('select-pagamento').value;
            const vezes = parseInt(document.getElementById('qtd-parcelas').value);
            const juros = parseFloat(document.getElementById('input-juros').value) || 0;

            if (!selecionadoId) return alert("Selecione um serviço primeiro!");

            let s = servicosBase.find(x => x.id === selecionadoId);
            let nomeFinal = s.nome;
            let valorBase = 0; let qtd = 1; let valorUnit = 0;

            if(selecionadoId === 'outro') {
                nomeFinal = document.getElementById('input-nome-servico').value || 'Serviço Extra';
            }

            if (selecionadoId === 'convidados') {
                qtd = parseInt(document.getElementById('input-qtd-convidados').value);
                valorUnit = parseFloat(document.getElementById('input-valor-convidado').value);
                if(!qtd || !valorUnit) return alert("Preencha a quantidade e o valor por convidado/unidade!");
                valorBase = qtd * valorUnit;
            } else {
                valorBase = parseFloat(document.getElementById('valor-input').value);
                valorUnit = valorBase;
                if(!valorBase) return alert("Preencha o valor do serviço!");
            }

            let valorFinal = modo === 'parcelado' ? valorBase * (1 + ((juros/100) * vezes)) : valorBase;
            let valorParcela = modo === 'parcelado' ? valorFinal / vezes : valorFinal;

            orcamento.push({ id: selecionadoId, nome: nomeFinal, valorUnit, qtd, valorFinal, vezes, modo, juros, valorParcela });

            selecionadoId = null;
            document.getElementById('valor-input').value = '';
            document.getElementById('input-valor-convidado').value = '';
            document.getElementById('input-nome-servico').value = '';
            document.getElementById('container-nome-servico').classList.add('hidden');
            document.getElementById('container-convidados').classList.add('hidden');
            document.getElementById('container-valor-padrao').classList.remove('hidden'); 

            atualizarUI();
            renderGrid();
            showToast("Item adicionado!");
        }

        function removerItem(index) {
            orcamento.splice(index, 1);
            atualizarUI();
            renderGrid();
        }

        function editarItem(index) {
            const item = orcamento[index];
            setServico(item.id); 

            if(item.id === 'convidados') {
                document.getElementById('input-qtd-convidados').value = item.qtd;
                document.getElementById('input-valor-convidado').value = item.valorUnit;
            } else {
                document.getElementById('valor-input').value = item.valorUnit;
            }

            if(item.id === 'outro') {
                document.getElementById('input-nome-servico').value = item.nome;
            }

            document.getElementById('select-pagamento').value = item.modo;
            toggleParcelas();

            if(item.modo === 'parcelado') {
                document.getElementById('qtd-parcelas').value = item.vezes;
                document.getElementById('input-juros').value = item.juros;
            }

            removerItem(index);
            showToast("Modo Edição Ativado");
        }

        function calcularSaldo() {
            const budget = parseFloat(document.getElementById('input-orcamento-cliente').value) || 0;
            const display = document.getElementById('saldo-display');
            if (budget > 0) {
                display.classList.remove('hidden');
                const diferenca = budget - totalAtual;
                if (diferenca >= 0) {
                    display.className = 'mt-4 text-sm md:text-base font-bold p-3 md:p-4 rounded-xl bg-green-500/20 text-green-400 border border-green-500/30 text-center transition-all shadow-inner';
                    display.innerText = `✅ Budget Livre: R$ ${diferenca.toLocaleString('pt-BR', {minimumFractionDigits: 2})}`;
                } else {
                    display.className = 'mt-4 text-sm md:text-base font-bold p-3 md:p-4 rounded-xl bg-red-500/20 text-red-400 border border-red-500/30 text-center transition-all shadow-inner';
                    display.innerText = `⚠️ Extrapolou em: R$ ${Math.abs(diferenca).toLocaleString('pt-BR', {minimumFractionDigits: 2})}`;
                }
            } else { display.classList.add('hidden'); }
        }

        function atualizarUI() {
            const lista = document.getElementById('lista-real');
            totalAtual = 0;

            if(orcamento.length === 0) {
                lista.innerHTML = `
                    <div class="text-center py-10 opacity-60">
                        <span class="text-5xl block mb-3">📋</span>
                        <p class="text-gray-500 font-medium">Nenhum serviço adicionado ainda.</p>
                        <p class="text-xs text-gray-400 mt-1">Os itens aparecerão aqui.</p>
                    </div>`;
                document.getElementById('btn-pdf').classList.add('hidden');
            } else {
                document.getElementById('btn-pdf').classList.remove('hidden');
                lista.innerHTML = orcamento.map((item, idx) => {
                    totalAtual += item.valorFinal;
                    let txtDetalhe = item.id === 'convidados' ? `${item.qtd}x R$ ${item.valorUnit.toLocaleString('pt-BR', {minimumFractionDigits: 2})} | ` : '';
                    if (item.modo === 'avista') txtDetalhe += 'Pagamento à vista';
                    else txtDetalhe += `${item.vezes}x de R$ ${item.valorParcela.toLocaleString('pt-BR', {minimumFractionDigits: 2})} (${item.juros}% a.m.)`;

                    return `<div class="bg-gray-50 p-4 md:p-5 rounded-2xl border-l-4 border-amber-500 flex justify-between items-center group transition-all hover:shadow-md hover:bg-white border-y border-r border-gray-100">
                                <div><p class="font-bold text-sm md:text-base text-gray-800">${item.nome}</p>
                                <p class="text-[11px] md:text-xs text-gray-500 mt-1 font-medium">${txtDetalhe}</p></div>
                                <div class="flex items-center gap-2 md:gap-4">
                                    <p class="font-bold text-amber-600 text-sm md:text-base bg-amber-50 px-3 py-1 rounded-lg">R$ ${item.valorFinal.toLocaleString('pt-BR', {minimumFractionDigits: 2})}</p>
                                    <button onclick="editarItem(${idx})" class="text-gray-400 hover:text-blue-500 transition-colors p-2 bg-white rounded-full shadow-sm hover:shadow" title="Editar">✎</button>
                                    <button onclick="removerItem(${idx})" class="text-gray-400 hover:text-red-500 transition-colors p-2 bg-white rounded-full shadow-sm hover:shadow" title="Remover">✕</button>
                                </div>
                            </div>`;
                }).join('');
            }
            document.getElementById('total-display').innerText = "R$ " + totalAtual.toLocaleString('pt-BR', {minimumFractionDigits: 2});
            document.getElementById('itens-count').innerText = orcamento.length === 1 ? "1 serviço incluso" : orcamento.length + " serviços inclusos";

            calcularSaldo();
            salvarSessao();
        }

        function showToast(msg) {
            const t = document.getElementById('toast');
            t.innerText = "✅ " + msg;
            t.style.display = 'block'; setTimeout(() => t.style.display = 'none', 3000);
        }

        function gerarPDF() {
            const { jsPDF } = window.jspdf;
            const doc = new jsPDF();
            const nomeE = document.getElementById('display-titulo').innerText;
            const tipoE = document.getElementById('display-sub').innerText;
            const budget = parseFloat(document.getElementById('input-orcamento-cliente').value) || 0;

            doc.setFillColor(30, 41, 59); doc.rect(0, 0, 210, 40, 'F');
            doc.setTextColor(212, 160, 23); doc.setFontSize(22); doc.text("EVENTMASTER PRO", 20, 25);
            doc.setTextColor(255, 255, 255); doc.setFontSize(10); doc.text(`PROPOSTA: ${nomeE} | ${tipoE.toUpperCase()}`, 20, 33);

            const rows = orcamento.map(i => {
                let txtCalc = i.id === 'convidados' ? `${i.qtd}x R$ ${i.valorUnit.toLocaleString('pt-BR', {minimumFractionDigits: 2})} ` : '';
                txtCalc += i.modo === 'avista' ? '(À vista)' : `| ${i.vezes}x de R$ ${i.valorParcela.toLocaleString('pt-BR', {minimumFractionDigits: 2})} (juros ${i.juros}%)`;
                return [i.nome, txtCalc, `R$ ${i.valorFinal.toLocaleString('pt-BR', {minimumFractionDigits: 2})}`];
            });

            doc.autoTable({ 
                startY: 50, 
                head: [['Serviço', 'Condições e Cálculo', 'Total Final']], 
                body: rows, 
                headStyles: { fillColor: [212, 160, 23] },
                styles: { fontSize: 9, cellPadding: 4 },
                alternateRowStyles: { fillColor: [250, 250, 250] }
            });

            let finalY = doc.lastAutoTable.finalY + 15;
            doc.setFontSize(14); doc.setTextColor(30, 41, 59);
            doc.text(`TOTAL DA PROPOSTA: ${document.getElementById('total-display').innerText}`, 20, finalY);

            if(budget > 0) {
                finalY += 10;
                doc.setFontSize(11);
                doc.text(`Budget Inicial do Cliente: R$ ${budget.toLocaleString('pt-BR', {minimumFractionDigits: 2})}`, 20, finalY);
                finalY += 7;
                const diferenca = budget - totalAtual;
                if(diferenca >= 0) {
                    doc.setTextColor(0, 150, 0);
                    doc.text(`Saldo Restante: R$ ${diferenca.toLocaleString('pt-BR', {minimumFractionDigits: 2})} (Dentro do Orçamento)`, 20, finalY);
                } else {
                    doc.setTextColor(200, 0, 0);
                    doc.text(`Valor Excedente: R$ ${Math.abs(diferenca).toLocaleString('pt-BR', {minimumFractionDigits: 2})} (Acima do Orçamento)`, 20, finalY);
                }
            }

            doc.save(`Proposta_${nomeE.replace(/ /g, '_')}.pdf`);
        }
    </script>
</body>
</html>
"""

components.html(html_final, height=1200, scrolling=True)