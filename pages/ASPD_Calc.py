import streamlit as st
import math

def main():
    st.set_page_config(
        page_title="Attack Speed Calculator",
        page_icon="⚔️",
        layout="centered"
    )
    
    # CSS personalizado para melhorar a aparência
    st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #4CAF50;
        font-size: 2rem;
        margin-bottom: 2rem;
    }
    .result-box {
        background-color: #262730;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-top: 1rem;
    }
    .stSelectbox > div > div {
        background-color: #262730;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 class='main-title'>Calculadora de Atq Spd de EduardoZack</h1>", unsafe_allow_html=True)
    
    # Dados de lookup para diferentes tipos de hunter e armas
    lookup = {
        "berserker": {
            "ancient": {"spd": 2.00},
            "primal": {"spd": 2.00},
            "pvp": {"spd": 2.20},
            "pvpult": {"spd": 2.20},
            "wb": {"spd": 2.20}
        },
        "sorcerer": {
            "ancient": {"spd": 2.20},
            "primal": {"spd": 2.20},
            "pvp": {"spd": 2.30},
            "pvpult": {"spd": 2.30},
            "wb": {"spd": 2.30}
        },
        "ranger": {
            "ancient": {"spd": 1.80},
            "primal": {"spd": 1.80},
            "pvp": {"spd": 2.00},
            "pvpult": {"spd": 2.00},
            "wb": {"spd": 2.00}
        },
        "paladin": {
            "ancient": {"spd": 2.40},
            "primal": {"spd": 2.40},
            "pvp": {"spd": 2.50},
            "pvpult": {"spd": 2.50},
            "wb": {"spd": 2.50}
        }
    }
    
    # Interface do usuário com colunas
    col1, col2 = st.columns(2)
    
    with col1:
        # Seleção do tipo de hunter
        hunter_type = st.selectbox(
            "**Selecione o tipo de hunter:**",
            ["berserker", "sorcerer", "ranger", "paladin"],
            index=0
        )
        
        # Seleção do tipo de arma
        weapon_type = st.selectbox(
            "**Selecione o tipo de arma:**",
            ["pvp", "ancient"],
            format_func=lambda x: "PVP/World Boss" if x == "pvp" else "Ancient/Primal/Original"
        )
        
        # Fury
        fury_options = {
            "Level 13": 4.54,
            "Level 12": 4.36,
            "Level 11": 4.18,
            "Level 10": 4.00,
            "Level 1": 2.38,
            "Level 0": 0
        }
        fury_label = st.selectbox(
            "**Fury:** Berserkers podem ter level 1-13, Sorcerers podem ter level 1 usando Immortal",
            list(fury_options.keys()),
            index=5
        )
        fury = fury_options[fury_label]
        
        # Guild ATK SPD Buff
        guild = st.selectbox(
            "**Buff de ATK SPD da Guild:**",
            [0, 1, 2, 3, 4, 5],
            format_func=lambda x: f"{x}%"
        )
        
        # Secret Tech
        s_tech = st.number_input(
            "**ATK SPD % - Técnicas Secretas (Lv100:10%):**",
            min_value=0.0,
            max_value=10.0,
            value=10.0,
            step=0.1
        )
    
    with col2:
        # Equipment Bonus
        equip_bonus = st.number_input(
            "**% Bonus de Equipamento + % Runa de ATQ Spd:**",
            min_value=0.0,
            value=0.0,
            step=0.1
        )
        
        # Hunter Stat
        hunter_stat_options = {
            "White/Grey": 0,
            "Blue": 10,
            "Orange": 20,
            "Purple": 30
        }
        hunter_stat_label = st.selectbox(
            "**Cor do Status de ATQ SPD:**",
            list(hunter_stat_options.keys())
        )
        hunter_stat = hunter_stat_options[hunter_stat_label]
        
        # Hunter's Characteristic
        hunter_char_options = {
            "Other": 0,
            "Heroic": 7,
            "Swift": 10,
            "Thickheaded": -10
        }
        hunter_char_label = st.selectbox(
            "**Hunter's Characteristic:**",
            list(hunter_char_options.keys())
        )
        hunter_char = hunter_char_options[hunter_char_label]
        
        # Hunter's Quicken Trait
        hunter_quicken_options = {
            "0": 1,
            "1": 1.1,
            "2": 1.2,
            "3": 1.3,
            "4": 1.4,
            "5": 1.5
        }
        hunter_quicken_label = st.selectbox(
            "**Hunter's Quicken Trait:**",
            list(hunter_quicken_options.keys())
        )
        hunter_trait = hunter_quicken_options[hunter_quicken_label]
        
        # Mount Equip Tier
        mount_options = {
            "None": 0,
            "B (6%)": 6,
            "A (9%)": 9,
            "S (12%)": 12
        }
        mount_label = st.selectbox(
            "**Mount Equip Tier:**",
            list(mount_options.keys())
        )
        mount_bonus = mount_options[mount_label]
    
    # Cálculo da velocidade de ataque
    def calc_attack_speed():
        # Obter velocidade base da arma
        weapon_speed = lookup[hunter_type][weapon_type]['spd']
        
        # Cálculo dos steps
        step_1 = guild + s_tech + equip_bonus + hunter_stat + hunter_char + mount_bonus
        step_2 = step_1 / 100
        step_3 = 1 - step_2
        step_4 = weapon_speed * step_3
        
        # Velocidade de ataque sem fury
        atk_spd = round(step_4 / hunter_trait, 2)
        
        # Velocidade de ataque com fury
        atk_spd_fury = round(step_4 / (fury + (hunter_trait - 1)), 2) if fury > 0 else atk_spd
        
        # Cálculo do ATK SPD necessário para atingir 0.25
        total_atk_spd_needed_no_fury = 1 - (hunter_trait / (4 * weapon_speed))
        total_atk_spd_needed_with_fury = 1 - (((hunter_trait - 1) + fury) / (4 * weapon_speed))
        
        atk_spd_needed = total_atk_spd_needed_no_fury - step_2
        atk_spd_needed_with_fury = total_atk_spd_needed_with_fury - step_2
        
        return {
            'atk_spd': atk_spd,
            'atk_spd_fury': atk_spd_fury,
            'atk_spd_needed': atk_spd_needed * 100,
            'atk_spd_needed_with_fury': atk_spd_needed_with_fury * 100,
            'has_fury': fury > 0 and (hunter_type == "berserker" or hunter_type == "sorcerer")
        }
    
    # Calcular e exibir resultados
    results = calc_attack_speed()
    
    st.markdown("---")
    st.markdown("### 📊 Resultados:")
    
    # Exibir resultados
    if results['has_fury']:
        st.markdown(f"""
        <div class='result-box'>
        <strong>COM FURY:</strong> {results['atk_spd_fury']}<br>
        <em>{results['atk_spd_needed_with_fury']:.1f}% +ATKSPD% necessário para atingir 0.25 com fury</em><br><br>
        <strong>SEM FURY:</strong> {results['atk_spd']}<br>
        <em>{results['atk_spd_needed']:.1f}% +ATKSPD% necessário para atingir 0.25 sem fury</em>
        </div>
        """, unsafe_allow_html=True)
    elif results['atk_spd'] >= 0.25:
        st.markdown(f"""
        <div class='result-box'>
        <strong>Velocidade de Ataque:</strong> {results['atk_spd']}<br>
        <em>{results['atk_spd_needed']:.1f}% +ATKSPD% necessário para atingir 0.25</em>
        </div>
        """, unsafe_allow_html=True)
    else:
        excess = abs(results['atk_spd_needed'])
        st.markdown(f"""
        <div class='result-box'>
        <strong>⚠️ Considere remover {excess:.1f}% +ATKSPD%</strong><br>
        O máximo é 0.25 e você tem: {results['atk_spd']}
        </div>
        """, unsafe_allow_html=True)
    
    # Informações adicionais
    st.markdown("---")
    st.markdown("### ℹ️ Informações:")
    st.info("Esta calculadora ajuda a otimizar a velocidade de ataque do seu hunter baseado nas configurações e equipamentos selecionados.")

if __name__ == "__main__":
    main()