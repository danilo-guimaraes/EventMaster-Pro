import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="EventMaster Pro", layout="wide", initial_sidebar_state="collapsed")

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
        .btn-primary:hover { background: #b8860b; transform: translateY(-1px); }
        .servico-card { border: 2px solid #f1f5f9; transition: 0.2s; cursor: pointer; background: white; }
        .servico-card.selected { border-color: #d4a017; background: #fffcf0; border-width: 3px; }
        .servico-card.disabled { opacity: 0.4; cursor: not-allowed; background: #f8fafc; }
        .toast { position: fixed; top: 20px; right: 20px; background: #22c55e; color: white; padding: 12px 24px; border-radius: 12px; display: none; z-index: 1000; }
    </style>
</head>
<body>

    <div id="toast" class="toast font-semibold shadow-lg">✅ Sucesso!</div>

    <div id="config-modal" class="fixed inset-0 z-50 flex items-center justify-center modal-backdrop">
        <div class="bg-white rounded-3xl p-10 max-w-md w-full mx-4 card-shadow text-center">
            <div id="config-icon" class="w-16 h-16 gradient-gold rounded-full flex items-center justify-center mx-auto mb-6 text-white text-2xl shadow-lg">💍</div>
            <h2 class="font-display text-2xl font-bold mb-2">Configurar Evento</h2>
            <div class="text-left space-y-4 mt-6">
                <input type="text" id="input-nome" class="w-full p-4 border-2 border-gray-100 rounded-xl outline-none focus:border-amber-500" placeholder="Nome do Cliente/Evento">
                <select id="input-tipo" onchange="updateConfigUI()" class="w-full p-4 border-2 border-gray-100 rounded-xl bg-white outline-none">
                    <option value="💍 Casamento">💍 Casamento</option>
                    <option value="🎭 15 Anos">🎭 15 Anos</option>
                    <option value="🎓 Formatura">🎓 Formatura</option>
                    <option value="outro">✨ Outro Evento...</option>
                </select>
                <input type="text" id="input-outro-tipo" class="hidden w-full p-4 border-2 border-gray-100 rounded-xl outline-none focus:border-amber-500" placeholder="Qual o tipo de festa?">
                <button onclick="iniciarApp()" class="w-full btn-primary p-4 mt-4 shadow-lg">Salvar Configuração →</button>
            </div>
        </div>
    </div>

    <div id="main-app" class="hidden max-w-6xl mx-auto py-8 px-4">
        <header class="flex justify-between items-center mb-8 bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
            <div class="flex items-center gap-4">
                <div id="header-icon" class="w-12 h-12 gradient-gold rounded-xl flex items-center justify-center text-2xl text-white shadow-inner">💍</div>
                <div>
                    <h1 id="display-titulo" class="font-display text-2xl font-bold text-gray-800">EventMaster Pro</h1>
                    <p id="display-sub" class="text-sm text-gray-500 italic"></p>
                </div>
            </div>
            <button onclick="abrirConfig()" class="bg-gray-100 hover:bg-gray-200 p-2 px-4 rounded-xl font-bold text-gray-600 flex items-center gap-2 transition-all">⚙️ Editar Título</button>
        </header>

        <div class="grid lg:grid-cols-3 gap-8">
            <div class="lg:col-span-2 bg-white rounded-3xl p-8 card-shadow">
                <h3 class="font-display text-xl mb-6 text-amber-700 font-bold">📝 Adicionar Serviço</h3>

                <div id="grid-servicos" class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-8"></div>

                <div id="container-nome-servico" class="hidden mb-6 p-4 bg-amber-50 rounded-2xl border-2 border-amber-200">
                    <label class="block text-sm font-bold text-amber-800 mb-2">Qual o nome deste serviço?</label>
                    <input type="text" id="input-nome-servico" class="w-full p-4 border-2 border-white rounded-xl outline-none" placeholder="Ex: Segurança, Garçom...">
                </div>

                <div id="container-convidados" class="hidden grid md:grid-cols-2 gap-6 mb-8 p-4 bg-blue-50 rounded-2xl border-2 border-blue-200">
                    <div>
                        <label class="block text-sm font-bold text-blue-800 mb-2">Qtd de Convidados:</label>
                        <input type="number" id="input-qtd-convidados" class="w-full p-4 border-2 border-white rounded-xl outline-none" value="100" min="1">
                    </div>
                    <div>
                        <label class="block text-sm font-bold text-blue-800 mb-2">Valor por Cabeça (R$):</label>
                        <input type="number" id="input-valor-convidado" class="w-full p-4 border-2 border-white rounded-xl outline-none" placeholder="Ex: 80,00">
                    </div>
                </div>

                <div id="container-valor-padrao" class="mb-8">
                    <label class="block text-sm font-bold text-gray-700 mb-2">Valor Fixo do Serviço (R$):</label>
                    <input type="number" id="valor-input" class="w-full p-4 border-2 border-gray-100 rounded-xl text-xl outline-none focus:border-amber-500" placeholder="0,00">
                </div>

                <div class="grid md:grid-cols-3 gap-4 mb-8">
                    <div>
                        <label class="block text-sm font-bold text-gray-700 mb-2">Pagamento:</label>
                        <select id="select-pagamento" onchange="toggleParcelas()" class="w-full p-4 border-2 border-gray-100 rounded-xl bg-white outline-none">
                            <option value="avista">💵 À Vista</option>
                            <option value="parcelado">💳 Parcelado</option>
                        </select>
                    </div>
                    <div id="container-parcelas-1" class="hidden">
                        <label class="block text-sm font-bold text-gray-700 mb-2">Qtd Vezes:</label>
                        <select id="qtd-parcelas" class="w-full p-4 border-2 border-gray-100 rounded-xl bg-white outline-none"></select>
                    </div>
                    <div id="container-parcelas-2" class="hidden">
                        <label class="block text-sm font-bold text-gray-700 mb-2">Juros a.m. (%):</label>
                        <input type="number" id="input-juros" class="w-full p-4 border-2 border-gray-100 rounded-xl outline-none" value="2" step="0.1" min="0">
                    </div>
                </div>

                <button onclick="adicionarAoOrcamento()" class="w-full btn-primary p-5 text-lg shadow-lg">ADICIONAR AO ORÇAMENTO</button>
            </div>

            <div class="space-y-6">
                <div class="bg-slate-900 text-white p-8 rounded-3xl shadow-xl text-center border-b-8 border-amber-600">
                    <p class="text-gray-400 text-xs font-bold uppercase mb-2">Total Estimado</p>
                    <h2 id="total-display" class="text-4xl font-bold text-amber-500">R$ 0,00</h2>
                    <p id="itens-count" class="text-gray-500 mt-2 text-sm">Nenhum item</p>
                    <button id="btn-pdf" onclick="gerarPDF()" class="hidden mt-6 w-full bg-amber-600 hover:bg-amber-500 p-3 rounded-xl font-bold text-sm transition-all flex items-center justify-center gap-2">📥 BAIXAR PROPOSTA (PDF)</button>
                </div>

                <div class="bg-white p-6 rounded-3xl card-shadow min-h-[300px]">
                    <h3 class="font-display text-lg font-bold mb-4 border-b pb-2 text-gray-800">Itens Inclusos</h3>
                    <div id="lista-real" class="space-y-3"></div>
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

        function abrirConfig() { document.getElementById('config-modal').classList.remove('hidden'); }

        function iniciarApp() {
            const nome = document.getElementById('input-nome').value || 'Cliente Master';
            const tipoRaw = document.getElementById('input-tipo').value;
            let tipoFinal = tipoRaw;
            let iconeFinal = '💍';

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
            document.getElementById('config-modal').classList.add('hidden');
            document.getElementById('main-app').classList.remove('hidden');
            renderGrid();
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
                return `<div class="servico-card ${css} p-4 rounded-2xl text-center shadow-sm" onclick="${jaTem ? '' : `setServico('${s.id}')`}">
                            <span class="text-3xl block mb-1">${s.icon}</span>
                            <span class="text-xs font-bold text-gray-600">${s.nome}</span>
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
            let valorBase = 0;
            let qtd = 1;
            let valorUnit = 0;

            if(selecionadoId === 'outro') {
                nomeFinal = document.getElementById('input-nome-servico').value || 'Serviço Extra';
            }

            if (selecionadoId === 'convidados') {
                qtd = parseInt(document.getElementById('input-qtd-convidados').value);
                valorUnit = parseFloat(document.getElementById('input-valor-convidado').value);
                if(!qtd || !valorUnit) return alert("Preencha a quantidade e o valor por convidado!");
                valorBase = qtd * valorUnit;
            } else {
                valorBase = parseFloat(document.getElementById('valor-input').value);
                valorUnit = valorBase;
                if(!valorBase) return alert("Preencha o valor do serviço!");
            }

            // CALCULO DE JUROS E VALOR DA PARCELA
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
            showToast("Modo Edição");
        }

        function atualizarUI() {
            const lista = document.getElementById('lista-real');
            let total = 0;
            if(orcamento.length === 0) {
                lista.innerHTML = '<p class="text-gray-400 text-center py-4 italic text-sm">Sua lista está vazia</p>';
                document.getElementById('btn-pdf').classList.add('hidden');
            } else {
                document.getElementById('btn-pdf').classList.remove('hidden');
                lista.innerHTML = orcamento.map((item, idx) => {
                    total += item.valorFinal;
                    let txtDetalhe = item.id === 'convidados' ? `${item.qtd}x R$ ${item.valorUnit.toLocaleString('pt-BR', {minimumFractionDigits: 2})} | ` : '';

                    if (item.modo === 'avista') {
                        txtDetalhe += 'À vista';
                    } else {
                        txtDetalhe += `${item.vezes}x de R$ ${item.valorParcela.toLocaleString('pt-BR', {minimumFractionDigits: 2})} (${item.juros}% a.m.)`;
                    }

                    return `<div class="bg-gray-50 p-4 rounded-2xl border-l-4 border-amber-500 flex justify-between items-center group">
                                <div>
                                    <p class="font-bold text-sm text-gray-800">${item.nome}</p>
                                    <p class="text-[11px] text-gray-500 mt-1">${txtDetalhe}</p>
                                </div>
                                <div class="flex items-center gap-3">
                                    <p class="font-bold text-amber-600 text-sm">R$ ${item.valorFinal.toLocaleString('pt-BR', {minimumFractionDigits: 2})}</p>
                                    <button onclick="editarItem(${idx})" class="text-blue-400 hover:text-blue-600 transition-colors">✎</button>
                                    <button onclick="removerItem(${idx})" class="text-gray-300 hover:text-red-500 transition-colors">✕</button>
                                </div>
                            </div>`;
                }).join('');
            }
            document.getElementById('total-display').innerText = "R$ " + total.toLocaleString('pt-BR', {minimumFractionDigits: 2});
            document.getElementById('itens-count').innerText = orcamento.length + " serviços";
        }

        function showToast(msg) {
            const t = document.getElementById('toast');
            t.innerText = "✅ " + msg;
            t.style.display = 'block'; setTimeout(() => t.style.display = 'none', 2000);
        }

        function gerarPDF() {
            const { jsPDF } = window.jspdf;
            const doc = new jsPDF();
            const nomeE = document.getElementById('display-titulo').innerText;
            doc.setFillColor(30, 41, 59); doc.rect(0, 0, 210, 40, 'F');
            doc.setTextColor(212, 160, 23); doc.setFontSize(22); doc.text("EVENTMASTER PRO", 20, 25);
            doc.setTextColor(255, 255, 255); doc.setFontSize(10); doc.text(`PROPOSTA: ${nomeE}`, 20, 33);

            const rows = orcamento.map(i => {
                let txtCalc = i.id === 'convidados' ? `${i.qtd}x R$ ${i.valorUnit.toLocaleString('pt-BR', {minimumFractionDigits: 2})} ` : '';
                if (i.modo === 'avista') {
                    txtCalc += '(À vista)';
                } else {
                    txtCalc += `| ${i.vezes}x de R$ ${i.valorParcela.toLocaleString('pt-BR', {minimumFractionDigits: 2})} (juros ${i.juros}% a.m.)`;
                }
                return [i.nome, txtCalc, `R$ ${i.valorFinal.toLocaleString('pt-BR', {minimumFractionDigits: 2})}`];
            });

            doc.autoTable({ startY: 50, head: [['Serviço', 'Cálculo', 'Total']], body: rows, headStyles: { fillColor: [212, 160, 23] } });
            doc.setFontSize(16); doc.setTextColor(30, 41, 59);
            doc.text(`TOTAL FINAL: ${document.getElementById('total-display').innerText}`, 20, doc.lastAutoTable.finalY + 15);
            doc.save(`Orcamento_${nomeE.replace(/ /g, '_')}.pdf`);
        }
    </script>
</body>
</html>
"""

components.html(html_final, height=1000, scrolling=True)