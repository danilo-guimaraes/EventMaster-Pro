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
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>EventMaster Pro — Planejamento de Casamento</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.5.29/jspdf.plugin.autotable.min.js"></script>

  <style>

/* ========================================
   PREMIUM WEDDING PLANNER - DESIGN 2025
   ======================================== */

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400&family=Montserrat:wght@300;400;500;600;700&family=Great+Vibes&display=swap');

/* CSS Variables */
:root {
  --burgundy: #6B1D2E;
  --burgundy-light: #8B2D3E;
  --burgundy-deep: #4A0F1E;
  --gold: #C9A84C;
  --gold-light: #E8C97A;
  --gold-pale: #F5E6C0;
  --champagne: #F8F0E3;
  --cream: #FDF8F3;
  --ivory: #FFFEF9;
  --charcoal: #2C2C2C;
  --warm-gray: #8B7D7D;
  --rose-blush: #F4E4E4;
  --soft-pink: #E8C5C5;
  --glass-bg: rgba(255,255,255,0.12);
  --glass-border: rgba(255,255,255,0.25);
  --shadow-luxury: 0 25px 60px rgba(107,29,46,0.25);
  --shadow-card: 0 8px 32px rgba(107,29,46,0.12);
  --shadow-gold: 0 4px 20px rgba(201,168,76,0.35);
  --radius-lg: 20px;
  --radius-xl: 28px;
  --radius-card: 16px;
  --transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
}

/* ---- Reset & Base ---- */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body {
  font-family: 'Montserrat', sans-serif;
  background: var(--cream);
  color: var(--charcoal);
  min-height: 100vh;
  -webkit-font-smoothing: antialiased;
}

/* ========================================
   LOGIN SCREEN - PREMIUM HERO
   ======================================== */
#login-screen {
  min-height: 100vh;
  background:
    linear-gradient(135deg, rgba(74,15,30,0.88) 0%, rgba(107,29,46,0.78) 45%, rgba(44,12,20,0.92) 100%),
    url('https://images.unsplash.com/photo-1519741497674-611481863552?w=1600&q=80&fm=jpg') center/cover no-repeat;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  position: relative;
  overflow: hidden;
}

#login-screen::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 30% 50%, rgba(201,168,76,0.15) 0%, transparent 60%),
              radial-gradient(ellipse at 70% 20%, rgba(201,168,76,0.10) 0%, transparent 50%);
  pointer-events: none;
}

/* Decorative floating petals */
#login-screen::after {
  content: '✦';
  position: absolute;
  top: 12%;
  right: 8%;
  font-size: 80px;
  color: rgba(201,168,76,0.15);
  pointer-events: none;
  animation: floatStar 6s ease-in-out infinite;
}

@keyframes floatStar {
  0%, 100% { transform: translateY(0) rotate(0deg); opacity: 0.15; }
  50% { transform: translateY(-15px) rotate(15deg); opacity: 0.25; }
}

#login-card {
  background: rgba(255,255,255,0.10);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  border: 1px solid rgba(255,255,255,0.22);
  border-radius: var(--radius-xl);
  padding: 56px 48px;
  max-width: 440px;
  width: 100%;
  text-align: center;
  box-shadow: 0 30px 80px rgba(0,0,0,0.45), inset 0 1px 0 rgba(255,255,255,0.15);
  position: relative;
  animation: slideUpFade 0.8s cubic-bezier(0.4,0,0.2,1) both;
}

@keyframes slideUpFade {
  from { opacity: 0; transform: translateY(40px); }
  to { opacity: 1; transform: translateY(0); }
}

#login-card::before {
  content: '';
  position: absolute;
  top: 0; left: 50%; transform: translateX(-50%);
  width: 80%; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(201,168,76,0.6), transparent);
}

.login-logo {
  font-size: 60px;
  margin-bottom: 8px;
  filter: drop-shadow(0 4px 12px rgba(201,168,76,0.5));
}

.login-brand {
  font-family: 'Great Vibes', cursive;
  font-size: 42px;
  color: var(--gold-light);
  margin-bottom: 4px;
  text-shadow: 0 2px 20px rgba(201,168,76,0.4);
  line-height: 1.1;
}

.login-tagline {
  font-family: 'Montserrat', sans-serif;
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 4px;
  text-transform: uppercase;
  color: rgba(255,255,255,0.55);
  margin-bottom: 40px;
}

.login-divider {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 28px;
}
.login-divider::before, .login-divider::after {
  content: '';
  flex: 1;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(201,168,76,0.4));
}
.login-divider::after {
  background: linear-gradient(90deg, rgba(201,168,76,0.4), transparent);
}
.login-divider span {
  font-size: 18px;
  color: rgba(201,168,76,0.7);
}

.login-label {
  display: block;
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: rgba(255,255,255,0.65);
  margin-bottom: 10px;
  text-align: left;
}

#input-celular, #input-nome {
  width: 100%;
  padding: 16px 20px;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.18);
  border-radius: 12px;
  color: #1f2937 !important;
  font-family: 'Montserrat', sans-serif;
  font-size: 15px;
  font-weight: 400;
  outline: none;
  transition: var(--transition);
  margin-bottom: 16px;
}

#input-celular::placeholder, #input-nome::placeholder {
  color: rgba(31,41,55,0.45);
}

#input-celular:focus, #input-nome:focus {
  border-color: rgba(201,168,76,0.6);
  background: rgba(255,255,255,0.98);
  box-shadow: 0 0 0 3px rgba(201,168,76,0.15), 0 4px 20px rgba(0,0,0,0.2);
}

#input-nome {
  -webkit-text-fill-color: #1f2937;
  caret-color: #1f2937;
}

.btn-login {
  width: 100%;
  padding: 18px;
  background: linear-gradient(135deg, var(--gold) 0%, var(--gold-light) 50%, var(--gold) 100%);
  background-size: 200% auto;
  border: none;
  border-radius: 12px;
  color: var(--burgundy-deep);
  font-family: 'Montserrat', sans-serif;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  cursor: pointer;
  margin-top: 8px;
  transition: var(--transition);
  box-shadow: 0 8px 25px rgba(201,168,76,0.4);
}

.btn-login:hover {
  background-position: right center;
  transform: translateY(-2px);
  box-shadow: 0 12px 35px rgba(201,168,76,0.55);
}

.btn-login:active {
  transform: translateY(0);
}

.btn-secondary,
.btn-danger,
.btn-hero {
  border: 1px solid rgba(255,255,255,0.18) !important;
  border-radius: 14px !important;
  font-family: 'Montserrat', sans-serif !important;
  font-weight: 700 !important;
  letter-spacing: 1px !important;
  transition: var(--transition) !important;
  backdrop-filter: blur(12px) !important;
}

.btn-secondary {
  background: rgba(255,255,255,0.10) !important;
  color: #fff !important;
  box-shadow: 0 10px 30px rgba(44,12,20,0.18) !important;
}

.btn-secondary:hover {
  background: rgba(255,255,255,0.18) !important;
  transform: translateY(-1px) !important;
}

