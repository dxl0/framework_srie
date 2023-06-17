# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Implements the logic for TP4 - Gaining Access
"""
from flask import Flask, render_template, url_for, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from ....models.sql import db, UserDB
from ...utils import get_shell_output
from ....models.srie.tp4_gaining_access.forms import HydraForm



@login_required
def srie_tp4_gaining_access():
    """
        Logic for /srie/tp4_gaining_access/home
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp4_gaining_access/home.html
        """
    username = current_user.username
    return render_template(url_for('blueprint.srie_tp4_gaining_access')+'.html', username=username)


@login_required
def srie_tp4_hydra():
    content = {
        "form" : HydraForm(),
        "command_executed": "Waiting...",
        "command_output": "Waiting...", 
    }

    if content["form"].validate_on_submit():
        ip = content["form"].ip.data
        usernames = content["form"].usernames.data
        passwords = content["form"].passwords.data
        content["command_executed"] = f""
        content["command_output"] = get_shell_output(content["command_executed"])
    return render_template(url_for('blueprint.srie_tp4_hydra')+'.html', content = content)

@login_required
def srie_tp4_VSFTPD():
    return render_template(url_for('blueprint.srie_tp4_VSFTPD')+'.html')

@login_required
def srie_tp4_metasploit():
    return render_template(url_for('blueprint.srie_tp4_metasploit')+'.html')