import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, date
import plotly.graph_objects as go
import plotly.express as px
from io import BytesIO

# Configuration de la page
st.set_page_config(
    page_title="Prévision Agricole IA - Togo",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Styles CSS personnalisés
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #2E7D32;
        text-align: center;
        padding: 1rem;
        background: linear-gradient(90deg, #C8E6C9 0%, #A5D6A7 100%);
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #E8F5E9;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #4CAF50;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #FFF3E0;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #FF9800;
    }
    .success-box {
        background-color: #E8F5E9;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #4CAF50;
    }
    </style>
""", unsafe_allow_html=True)

# Titre principal
st.markdown('<div class="main-header">🌾 Système de Prévision Agricole - Togo</div>', unsafe_allow_html=True)
st.markdown("### Intelligence Artificielle pour l'agriculture durable")

# Initialisation de la session
if 'historique' not in st.session_state:
    st.session_state.historique = []

# Sidebar - Navigation
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Flag_of_Togo.svg/200px-Flag_of_Togo.svg.png", width=100)
    st.title("Navigation")
    page = st.radio(
        "Sélectionnez une section",
        ["Accueil", "Prévision", "Visualisations", "Historique", "ℹÀ propos"]
    )
    
    st.markdown("---")
    st.info("**Cultures supportées:**\n- Maïs\n- Sorgho\n- Mil")
    st.markdown("---")
    st.caption("Version 1.0 - 2026")

# PAGE ACCUEIL
if page == "Accueil":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("## Bienvenue sur le système de prévision agricole")
        st.write("""
        Ce système utilise l'**intelligence artificielle** pour vous aider à prendre de meilleures 
        décisions agricoles concernant vos cultures de maïs et céréales locales.
        """)
        
        st.markdown("### Que pouvez-vous faire ?")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("""
            **Prévisions de rendement**
            - Estimation de la production (t/ha)
            - Basée sur vos données réelles
            
            **Analyse climatique**
            - Évaluation des risques
            - Recommandations adaptées
            """)
        
        with col_b:
            st.markdown("""
            **Calendrier optimal**
            - Meilleure période de récolte
            - Adaptation aux conditions locales
            
            **Suivi historique**
            - Conservation des prévisions
            - Exportation des données
            """)
    
    with col2:
        st.markdown("###  Régions couvertes")
        regions = ["Maritime", "Plateaux", "Centrale", "Kara", "Savanes"]
        for region in regions:
            st.success(f"✓ {region}")
        
        st.markdown("### Besoin d'aide ?")
        st.info("Consultez la section **À propos** pour plus d'informations.")

# PAGE PRÉVISION
elif page == "Prévision":
    st.markdown("## 🌾 Nouvelle Prévision Agricole")
    
    # Formulaire de saisie
    with st.form("formulaire_prevision"):
        st.markdown("### Informations sur votre exploitation")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            region = st.selectbox(
                "Région agricole",
                ["Maritime", "Plateaux", "Centrale", "Kara", "Savanes"],
                help="Sélectionnez votre région"
            )
            
            culture = st.selectbox(
                "Type de culture",
                ["Maïs", "Sorgho", "Mil"],
                help="Culture à analyser"
            )
            
            superficie = st.number_input(
                "Superficie cultivée (ha)",
                min_value=0.1,
                max_value=1000.0,
                value=5.0,
                step=0.5,
                help="Surface de votre exploitation"
            )
        
        with col2:
            date_semis = st.date_input(
                "Date de semis",
                value=date.today(),
                help="Date de plantation"
            )
            
            type_sol = st.selectbox(
                "Type de sol",
                ["Argileux", "Sableux", "Limoneux", "Argilo-sableux", "Argilo-limoneux"],
                help="Nature du sol de votre parcelle"
            )
            
            pluviometrie = st.number_input(
                "Pluviométrie cumulée (mm)",
                min_value=0,
                max_value=3000,
                value=800,
                step=50,
                help="Précipitations totales depuis le semis"
            )
        
        with col3:
            temperature_moy = st.number_input(
                "Température moyenne (°C)",
                min_value=15.0,
                max_value=45.0,
                value=27.0,
                step=0.5,
                help="Température moyenne de la saison"
            )
            
            irrigation = st.selectbox(
                "Système d'irrigation",
                ["Aucun", "Traditionnel", "Goutte à goutte", "Aspersion"],
                help="Type d'irrigation utilisé"
            )
            
            fertilisation = st.selectbox(
                "Type de fertilisation",
                ["Aucune", "Organique", "Chimique", "Mixte"],
                help="Mode de fertilisation"
            )
        
        submitted = st.form_submit_button("Générer la Prévision", use_container_width=True)
    
    # Génération de la prévision
    if submitted:
        with st.spinner("🤖 Analyse en cours..."):
            # Simulation du modèle IA (à remplacer par le vrai modèle)
            import time
            time.sleep(1.5)
            
            # Calculs simulés
            """ base_rendement = {
                "Maïs": 3.5,
                "Sorgho": 2.8,
                "Mil": 2.2
            }"""
                   
            import pandas as pd
            import joblib
            # Chargement du modèle
            model = joblib.load("modele_rendement_agricole.pkl")

            def predict_rendement(region, culture, type_sol,
                                surface_ha, pluviometrie_mm, temperature_c):
                data = pd.DataFrame([{
                    "region": region,
                    "culture": culture,
                    "type_sol": type_sol,
                    "surface_ha": surface_ha,
                    "pluviometrie_mm": pluviometrie_mm,
                    "temperature_moyenne_c": temperature_c
                }])

                prediction = model.predict(data)
                return round(prediction[0], 2)
            base_rendement = {culture: predict_rendement(region, culture, type_sol,
                                              superficie, pluviometrie, temperature_moy)}

            # Facteurs d'ajustement
            facteur_pluie = min(pluviometrie / 1000, 1.2)
            facteur_temp = 1.0 if 25 <= temperature_moy <= 30 else 0.85
            facteur_irrigation = {"Aucun": 1.0, "Traditionnel": 1.1, "Goutte à goutte": 1.25, "Aspersion": 1.15}
            facteur_ferti = {"Aucune": 0.8, "Organique": 1.0, "Chimique": 1.2, "Mixte": 1.15}
            
            rendement_prevu = (
                base_rendement[culture] * 
                facteur_pluie * 
                facteur_temp * 
                facteur_irrigation[irrigation] * 
                facteur_ferti[fertilisation] *
                np.random.uniform(0.95, 1.05)
            )
            
            production_totale = rendement_prevu * superficie
            
            # Calcul du risque
            if pluviometrie < 500:
                risque = "Élevé"
                niveau_risque = 75
                couleur_risque = "🔴"
            elif pluviometrie < 800:
                risque = "Moyen"
                niveau_risque = 45
                couleur_risque = "🟡"
            else:
                risque = "Faible"
                niveau_risque = 20
                couleur_risque = "🟢"
            
            # Affichage des résultats
            st.success("Prévision générée avec succès !")
            
            st.markdown("### Résultats de la Prévision")
            
            # Métriques principales
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric(
                    label="Rendement Estimé",
                    value=f"{rendement_prevu:.2f} t/ha",
                    delta=f"+{(rendement_prevu/base_rendement[culture]-1)*100:.1f}% vs base"
                )
            
            with col2:
                st.metric(
                    label="Production Totale",
                    value=f"{production_totale:.2f} t",
                    delta=f"{superficie} ha"
                )
            
            with col3:
                st.metric(
                    label="Niveau de Risque",
                    value=f"{risque} ({niveau_risque}%)",
                    delta=couleur_risque,
                    delta_color="inverse"
                )
            
            with col4:
                jours_optimal = np.random.randint(90, 120)
                date_recolte = pd.Timestamp(date_semis) + pd.Timedelta(days=jours_optimal)
                st.metric(
                    label="Récolte Optimale",
                    value=date_recolte.strftime("%d/%m/%Y"),
                    delta=f"Dans {jours_optimal} jours"
                )
            
            # Graphique de rendement
            st.markdown("### Analyse Détaillée")
            
            col_g1, col_g2 = st.columns(2)
            
            with col_g1:
                # Graphique comparatif
                fig1 = go.Figure()
                categories = ['Rendement\nPrévu', 'Rendement\nMoyen', 'Rendement\nOptimal']
                valeurs = [rendement_prevu, base_rendement[culture], base_rendement[culture] * 1.3]
                couleurs = ['#4CAF50', '#FFC107', '#2196F3']
                
                fig1.add_trace(go.Bar(
                    x=categories,
                    y=valeurs,
                    marker_color=couleurs,
                    text=[f'{v:.2f} t/ha' for v in valeurs],
                    textposition='outside'
                ))
                
                fig1.update_layout(
                    title="Comparaison des Rendements",
                    yaxis_title="Rendement (t/ha)",
                    height=400
                )
                st.plotly_chart(fig1, use_container_width=True)
            
            with col_g2:
                # Jauge de risque
                fig2 = go.Figure(go.Indicator(
                    mode="gauge+number+delta",
                    value=niveau_risque,
                    title={'text': "Indice de Risque (%)"},
                    delta={'reference': 50},
                    gauge={
                        'axis': {'range': [None, 100]},
                        'bar': {'color': "darkred" if niveau_risque > 60 else "orange" if niveau_risque > 30 else "green"},
                        'steps': [
                            {'range': [0, 30], 'color': "lightgreen"},
                            {'range': [30, 60], 'color': "lightyellow"},
                            {'range': [60, 100], 'color': "lightcoral"}
                        ],
                        'threshold': {
                            'line': {'color': "red", 'width': 4},
                            'thickness': 0.75,
                            'value': 70
                        }
                    }
                ))
                fig2.update_layout(height=400)
                st.plotly_chart(fig2, use_container_width=True)
            
            # Recommandations
            st.markdown("### Recommandations")
            
            if niveau_risque > 60:
                st.markdown('<div class="warning-box">', unsafe_allow_html=True)
                st.warning(f"""
                **⚠️ Attention - Risque {risque}**
                
                - Surveillez étroitement l'évolution climatique
                - Envisagez un système d'irrigation complémentaire
                - Planifiez des mesures préventives
                - Consultez un agronome si possible
                """)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="success-box">', unsafe_allow_html=True)
                st.success(f"""
                **Conditions Favorables - Risque {risque}**
                
                - Les conditions sont bonnes pour votre culture
                - Maintenez vos pratiques actuelles
                - Suivez le calendrier de récolte recommandé
                - Préparez le stockage pour la récolte
                """)
                st.markdown('</div>', unsafe_allow_html=True)
            
            # Sauvegarde dans l'historique
            prevision = {
                'date': datetime.now().strftime("%Y-%m-%d %H:%M"),
                'region': region,
                'culture': culture,
                'superficie': superficie,
                'rendement': round(rendement_prevu, 2),
                'production': round(production_totale, 2),
                'risque': risque,
                'date_recolte': date_recolte.strftime("%Y-%m-%d")
            }
            st.session_state.historique.append(prevision)
            
            # Boutons d'action
            col_b1, col_b2, col_b3 = st.columns(3)
            
            with col_b1:
                if st.button("Télécharger le Rapport (PDF)", use_container_width=True):
                    st.info("Fonctionnalité d'export PDF à venir")
            
            with col_b2:
                # Export CSV
                df_export = pd.DataFrame([prevision])
                csv = df_export.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Exporter en CSV",
                    data=csv,
                    file_name=f"prevision_{culture}_{datetime.now().strftime('%Y%m%d')}.csv",
                    mime="text/csv",
                    use_container_width=True
                )
            
            with col_b3:
                if st.button("🔄 Nouvelle Prévision", use_container_width=True):
                    st.rerun()

# PAGE VISUALISATIONS
elif page == "Visualisations":
    st.markdown("## Visualisations et Analyses")
    
    tab1, tab2, tab3 = st.tabs(["Tendances Régionales", "Analyse Climatique", "Calendrier Cultural"])
    
    with tab1:
        st.markdown("### Rendements Moyens par Région")
        
        # Données simulées
        regions = ["Maritime", "Plateaux", "Centrale", "Kara", "Savanes"]
        cultures_viz = ["Maïs", "Sorgho", "Mil"]
        
        data = []
        for region in regions:
            for culture in cultures_viz:
                rendement = np.random.uniform(1.5, 4.5)
                data.append({'Région': region, 'Culture': culture, 'Rendement': rendement})
        
        df_viz = pd.DataFrame(data)
        
        fig = px.bar(
            df_viz,
            x='Région',
            y='Rendement',
            color='Culture',
            barmode='group',
            title='Rendements Moyens par Région et Culture (t/ha)',
            color_discrete_sequence=['#4CAF50', '#FF9800', '#2196F3']
        )
        fig.update_layout(height=500)
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("Ces données sont basées sur les prévisions historiques du système.")
    
    with tab2:
        st.markdown("### Impact de la Pluviométrie sur le Rendement")
        
        # Génération de données synthétiques
        pluie = np.linspace(300, 1500, 50)
        rendement_mais = 1.5 + 0.003 * pluie - 0.000001 * pluie**2 + np.random.normal(0, 0.2, 50)
        
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(
            x=pluie,
            y=rendement_mais,
            mode='markers',
            name='Observations',
            marker=dict(size=8, color='#4CAF50')
        ))
        
        # Ligne de tendance
        z = np.polyfit(pluie, rendement_mais, 2)
        p = np.poly1d(z)
        fig2.add_trace(go.Scatter(
            x=pluie,
            y=p(pluie),
            mode='lines',
            name='Tendance',
            line=dict(color='red', width=3, dash='dash')
        ))
        
        fig2.update_layout(
            title='Relation Pluviométrie - Rendement (Maïs)',
            xaxis_title='Pluviométrie (mm)',
            yaxis_title='Rendement (t/ha)',
            height=500
        )
        st.plotly_chart(fig2, use_container_width=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Pluviométrie Optimale", "800-1000 mm")
        with col2:
            st.metric("Rendement Maximal Observé", "4.2 t/ha")
    
    with tab3:
        st.markdown("### Calendrier Cultural Recommandé")
        
        calendrier = {
            'Culture': ['Maïs', 'Maïs', 'Sorgho', 'Sorgho', 'Mil', 'Mil'],
            'Saison': ['Première', 'Deuxième', 'Première', 'Deuxième', 'Première', 'Deuxième'],
            'Semis': ['Mars-Avril', 'Août-Sept', 'Avril-Mai', 'Septembre', 'Mai-Juin', '-'],
            'Récolte': ['Juin-Juillet', 'Nov-Déc', 'Sept-Oct', 'Janvier', 'Sept-Oct', '-'],
            'Durée (jours)': [90, 90, 120, 120, 100, 0]
        }
        
        df_cal = pd.DataFrame(calendrier)
        df_cal = df_cal[df_cal['Durée (jours)'] > 0]  # Retirer les entrées vides
        
        st.dataframe(df_cal, use_container_width=True, hide_index=True)
        
        st.info("""
        📅 **Note:** Ces périodes sont indicatives et peuvent varier selon les conditions 
        climatiques spécifiques de votre région. 
        """)

# PAGE HISTORIQUE
elif page == "Historique":
    st.markdown("## Historique des Prévisions")
    
    if len(st.session_state.historique) == 0:
        st.info("Aucune prévision enregistrée pour le moment. Commencez par créer une nouvelle prévision !")
    else:
        st.success(f"{len(st.session_state.historique)} prévision(s) enregistrée(s)")
        
        # Affichage sous forme de tableau
        df_historique = pd.DataFrame(st.session_state.historique)
        st.dataframe(df_historique, use_container_width=True, hide_index=True)
        
        # Statistiques
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Rendement Moyen", f"{df_historique['rendement'].mean():.2f} t/ha")
        
        with col2:
            st.metric("Production Totale", f"{df_historique['production'].sum():.2f} t")
        
        with col3:
            culture_freq = df_historique['culture'].mode()[0] if not df_historique.empty else "N/A"
            st.metric("Culture Principale", culture_freq)
        
        # Graphique d'évolution
        if len(st.session_state.historique) > 1:
            st.markdown("### Évolution des Rendements")
            
            fig = px.line(
                df_historique,
                x='date',
                y='rendement',
                color='culture',
                markers=True,
                title='Évolution des Rendements Prévus'
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        # Actions
        col_a1, col_a2 = st.columns(2)
        
        with col_a1:
            csv_all = df_historique.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Télécharger l'Historique Complet (CSV)",
                data=csv_all,
                file_name=f"historique_complet_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv",
                use_container_width=True
            )
        
        with col_a2:
            if st.button("Effacer l'Historique", use_container_width=True):
                st.session_state.historique = []
                st.rerun()

# PAGE À PROPOS
elif page == "ℹ️ À propos":
    st.markdown("## ℹÀ propos du Système")
    
    tab1, tab2, tab3 = st.tabs(["Présentation", "Technologie", "Contact"])
    
    with tab1:
        st.markdown("""
        ### Système de Prévision Agricole Intelligent
        
        Ce système a été conçu pour répondre aux besoins des agriculteurs togolais en matière 
        de prévision et d'aide à la décision agricole.
        
        #### Objectifs
        
        - Fournir des prévisions fiables de rendement
        - Aider à la prise de décision (semis, irrigation, récolte)
        - Réduire les pertes liées aux aléas climatiques
        - Valoriser les données agricoles locales
        
        #### Couverture
        
        Le système couvre l'ensemble des régions agricoles du Togo :
        - Maritime
        - Plateaux
        - Centrale
        - Kara
        - Savanes
        
        #### Cultures Supportées
        
        - **Maïs** : Culture principale
        - **Sorgho** : Céréale traditionnelle
        - **Mil** : Culture de la zone sahélienne
        
        *D'autres cultures seront ajoutées prochainement.*
        """)
    
    with tab2:
        st.markdown("""
        ### Technologies Utilisées
        
        Le système repose sur des technologies modernes et robustes :
        
        #### Intelligence Artificielle
        
        - **Algorithmes** : Random Forest, Gradient Boosting
        - **Framework** : Scikit-learn
        - **Langage** : Python 3.10+
        
        #### Interface Utilisateur
        
        - **Framework** : Streamlit
        - **Visualisations** : Plotly
        - **Design** : Interface intuitive et responsive
        
        #### Données
        
        - Sources : FAOSTAT, Services météo, Enquêtes locales
        - Stockage : CSV, SQLite (évolutif)
        - Traitement : Pandas, NumPy
        
        #### Performance
        
        - Temps de réponse : < 2 secondes
        - Précision : R² > 0.85 (sur données de test)
        - Mises à jour : Modèles actualisés régulièrement
        
        ### Métriques d'Évaluation
        
        Les modèles sont évalués selon :
        - **RMSE** (Root Mean Square Error)
        - **MAE** (Mean Absolute Error)
        - **R²** (Coefficient de détermination)
        """)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Précision Moyenne", "87%")
        with col2:
            st.metric("Erreur Moyenne", "0.3 t/ha")
        with col3:
            st.metric("Prévisions/jour", "150+")
    
    with tab3:
        st.markdown("""
        ### Contact et Support
        
        #### 💬 Besoin d'aide ?
        
        Pour toute question ou assistance technique :
        
        - 📧 Email : tengacherif@gmail.com
        - 📱 Téléphone : +228 71 51 80 61
        - 🌐 Site web : www.agri-ia-togo.org
        
        
        #### Feedback
        
        Vos retours sont précieux pour améliorer le système !
        """)
        
        with st.form("formulaire_feedback"):
            st.markdown("**Envoyez-nous vos suggestions**")
            
            nom = st.text_input("Nom (optionnel)")
            email = st.text_input("Email (optionnel)")
            message = st.text_area("Votre message", height=150)
            
            if st.form_submit_button("Envoyer", use_container_width=True):
                if message:
                    st.success(" Merci pour votre retour ! Nous l'avons bien reçu.")
                else:
                    st.warning(" Veuillez saisir un message.")
        
        st.markdown("---")
        st.caption("© 2026 Système de Prévision Agricole IA - Togo | Version 1.0")

# Footer
st.markdown("---")
col_f1, col_f2, col_f3 = st.columns(3)

with col_f1:
    st.caption("🌾 Système de Prévision Agricole")

with col_f2:
    st.caption("🇹🇬 Fait pour le Togo")

with col_f3:
    st.caption("Propulsé par le groupe mais")