.btn-danger {
  background: rgba(168,42,64,0.16) !important;
  color: #fff !important;
  border-color: rgba(255,255,255,0.12) !important;
}

.btn-danger:hover {
  background: rgba(168,42,64,0.28) !important;
  transform: translateY(-1px) !important;
}

/* ========================================
   MAIN APP LAYOUT
   ======================================== */
#main-app {
  min-height: 100vh;
  background:
    linear-gradient(160deg, #FDF8F3 0%, #F8EEE8 40%, #F3E8E8 100%);
  position: relative;
}

#main-app::before {
  content: '';
  position: fixed;
  top: 0;
  right: 0;
  width: 45%;
  height: 100%;
  background:
    radial-gradient(ellipse at 80% 20%, rgba(107,29,46,0.06) 0%, transparent 60%),
    radial-gradient(ellipse at 90% 70%, rgba(201,168,76,0.05) 0%, transparent 50%);
  pointer-events: none;
  z-index: 0;
}

/* ========================================
   HEADER - LUXURY DESIGN
   ======================================== */
header, [id*="header"], .app-header, #main-app > div:first-child {
  background: linear-gradient(135deg, var(--burgundy-deep) 0%, var(--burgundy) 60%, var(--burgundy-light) 100%) !important;
  padding: 0 !important;
  border-bottom: 2px solid rgba(201,168,76,0.35) !important;
  box-shadow: 0 4px 30px rgba(74,15,30,0.35) !important;
}

/* Target the actual header div in body */
#main-app > div:first-child {
  background: linear-gradient(135deg, #2C0C14 0%, #6B1D2E 60%, #8B2D3E 100%);
  padding: 18px 32px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid rgba(201,168,76,0.3);
  box-shadow: 0 4px 30px rgba(44,12,20,0.4);
}

/* Header flex wrapper - style all headers generically */
.flex.items-center.justify-between.p-4.shadow-lg,
.bg-gray-900, [class*="bg-gray-9"] {
  background: linear-gradient(135deg, #2C0C14 0%, #6B1D2E 60%, #8B2D3E 100%) !important;
  border-bottom: 1px solid rgba(201,168,76,0.3) !important;
  box-shadow: 0 4px 30px rgba(44,12,20,0.4) !important;
}

/* Header text */
.flex.items-center.justify-between.p-4.shadow-lg h1,
.flex.items-center.justify-between.p-4.shadow-lg p,
[class*="bg-gray-9"] h1,
[class*="bg-gray-9"] p {
  color: #fff !important;
}

/* ---- Header Brand Pill ---- */
.bg-indigo-600, [class*="bg-indigo-"] {
  background: linear-gradient(135deg, var(--gold), var(--gold-light)) !important;
  color: var(--burgundy-deep) !important;
  font-weight: 700 !important;
  box-shadow: var(--shadow-gold) !important;
}

/* Header buttons */
button.text-white, .bg-gray-700, [class*="bg-gray-7"] {
  background: rgba(255,255,255,0.08) !important;
  border: 1px solid rgba(255,255,255,0.2) !important;
  color: #fff !important;
  border-radius: 10px !important;
  transition: var(--transition) !important;
  backdrop-filter: blur(8px) !important;
}

button.text-white:hover, .bg-gray-700:hover {
  background: rgba(201,168,76,0.2) !important;
  border-color: rgba(201,168,76,0.5) !important;
}

/* ========================================
   MAIN CONTENT LAYOUT
   ======================================== */
.flex.gap-6, .flex-1 {
  position: relative;
  z-index: 1;
}

/* ========================================
   LEFT PANEL - SERVICE SELECTION
   ======================================== */
.bg-white.rounded-2xl, [class*="rounded-2xl"][class*="bg-white"],
[class*="rounded-xl"][class*="bg-white"] {
  background: var(--ivory) !important;
  border-radius: var(--radius-lg) !important;
  box-shadow: var(--shadow-card) !important;
  border: 1px solid rgba(201,168,76,0.12) !important;
  overflow: hidden !important;
}

/* Section title inside left panel */
.text-lg.font-bold, h2[class*="font-bold"] {
  font-family: 'Cormorant Garamond', serif !important;
  font-size: 22px !important;
  font-weight: 600 !important;
  color: var(--burgundy) !important;
  letter-spacing: 0.5px !important;
}

/* ========================================
   SERVICE CATEGORY CARDS
   ======================================== */
.servico-card, [class*="servico-card"],
.cursor-pointer.rounded-xl.border, .cursor-pointer.border {
  background: var(--cream) !important;
  border: 2px solid transparent !important;
  border-radius: 16px !important;
  padding: 0 !important;
  text-align: center !important;
  cursor: pointer !important;
  transition: var(--transition) !important;
  position: relative !important;
  overflow: hidden !important;
  min-height: 220px !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: flex-end !important;
}

.servico-card::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(201,168,76,0.08), rgba(107,29,46,0.06));
  opacity: 0;
  transition: opacity 0.3s ease;
  border-radius: 16px;
}

.service-thumb {
  position: absolute;
  inset: 0 0 auto 0;
  height: 148px;
  background-size: cover;
  background-position: center;
  transform: scale(1.01);
}

.service-thumb::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(12,12,12,0.08) 0%, rgba(44,12,20,0.65) 100%);
}

.service-body {
  position: relative;
  z-index: 1;
  margin-top: auto;
  padding: 18px 16px 16px;
  text-align: left;
  background: linear-gradient(180deg, rgba(255,255,255,0.94) 0%, rgba(253,248,243,0.99) 100%);
}

.service-chip {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 10px;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(201,168,76,0.14);
  color: var(--burgundy);
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 1.2px;
  text-transform: uppercase;
}

.service-title {
  font-family: 'Cormorant Garamond', serif !important;
  font-size: 22px !important;
  font-weight: 700 !important;
  line-height: 1 !important;
  color: var(--burgundy-deep) !important;
}

.service-subtitle {
  font-size: 12px !important;
  font-weight: 500 !important;
  letter-spacing: 0.2px !important;
  color: var(--warm-gray) !important;
  text-transform: none !important;
}

.servico-card:hover::before { opacity: 1; }

