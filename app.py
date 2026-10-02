from datetime import datetime

import streamlit as st

from config import APP_NAME, APP_VERSION
from database.db import init_db
from database.models import User
from services.corrective_action_service import create_overdue_alerts
from services.training_service import create_expiry_alerts
from utils.ui_components import configure_page, login_view, logout, require_auth

configure_page("Inicio")
init_db()

if not st.session_state.get("authenticated"):
    login_view()
    st.stop()

session, user = require_auth("VIEW")
try:
    create_overdue_alerts(session, user)
    create_expiry_alerts(session, user)
    session.commit()
    with st.sidebar:
        st.markdown(f"**{user.username}**")
        st.caption(user.role)
        if st.button("Cerrar sesión"):
            logout(session, user)
            st.rerun()
    st.title(APP_NAME)
    st.caption(f"Versión {APP_VERSION} · {datetime.utcnow():%Y-%m-%d %H:%M} UTC")
    st.success("Sesión autenticada. Use el menú lateral para los módulos.")
    st.markdown(
        """
        - El sistema no certifica ISO 9001 ni declara conformidad automática.
        - La IA local no se ejecuta con datos insuficientes.
        - Los documentos históricos nunca se sobrescriben.
        """
    )
finally:
    session.close()