.servico-card:hover, [data-tipo]:hover {
  background: linear-gradient(135deg, #FFF8EE, #FFF0F0) !important;
  border-color: var(--gold) !important;
  transform: translateY(-4px) scale(1.02) !important;
  box-shadow: 0 12px 35px rgba(201,168,76,0.25), 0 4px 15px rgba(107,29,46,0.1) !important;
}

.servico-card.selected, [data-tipo].selected,
.servico-card.ring-2, [class*="ring-indigo"] {
  background: linear-gradient(135deg, var(--gold-pale), #FFEEDD) !important;
  border-color: var(--gold) !important;
  box-shadow: 0 8px 25px rgba(201,168,76,0.3) !important;
}

.servico-card.selected .service-body {
  background: linear-gradient(180deg, rgba(255,248,238,0.98) 0%, rgba(255,241,225,0.99) 100%);
}

/* Service emoji/icon */
.servico-card .text-3xl, .text-3xl {
  font-size: 36px !important;
  display: block;
  margin-bottom: 8px;
  filter: drop-shadow(0 2px 6px rgba(0,0,0,0.1));
}

/* Service card label */
.servico-card .font-semibold, .servico-card span,
.text-sm.font-semibold {
  font-family: 'Montserrat', sans-serif !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  letter-spacing: 1px !important;
  text-transform: uppercase !important;
  color: var(--warm-gray) !important;
}

.servico-card:hover .text-sm.font-semibold,
.servico-card:hover span {
  color: var(--burgundy) !important;
}

/* ========================================
   FORM INPUTS - PREMIUM STYLE
   ======================================== */
input[type="text"], input[type="number"], input[type="tel"],
select, textarea,
#valor-input, #input-qtd-convidados, #input-valor-convidado,
#input-orcamento-cliente, #input-nome-servico, #input-outro-tipo {
  width: 100% !important;
  padding: 14px 18px !important;
  background: var(--ivory) !important;
  border: 1.5px solid rgba(201,168,76,0.25) !important;
  border-radius: 12px !important;
  font-family: 'Montserrat', sans-serif !important;
  font-size: 14px !important;
  font-weight: 400 !important;
  color: var(--charcoal) !important;
  outline: none !important;
  transition: var(--transition) !important;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04) !important;
}

input:focus, select:focus, textarea:focus {
  border-color: var(--gold) !important;
  background: #fff !important;
  box-shadow: 0 0 0 3px rgba(201,168,76,0.12), 0 4px 16px rgba(0,0,0,0.06) !important;
}

label, .text-sm.font-semibold.text-gray-700,
[class*="text-gray-7"] {
  font-family: 'Montserrat', sans-serif !important;
  font-size: 10px !important;
  font-weight: 700 !important;
  letter-spacing: 1.5px !important;
  text-transform: uppercase !important;
  color: var(--warm-gray) !important;
  margin-bottom: 6px !important;
}

/* ========================================
   ADD TO BUDGET BUTTON
   ======================================== */
.btn-primary, button[onclick*="adicionar"], button[onclick*="Adicionar"],
.bg-indigo-600.text-white, [class*="bg-indigo-"][class*="text-white"] {
  background: linear-gradient(135deg, var(--burgundy) 0%, var(--burgundy-light) 100%) !important;
  color: #fff !important;
  border: none !important;
  border-radius: 12px !important;
  padding: 15px 28px !important;
  font-family: 'Montserrat', sans-serif !important;
  font-size: 12px !important;
  font-weight: 700 !important;
  letter-spacing: 2px !important;
  text-transform: uppercase !important;
  cursor: pointer !important;
  transition: var(--transition) !important;
  box-shadow: 0 8px 25px rgba(107,29,46,0.35) !important;
  position: relative !important;
  overflow: hidden !important;
}

.btn-primary::before {
  content: '';
  position: absolute;
  top: 0; left: -100%;
  width: 100%; height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.15), transparent);
  transition: left 0.5s ease;
}

.btn-primary:hover::before { left: 100%; }

.btn-primary:hover, button[onclick*="adicionar"]:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 12px 35px rgba(107,29,46,0.45) !important;
  background: linear-gradient(135deg, var(--burgundy-light) 0%, #A0384A 100%) !important;
}

/* ========================================
   RIGHT PANEL - BUDGET SIDEBAR
   ======================================== */
.w-80, .w-96, aside, [id*="sidebar"],
.bg-gray-900.text-white, [class*="bg-gray-9"][class*="text-white"] {
  border-radius: var(--radius-lg) !important;
  overflow: hidden !important;
}

/* Budget total header */
.bg-gradient-to-br, [class*="bg-gradient"] {
  background: linear-gradient(160deg, var(--burgundy-deep) 0%, var(--burgundy) 70%, #7A2235 100%) !important;
  padding: 32px 24px !important;
  position: relative !important;
  overflow: hidden !important;
}

.bg-gradient-to-br::before {
  content: '';
  position: absolute;
  bottom: -20px; right: -20px;
  width: 120px; height: 120px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(201,168,76,0.25), transparent 70%);
  pointer-events: none;
}

/* Total amount text */
.text-4xl.font-bold, [class*="text-4xl"] {
  font-family: 'Cormorant Garamond', serif !important;
  font-size: 40px !important;
  font-weight: 700 !important;
  color: #fff !important;
  letter-spacing: -0.5px !important;
}

.text-sm.text-gray-300, .text-xs.text-gray-400 {
  font-size: 10px !important;
  letter-spacing: 2px !important;
  text-transform: uppercase !important;
  color: rgba(255,255,255,0.55) !important;
}

/* Budget input area */
.p-4 input, #input-orcamento-cliente {
  background: rgba(255,255,255,0.12) !important;
  border: 1px solid rgba(255,255,255,0.2) !important;
  color: #fff !important;
  border-radius: 10px !important;
}

#input-orcamento-cliente::placeholder {
  color: rgba(255,255,255,0.4) !important;
}

#input-orcamento-cliente:focus {
  border-color: rgba(201,168,76,0.6) !important;
  background: rgba(255,255,255,0.15) !important;
  box-shadow: 0 0 0 2px rgba(201,168,76,0.2) !important;
}

/* Saldo display */
#saldo-display {
  font-family: 'Cormorant Garamond', serif !important;
  font-weight: 700 !important;
  font-size: 18px !important;
}

/* ========================================
   ITEMS LIST - ITENS INCLUSOS
   ======================================== */
#lista-real {
  max-height: 320px;
  overflow-y: auto;
  scrollbar-width: thin;
  scrollbar-color: var(--gold) transparent;
}

/* Each item in budget list */
.border-b.border-gray-100 {
  border-bottom: 1px solid rgba(201,168,76,0.12) !important;
  padding: 14px 0 !important;
  transition: var(--transition) !important;
}

.border-b.border-gray-100:hover {
  background: rgba(201,168,76,0.05) !important;
  padding-left: 8px !important;
  border-radius: 8px !important;
}

/* Item name */
.font-medium.text-gray-800 {
  font-family: 'Montserrat', sans-serif !important;
  font-weight: 600 !important;
  font-size: 13px !important;
  color: var(--charcoal) !important;
}

/* Item price */
.text-green-600, .font-bold.text-green-600 {
  color: var(--burgundy) !important;
  font-weight: 700 !important;
  font-family: 'Cormorant Garamond', serif !important;
  font-size: 16px !important;
}

/* Edit/Delete item buttons */
.text-blue-500, .text-red-500 {
  border-radius: 6px !important;
  padding: 4px 8px !important;
  transition: var(--transition) !important;
}

.text-blue-500:hover {
  background: rgba(201,168,76,0.15) !important;
  color: var(--gold) !important;
}

.text-red-500:hover {
  background: rgba(107,29,46,0.1) !important;
  color: var(--burgundy) !important;
}

/* Itens Inclusos header */
.font-semibold.text-gray-800, [class*="font-semibold"][class*="text-gray"] {
  font-family: 'Cormorant Garamond', serif !important;
  font-size: 18px !important;
  color: var(--charcoal) !important;
}

/* Empty state */
.text-center.py-8 {
  padding: 40px !important;
}

.text-gray-400 {
  color: rgba(107,29,46,0.3) !important;
}

/* ========================================
   PDF BUTTON
   ======================================== */
button[onclick*="gerarPDF"], .bg-green-600,
[class*="bg-green-"] {
  background: linear-gradient(135deg, var(--gold) 0%, var(--gold-light) 50%, #B8941E 100%) !important;
  background-size: 200% auto !important;
  color: var(--burgundy-deep) !important;
  border: none !important;
  border-radius: 12px !important;
  padding: 16px 24px !important;
  font-family: 'Montserrat', sans-serif !important;
  font-size: 12px !important;
  font-weight: 700 !important;
  letter-spacing: 2px !important;
  text-transform: uppercase !important;
  cursor: pointer !important;
  width: 100% !important;
  transition: var(--transition) !important;
  box-shadow: 0 8px 25px rgba(201,168,76,0.4) !important;
}

button[onclick*="gerarPDF"]:hover, .bg-green-600:hover {
  background-position: right center !important;
  transform: translateY(-2px) !important;
  box-shadow: 0 12px 35px rgba(201,168,76,0.55) !important;
}

/* ========================================
   TOAST NOTIFICATION
   ======================================== */
#toast {
  position: fixed !important;
  top: 24px !important;
  right: 24px !important;
  z-index: 9999 !important;
  padding: 16px 24px !important;
  border-radius: 14px !important;
  font-family: 'Montserrat', sans-serif !important;
  font-size: 13px !important;
  font-weight: 500 !important;
  backdrop-filter: blur(16px) !important;
  background: rgba(44,12,20,0.92) !important;
  color: #fff !important;
  border: 1px solid rgba(201,168,76,0.35) !important;
  box-shadow: 0 20px 60px rgba(0,0,0,0.35) !important;
  border-left: 4px solid var(--gold) !important;
  max-width: 340px !important;
}

/* ========================================
   CONFIG MODAL
   ======================================== */
#config-modal, .modal-backdrop {
  backdrop-filter: blur(10px) !important;
  background:
    linear-gradient(135deg, rgba(32, 9, 16, 0.82), rgba(74, 15, 30, 0.68)),
    url('https://images.unsplash.com/photo-1511795409834-ef04bbd61622?auto=format&fit=crop&w=1600&q=80') center/cover no-repeat !important;
}

.event-photo-card {
  border-radius: 20px;
  background: rgba(255,255,255,0.10);
  border: 1px solid rgba(255,255,255,0.10);
  backdrop-filter: blur(14px);
  padding: 16px;
}

.event-photo-frame {
  width: 100%;
  min-height: 220px;
  border-radius: 16px;
  background:
    linear-gradient(180deg, rgba(14,14,14,0.14), rgba(44,12,20,0.35)),
    url('https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=1200&q=80') center/cover no-repeat;
  border: 1px solid rgba(255,255,255,0.16);
  box-shadow: 0 14px 30px rgba(0,0,0,0.22);
}

.budget-summary-panel {
  background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(253,248,243,0.98)) !important;
  border: 1px solid rgba(201,168,76,0.16) !important;
  box-shadow: 0 18px 45px rgba(44,12,20,0.08) !important;
}

.budget-summary-badge {
  color: var(--burgundy) !important;
  background: rgba(201,168,76,0.10) !important;
  border: 1px solid rgba(201,168,76,0.12) !important;
}

.budget-summary-total {
  color: var(--burgundy-deep) !important;
}

.budget-summary-input {
  background: #fff !important;
  color: var(--charcoal) !important;
  border: 1px solid rgba(201,168,76,0.22) !important;
}

.budget-summary-input::placeholder {
  color: rgba(44,44,44,0.38) !important;
}

.budget-summary-input:focus {
  border-color: var(--gold) !important;
  box-shadow: 0 0 0 3px rgba(201,168,76,0.12), 0 4px 16px rgba(0,0,0,0.05) !important;
}

#input-orcamento-cliente {
  color: #1f2937 !important;
  -webkit-text-fill-color: #1f2937 !important;
  caret-color: #1f2937 !important;
}

#input-orcamento-cliente::placeholder {
  color: rgba(31,41,55,0.45) !important;
}

.modal-content, [class*="modal-content"],
.bg-white.rounded-2xl.shadow-2xl {
  background: var(--ivory) !important;
  border-radius: var(--radius-xl) !important;
  border: 1px solid rgba(201,168,76,0.15) !important;
  box-shadow: var(--shadow-luxury) !important;
}

/* ========================================
   SCROLLBAR CUSTOM
   ======================================== */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--gold); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--burgundy); }

/* ========================================
   PAYMENT CONDITION SELECT
   ======================================== */
#select-pagamento {
  appearance: none !important;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%23C9A84C' stroke-width='2' fill='none' stroke-linecap='round'/%3E%3C/svg%3E") !important;
  background-repeat: no-repeat !important;
  background-position: right 16px center !important;
  padding-right: 40px !important;
}

/* ========================================
   QUANTITY DISPLAY
   ======================================== */
#itens-count {
  background: linear-gradient(135deg, var(--burgundy), var(--burgundy-light)) !important;
  color: #fff !important;
  border-radius: 20px !important;
  padding: 2px 10px !important;
  font-size: 11px !important;
  font-weight: 700 !important;
}

/* ========================================
   SECTION HEADERS
   ======================================== */
.bg-white.rounded-2xl > div:first-child,
.card-header {
  border-bottom: 1px solid rgba(201,168,76,0.12);
  padding-bottom: 16px;
  margin-bottom: 20px;
}

.hero-panel {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 28px;
  margin: 0 0 24px;
  padding: 28px;
  border-radius: 32px;
  background:
    linear-gradient(135deg, rgba(44,12,20,0.94) 0%, rgba(107,29,46,0.92) 55%, rgba(139,45,62,0.92) 100%),
    url('https://images.unsplash.com/photo-1529634806980-85c3dd6d34ac?auto=format&fit=crop&w=1600&q=80') center/cover no-repeat;
  box-shadow: 0 24px 70px rgba(44,12,20,0.22);
  overflow: hidden;
  position: relative;
}

.hero-panel::before,
.hero-panel::after {
  content: '';
  position: absolute;
  inset: auto;
  border-radius: 50%;
  pointer-events: none;
}

.hero-panel::before {
  width: 220px;
  height: 220px;
  right: -40px;
  top: -60px;
  background: radial-gradient(circle, rgba(201,168,76,0.22) 0%, transparent 70%);
}

.hero-panel::after {
  width: 280px;
  height: 280px;
  left: -80px;
  bottom: -120px;
  background: radial-gradient(circle, rgba(255,255,255,0.08) 0%, transparent 72%);
}

.hero-copy {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 18px;
  color: #fff;
}

.hero-kicker {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  align-self: flex-start;
  padding: 8px 14px;
  border-radius: 999px;
  background: rgba(255,255,255,0.12);
  border: 1px solid rgba(255,255,255,0.12);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
}

.hero-copy h2 {
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(32px, 4.2vw, 58px);
  line-height: 0.95;
  letter-spacing: -0.8px;
  margin: 0;
  max-width: 12ch;
}

.hero-copy p {
  max-width: 58ch;
  font-size: 15px;
  line-height: 1.7;
  color: rgba(255,255,255,0.82);
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 6px;
}

.hero-actions .btn-hero,
.hero-actions .btn-secondary {
  padding: 14px 18px !important;
}

.hero-stats {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 12px;
  margin-top: 8px;
}

.hero-stat {
  padding: 14px 14px 16px;
  border-radius: 18px;
  background: rgba(255,255,255,0.10);
  border: 1px solid rgba(255,255,255,0.10);
  backdrop-filter: blur(12px);
}

.hero-stat strong {
  display: block;
  font-family: 'Cormorant Garamond', serif;
  font-size: 28px;
  line-height: 1;
  margin-bottom: 4px;
  color: var(--gold-light);
}

.hero-stat span {
  font-size: 10px;
  letter-spacing: 1.8px;
  text-transform: uppercase;
  color: rgba(255,255,255,0.68);
}

.hero-visual {
  position: relative;
  z-index: 1;
  display: flex;
  justify-content: flex-end;
  align-items: stretch;
}

.hero-image-main {
  width: min(100%, 430px);
  min-height: 340px;
  aspect-ratio: 4 / 5;
  border-radius: 24px;
  background-size: cover;
  background-position: center 42%;
  box-shadow: 0 16px 40px rgba(0,0,0,0.22);
  background-image: linear-gradient(180deg, rgba(14,14,14,0.06), rgba(14,14,14,0.30)), url('https://images.unsplash.com/photo-1478146896981-b80fe463b330?auto=format&fit=crop&w=1800&q=80');
}

.hero-image-main {
  position: relative;
  overflow: hidden;
}

.hero-image-main::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(44,12,20,0.18));
}

.hero-photo-caption {
  position: absolute;
  left: 18px;
  right: 18px;
  bottom: 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 12px 14px;
  border-radius: 18px;
  background: rgba(255,255,255,0.16);
  border: 1px solid rgba(255,255,255,0.16);
  backdrop-filter: blur(14px);
  color: #fff;
}

.hero-photo-caption strong {
  font-size: 12px;
  letter-spacing: 1.4px;
  text-transform: uppercase;
}

.hero-photo-caption span {
  font-size: 12px;
  color: rgba(255,255,255,0.78);
}

.hero-photo-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--gold-light);
  box-shadow: 0 0 0 8px rgba(232,201,122,0.18);
  flex: 0 0 auto;
}

.app-icon,
.service-icon,
.action-icon,
.status-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  line-height: 1;
}

.app-icon,
.status-icon {
  font-size: 1.1rem;
}

.service-icon {
  font-size: 1.4rem;
  color: var(--burgundy-deep);
}

.action-icon {
  font-size: 0.95rem;
}

.budget-item-card {
  display: flex;
  align-items: stretch;
  gap: 14px;
  padding: 14px;
  border-radius: 22px;
  background: linear-gradient(180deg, rgba(255,255,255,0.95), rgba(252,248,243,0.98));
  border: 1px solid rgba(201,168,76,0.12);
  box-shadow: 0 12px 24px rgba(44,12,20,0.06);
}

.budget-item-visual {
  flex: 0 0 96px;
  border-radius: 18px;
  background-size: cover;
  background-position: center;
  position: relative;
  overflow: hidden;
  min-height: 96px;
}

.budget-item-visual::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(14,14,14,0.05), rgba(44,12,20,0.30));
}

.budget-item-emoji {
  position: absolute;
  left: 12px;
  bottom: 10px;
  z-index: 1;
  font-size: 18px;
  width: 34px;
  height: 34px;
  border-radius: 999px;
  background: rgba(255,255,255,0.92);
  color: var(--burgundy-deep);
  box-shadow: 0 8px 18px rgba(44,12,20,0.12);
}

.budget-item-content {
  flex: 1;
  min-width: 0;
}

.budget-item-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: 22px;
  font-weight: 700;
  color: var(--burgundy-deep);
  line-height: 1;
  margin-bottom: 6px;
}

.budget-item-meta {
  font-size: 12px;
  line-height: 1.5;
  color: var(--warm-gray);
}

.budget-item-actions {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-left: auto;
}

.budget-item-price {
  min-width: 114px;
  padding: 10px 12px;
  border-radius: 14px;
  background: linear-gradient(135deg, rgba(201,168,76,0.12), rgba(255,240,214,0.9));
  color: var(--burgundy-deep);
  font-weight: 800;
  text-align: center;
}

.icon-action {
  width: 38px;
  height: 38px;
  border: 0;
  border-radius: 12px;
  background: rgba(255,255,255,0.9);
  box-shadow: 0 10px 20px rgba(44,12,20,0.08);
  color: var(--charcoal);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: var(--transition);
}

.icon-action:hover {
  transform: translateY(-1px);
  box-shadow: 0 14px 24px rgba(44,12,20,0.12);
}

.icon-action.edit:hover {
  color: var(--burgundy);
}

.icon-action.remove:hover {
  color: #b4233a;
}

@media (max-width: 1100px) {
  .hero-panel {
    grid-template-columns: 1fr;
  }

  .hero-visual {
    justify-content: center;
  }

  .hero-image-main {
    width: min(100%, 640px);
    aspect-ratio: 16 / 10;
    min-height: 300px;
  }
}

/* ========================================
   LOADING CARD (INITIAL)
   ======================================== */
.animate-pulse, [class*="animate-pulse"] {
  background: linear-gradient(90deg, rgba(201,168,76,0.1) 25%, rgba(201,168,76,0.2) 50%, rgba(201,168,76,0.1) 75%) !important;
  background-size: 200% 100% !important;
  animation: shimmer 1.5s infinite !important;
}

@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

/* ========================================
   ANIMATION - PAGE ENTRY
   ======================================== */
#main-app {
  animation: fadeInPage 0.6s ease both;
}

@keyframes fadeInPage {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* ========================================
   RESPONSIVE POLISH
   ======================================== */
@media (max-width: 768px) {
  #login-card { padding: 40px 28px; }
  .login-brand { font-size: 34px; }
  .hero-panel { padding: 22px; }
  .hero-stats { grid-template-columns: 1fr; }
  .hero-copy h2 { max-width: 100%; }
  .budget-item-card { flex-direction: column; }
  .budget-item-visual { flex-basis: auto; width: 100%; min-height: 160px; }
  .budget-item-actions { width: 100%; justify-content: flex-end; }
  .login-shell { grid-template-columns: 1fr; }
  .login-media { min-height: 220px; }
}

/* ========================================
   UTILITY OVERRIDES
   ======================================== */
.shadow-xl { box-shadow: var(--shadow-card) !important; }
.shadow-2xl { box-shadow: var(--shadow-luxury) !important; }
.rounded-2xl { border-radius: var(--radius-lg) !important; }
.rounded-xl { border-radius: var(--radius-card) !important; }

/* Background for main body */
body {
  background: linear-gradient(160deg, #FDF8F3 0%, #F8EEE8 50%, #F3E5E5 100%) !important;
}

/* Gap/padding tweaks for main layout */
.p-6 { padding: 28px !important; }
.p-4 { padding: 20px !important; }
.gap-6 { gap: 24px !important; }


  </style>
</head>
<body>


    <div id="toast" class="toast font-semibold shadow-xl border border-green-400"><i class="fa-solid fa-circle-check status-icon"></i> Sucesso!</div>

    <div id="config-modal" class="fixed inset-0 z-50 flex items-center justify-center modal-backdrop p-4">
      <div class="login-shell bg-white rounded-[2rem] overflow-hidden w-full max-w-5xl card-shadow grid grid-cols-1 lg:grid-cols-[1fr_1.05fr]">
        <div class="login-media relative min-h-[280px] lg:min-h-[620px] p-6 md:p-8 flex flex-col justify-between text-white" style="background: linear-gradient(135deg, rgba(44,12,20,0.78), rgba(107,29,46,0.55)), url('https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=1600&q=80') center/cover no-repeat;">
          <div class="flex items-center justify-between gap-3">
            <div class="inline-flex items-center gap-3 px-4 py-2 rounded-full bg-white/10 border border-white/10 backdrop-blur-md text-xs font-bold uppercase tracking-[0.2em]">
              <i class="fa-solid fa-star app-icon"></i>
              Acesso Premium
            </div>
            <div id="config-icon" class="w-14 h-14 rounded-2xl bg-white/10 border border-white/10 backdrop-blur-md flex items-center justify-center text-white text-2xl shadow-lg"><i class="fa-solid fa-heart app-icon"></i></div>
          </div>
          <div class="max-w-md">
            <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-black/20 border border-white/10 backdrop-blur-md text-[10px] font-bold uppercase tracking-[0.3em] text-white/80 mb-4">
              Casamento e eventos
            </div>
            <h2 class="font-display text-4xl md:text-5xl leading-[0.92] max-w-[12ch]">Imagens com atmosfera de evento real.</h2>
          </div>
          <div class="event-photo-card max-w-md shadow-2xl">
            <div class="flex items-center justify-between mb-4">
              <div>
                <p class="text-[10px] uppercase tracking-[0.35em] text-white/60 font-bold">Preview do evento</p>
                <h3 class="text-lg font-display text-white mt-1">Imagem temática</h3>
              </div>
              <div class="w-12 h-12 rounded-2xl bg-white/12 border border-white/10 flex items-center justify-center text-white text-xl">
                <i class="fa-regular fa-image"></i>
              </div>
            </div>
            <div id="login-event-photo" class="event-photo-frame"></div>
          </div>
        </div>
        <div class="login-form p-8 md:p-10 lg:p-12 bg-white flex flex-col justify-center">
          <div class="max-w-xl mx-auto w-full">
            <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-amber-50 text-amber-700 border border-amber-100 text-xs font-bold uppercase tracking-[0.2em] mb-5">
              <i class="fa-solid fa-shield-heart"></i>
              Área de acesso
            </div>
            <h2 class="font-display text-3xl md:text-4xl font-bold mb-3 text-gray-900">Acessar Orçamento</h2>
            <p id="modal-desc" class="text-sm md:text-base text-gray-500 mb-8">Seus dados ficam salvos no seu aparelho.</p>

            <div class="text-left space-y-4">
              <div id="container-celular">
                <label class="block text-sm font-bold text-gray-700 mb-2"><i class="fa-solid fa-phone action-icon"></i> Seu Celular (WhatsApp)</label>
                <input type="tel" id="input-celular" maxlength="15" class="w-full p-4 border-2 border-gray-200 rounded-2xl outline-none focus:border-amber-400 font-bold text-gray-800 transition-colors bg-white" placeholder="(21) 90000-0000">
              </div>

              <div class="grid md:grid-cols-2 gap-4">
                <input type="text" id="input-nome" class="w-full p-4 border-2 border-gray-200 rounded-2xl outline-none focus:border-amber-400 transition-colors" placeholder="Nome do Cliente/Evento">
                <select id="input-tipo" onchange="updateConfigUI()" class="w-full p-4 border-2 border-gray-200 rounded-2xl bg-white outline-none cursor-pointer">
                  <option value="Casamento">Casamento</option>
                  <option value="15 Anos">15 Anos</option>
                  <option value="Formatura">Formatura</option>
                  <option value="outro">Outro Evento...</option>
                </select>
              </div>
              <input type="text" id="input-outro-tipo" class="hidden w-full p-4 border-2 border-gray-200 rounded-2xl outline-none focus:border-amber-400" placeholder="Qual o tipo de festa?">

              <button id="btn-modal" onclick="iniciarApp()" class="w-full btn-primary p-4 mt-6 shadow-lg text-lg rounded-2xl">Entrar no Sistema →</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div id="main-app" class="hidden w-full max-w-[96%] mx-auto py-4 px-2 sm:px-4 lg:px-6">
        <header class="flex justify-between items-center mb-8 bg-white p-5 md:p-6 rounded-2xl shadow-sm border border-gray-100">
            <div class="flex items-center gap-4">
                <div id="header-icon" class="w-12 h-12 md:w-14 md:h-14 gradient-gold rounded-xl flex items-center justify-center text-2xl md:text-3xl text-white shadow-inner"><i class="fa-solid fa-gem app-icon"></i></div>
                <div>
                    <h1 id="display-titulo" class="font-display text-xl md:text-3xl font-bold text-gray-800">EventMaster Pro</h1>
                    <p id="display-sub" class="text-sm md:text-base text-gray-500 italic"></p>
                </div>
            </div>
            <div class="flex gap-2">
          <button onclick="abrirConfig()" class="btn-secondary p-2 md:px-5 hidden sm:flex items-center gap-2"><i class="fa-solid fa-gear action-icon"></i><span>Editar Título</span></button>
          <button onclick="sairSessao()" class="btn-danger p-2 md:px-5 flex items-center gap-2"><i class="fa-solid fa-right-from-bracket action-icon"></i> <span class="hidden sm:inline">Sair</span></button>
            </div>
        </header>

      <section class="hero-panel">
        <div class="hero-copy">
          <div class="hero-kicker">Planejamento de luxo</div>
          <h2>Orçamentos que parecem proposta de showroom.</h2>
          <p>Construa ofertas com imagens profissionais, leitura clara e botões mais elegantes para apresentar ao cliente com credibilidade.</p>
          <div class="hero-actions">
            <button onclick="document.getElementById('grid-servicos').scrollIntoView({behavior:'smooth', block:'start'})" class="btn-primary btn-hero px-5 py-4">Explorar serviços</button>
            <button onclick="abrirConfig()" class="btn-secondary px-5 py-4">Editar identidade</button>
          </div>
          <div class="hero-stats">
            <div class="hero-stat"><strong>8+</strong><span>Categorias premium</span></div>
            <div class="hero-stat"><strong>24</strong><span>Parcelas configuráveis</span></div>
            <div class="hero-stat"><strong>100%</strong><span>Visual profissional</span></div>
          </div>
        </div>
        <div class="hero-visual">
          <div class="hero-image-main"></div>
        </div>
      </section>

        <div class="grid lg:grid-cols-12 gap-6 xl:gap-10">

            <div class="lg:col-span-8 bg-white rounded-3xl p-6 md:p-10 card-shadow border border-gray-50">
                <h3 class="font-display text-2xl mb-8 text-amber-700 font-bold border-b border-gray-100 pb-4"><i class="fa-solid fa-list-check action-icon"></i> Adicionar Serviço</h3>

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
                          <option value="avista">À Vista</option>
                          <option value="parcelado">Parcelado</option>
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

                <div class="budget-summary-panel p-6 md:p-8 rounded-3xl relative overflow-hidden">
                    <div class="absolute -right-10 -top-10 opacity-10 text-9xl"><i class="fa-solid fa-wallet"></i></div>
                    <div class="text-center mb-6 relative z-10">
                    <p class="budget-summary-badge inline-flex items-center gap-2 text-xs font-bold uppercase tracking-widest mb-3 px-3 py-1 rounded-full">Resumo do orçamento</p>
                    <h2 id="total-display" class="budget-summary-total text-4xl md:text-5xl font-bold font-display">R$ 0,00</h2>
                    <p id="itens-count" class="text-gray-600 mt-3 text-sm font-medium">Nenhum serviço incluso</p>
                    </div>

                  <div class="pt-6 border-t border-[rgba(201,168,76,0.12)] relative z-10">
                    <label class="block text-xs font-bold text-gray-500 uppercase tracking-wider mb-3 text-center">Caixa Disponível do Cliente (R$):</label>
                    <input type="number" id="input-orcamento-cliente" oninput="calcularSaldo(); salvarSessao();" class="budget-summary-input w-full p-4 rounded-xl text-center text-xl font-bold transition-colors" placeholder="Ex: 50000">
                        <div id="saldo-display" class="mt-4 text-sm md:text-base font-bold hidden p-4 rounded-xl text-center transition-all shadow-inner"></div>
                    </div>

                    <button id="btn-pdf" onclick="gerarPDF()" class="hidden relative z-10 mt-8 w-full bg-gradient-to-r from-amber-600 to-amber-500 hover:from-amber-500 hover:to-amber-400 text-white p-4 rounded-xl font-bold text-sm transition-all flex items-center justify-center gap-2 shadow-lg hover:shadow-amber-500/25">
                        <i class="fa-solid fa-file-pdf text-lg"></i> GERAR PROPOSTA (PDF)
                    </button>
                </div>

                <div class="bg-white p-6 md:p-8 rounded-3xl card-shadow border border-gray-50 flex flex-col max-h-[600px]">
                    <h3 class="font-display text-xl font-bold mb-4 border-b border-gray-100 pb-4 text-gray-800 flex justify-between items-center">
                      <span><i class="fa-solid fa-box-archive action-icon"></i> Itens Inclusos</span>
                        <span class="text-xs font-normal text-gray-400 bg-gray-100 px-3 py-1 rounded-full">Atualizado agora</span>
                    </h3>
                    <div id="lista-real" class="space-y-3 overflow-y-auto pr-2 pb-2 flex-1"></div>
                </div>
            </div>
        </div>
    </div>

    <script>
        const servicosBase = [
            {id: 'convidados', nome: 'Convidados', iconClass: 'fa-solid fa-people-group'},
            {id: 'buffet', nome: 'Buffet Fixo', iconClass: 'fa-solid fa-utensils'},
            {id: 'salao', nome: 'Salão', iconClass: 'fa-solid fa-building'},
            {id: 'vestido', nome: 'Vestido', iconClass: 'fa-solid fa-gem'},
            {id: 'foto', nome: 'Fotógrafo', iconClass: 'fa-solid fa-camera'},
            {id: 'decor', nome: 'Decoração', iconClass: 'fa-solid fa-leaf'},
            {id: 'lembranca', nome: 'Lembranças', iconClass: 'fa-solid fa-gift'},
            {id: 'outro', nome: 'Outro', iconClass: 'fa-solid fa-sparkles'}
        ];

        const serviceAssets = {
          convidados: {
            image: 'https://images.unsplash.com/photo-1519671482749-fd09be7ccebf?auto=format&fit=crop&w=1400&q=80',
            badge: 'Recepção',
            subtitle: 'Planejamento por pessoa',
            iconClass: 'fa-solid fa-people-group'
          },
          buffet: {
            image: 'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?auto=format&fit=crop&w=1400&q=80',
            badge: 'Gastronomia',
            subtitle: 'Menus e experiências',
            iconClass: 'fa-solid fa-utensils'
          },
          salao: {
            image: 'https://images.unsplash.com/photo-1511795409834-ef04bbd61622?auto=format&fit=crop&w=1400&q=80',
            badge: 'Espaço',
            subtitle: 'Ambiente e estrutura',
            iconClass: 'fa-solid fa-building'
          },
          vestido: {
            image: 'https://images.unsplash.com/photo-1483985988355-763728e1935b?auto=format&fit=crop&w=1400&q=80',
            badge: 'Moda nupcial',
            subtitle: 'Alta-costura e estilo',
            iconClass: 'fa-solid fa-gem'
          },
          foto: {
            image: 'https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=1400&q=80',
            badge: 'Memórias',
            subtitle: 'Registro editorial',
            iconClass: 'fa-solid fa-camera'
          },
          decor: {
            image: 'https://images.unsplash.com/photo-1469371670807-013ccf25f16a?auto=format&fit=crop&w=1400&q=80',
            badge: 'Cenografia',
            subtitle: 'Florais e ambientação',
            iconClass: 'fa-solid fa-leaf'
          },
          lembranca: {
            image: 'https://images.unsplash.com/photo-1513885535751-8b9238bd345a?auto=format&fit=crop&w=1400&q=80',
            badge: 'Detalhes',
            subtitle: 'Lembranças e mimos',
            iconClass: 'fa-solid fa-gift'
          },
          outro: {
            image: 'https://images.unsplash.com/photo-1501386761578-eac5c94b800a?auto=format&fit=crop&w=1400&q=80',
            badge: 'Customizado',
            subtitle: 'Itens sob medida',
            iconClass: 'fa-solid fa-sparkles'
          }
        };

        function getServiceAsset(id) {
          return serviceAssets[id] || serviceAssets.outro;
        }

        function getEventIconMarkup(tipoRaw) {
          if (tipoRaw === 'outro' || tipoRaw.includes('Outro')) return '<i class="fa-solid fa-sparkles app-icon"></i>';
          if (tipoRaw.includes('Casamento')) return '<i class="fa-solid fa-gem app-icon"></i>';
          if (tipoRaw.includes('15 Anos')) return '<i class="fa-solid fa-crown app-icon"></i>';
          if (tipoRaw.includes('Formatura')) return '<i class="fa-solid fa-graduation-cap app-icon"></i>';
          return '<i class="fa-solid fa-heart app-icon"></i>';
        }

        function getEventTypeImage(tipoRaw) {
          if (tipoRaw && tipoRaw.includes('Casamento')) return 'https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=1200&q=80';
          if (tipoRaw && tipoRaw.includes('15 Anos')) return 'https://images.unsplash.com/photo-1522673607200-164d1b6ce486?auto=format&fit=crop&w=1200&q=80';
          if (tipoRaw && tipoRaw.includes('Formatura')) return 'https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=1200&q=80';
          return 'https://images.unsplash.com/photo-1492684223066-81342ee5ff30?auto=format&fit=crop&w=1200&q=80';
        }

        function updateLoginEventPhoto(tipoRaw) {
          const photo = document.getElementById('login-event-photo');
          if (!photo) return;
          const img = getEventTypeImage(tipoRaw || document.getElementById('input-tipo').value);
          photo.style.backgroundImage = `linear-gradient(180deg, rgba(14,14,14,0.14), rgba(44,12,20,0.35)), url('${img}')`;
        }

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

        updateLoginEventPhoto();

        function updateConfigUI() {
            const val = document.getElementById('input-tipo').value;
            const iconDiv = document.getElementById('config-icon');
            document.getElementById('input-outro-tipo').classList.toggle('hidden', val !== 'outro');
          iconDiv.innerHTML = getEventIconMarkup(val);
          updateLoginEventPhoto(val);
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
                if(celularRaw.length !== 11) return alert("Por favor, digite um celular válido com DDD (Ex: 21988887777).");
                telefoneLogado = celularRaw;

                const savedData = localStorage.getItem('em_data_' + telefoneLogado);
                const savedConfig = localStorage.getItem('em_config_' + telefoneLogado);

                if(savedData && savedConfig) {
                    orcamento = JSON.parse(savedData);
                    const cfg = JSON.parse(savedConfig);
                    document.getElementById('display-titulo').innerText = cfg.nome;
                    document.getElementById('display-sub').innerText = cfg.tipo;
                    document.getElementById('header-icon').innerHTML = getEventIconMarkup(cfg.tipo || 'Casamento');
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
          let tipoFinal = tipoRaw;
          let iconeFinal = getEventIconMarkup(tipoRaw);

          if(tipoRaw === 'outro') {
            tipoFinal = document.getElementById('input-outro-tipo').value || 'Evento Especial';
          }

            document.getElementById('display-titulo').innerText = nome;
            document.getElementById('display-sub').innerText = tipoFinal;
          document.getElementById('header-icon').innerHTML = iconeFinal;
        }

        function salvarSessao() {
            if(!telefoneLogado) return;
            const config = {
                nome: document.getElementById('display-titulo').innerText,
                tipo: document.getElementById('display-sub').innerText,
              icone: document.getElementById('header-icon').innerHTML,
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
            const asset = getServiceAsset(s.id);
            return `<div class="servico-card ${css}" onclick="${jaTem ? '' : `setServico('${s.id}')`}">
                  <div class="service-thumb" style="background-image:url('${asset.image}')"></div>
                  <div class="service-body">
                    <span class="service-chip">${asset.badge}</span>
                      <div class="service-icon"><i class="${asset.iconClass}"></i></div>
                    <div class="service-title">${s.nome}</div>
                    <div class="service-subtitle">${asset.subtitle}</div>
                  </div>
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
                  display.innerHTML = `<i class="fa-solid fa-circle-check status-icon"></i> Caixa Livre: R$ ${diferenca.toLocaleString('pt-BR', {minimumFractionDigits: 2})}`;
                } else {
                    display.className = 'mt-4 text-sm md:text-base font-bold p-3 md:p-4 rounded-xl bg-red-500/20 text-red-400 border border-red-500/30 text-center transition-all shadow-inner';
                  display.innerHTML = `<i class="fa-solid fa-triangle-exclamation status-icon"></i> Extrapolou em: R$ ${Math.abs(diferenca).toLocaleString('pt-BR', {minimumFractionDigits: 2})}`;
                }
            } else { display.classList.add('hidden'); }
        }

        function atualizarUI() {
            const lista = document.getElementById('lista-real');
            totalAtual = 0;

            if(orcamento.length === 0) {
                lista.innerHTML = `
                    <div class="text-center py-10 opacity-60">
                <div class="text-5xl block mb-3"><i class="fa-solid fa-clipboard-list"></i></div>
                        <p class="text-gray-500 font-medium">Nenhum serviço adicionado ainda.</p>
                        <p class="text-xs text-gray-400 mt-1">Os itens aparecerão aqui.</p>
                    </div>`;
                document.getElementById('btn-pdf').classList.add('hidden');
            } else {
                document.getElementById('btn-pdf').classList.remove('hidden');
                lista.innerHTML = orcamento.map((item, idx) => {
                const asset = getServiceAsset(item.id);
                    totalAtual += item.valorFinal;
                    let txtDetalhe = item.id === 'convidados' ? `${item.qtd}x R$ ${item.valorUnit.toLocaleString('pt-BR', {minimumFractionDigits: 2})} | ` : '';
                    if (item.modo === 'avista') txtDetalhe += 'Pagamento à vista';
                    else txtDetalhe += `${item.vezes}x de R$ ${item.valorParcela.toLocaleString('pt-BR', {minimumFractionDigits: 2})} (${item.juros}% a.m.)`;

                return `<div class="budget-item-card">
                      <div class="budget-item-visual" style="background-image:url('${asset.image}')">
                <span class="budget-item-emoji"><i class="${asset.iconClass}"></i></span>
                      </div>
                      <div class="budget-item-content">
                        <p class="budget-item-title">${item.nome}</p>
                        <p class="budget-item-meta">${txtDetalhe}</p>
                      </div>
                      <div class="budget-item-actions">
                        <div class="budget-item-price">R$ ${item.valorFinal.toLocaleString('pt-BR', {minimumFractionDigits: 2})}</div>
                <button onclick="editarItem(${idx})" class="icon-action edit" title="Editar"><i class="fa-solid fa-pen-to-square"></i></button>
                <button onclick="removerItem(${idx})" class="icon-action remove" title="Remover"><i class="fa-solid fa-trash"></i></button>
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
          t.innerHTML = '<i class="fa-solid fa-circle-check status-icon"></i> ' + msg;
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
                doc.text(`Caixa Inicial do Cliente: R$ ${budget.toLocaleString('pt-BR', {minimumFractionDigits: 2})}`, 20, finalY);
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