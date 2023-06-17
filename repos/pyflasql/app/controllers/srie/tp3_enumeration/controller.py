# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Implements the logic for TP3 - Enumeration
"""
from flask import Flask, render_template, url_for, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from ....models.sql import db, UserDB
from ...utils import get_shell_output
from ....models.srie.tp3_enumeration.forms import BannerForm, OSForm, LDAPForm
import os


@login_required
def srie_tp3_enumeration():
    """
        Logic for /srie/tp3_enumeration/home
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp3_enumeration/home.html
        """
    username = current_user.username
    return render_template(url_for('blueprint.srie_tp3_enumeration')+'.html', username=username)



@login_required
def srie_tp3_banner_grabbing():
    content = {
        "form" : BannerForm(),
        "command_executed": "Waiting...",
        "command_output": "Waiting...", 
    }

    if content["form"].validate_on_submit():
        ip = content["form"].ip.data
        content["command_executed"] = f"nmap -sV -script=banner {ip}"
        content["command_output"] = get_shell_output(content["command_executed"])
    return render_template(url_for('blueprint.srie_tp3_banner_grabbing')+'.html', content=content)

@login_required
def srie_tp3_os_reco():
    content = {
        "form" : OSForm(),
        "command_executed": "Waiting...",
        "command_output": "Waiting...", 
    }

    if content["form"].validate_on_submit():
        ip = content["form"].ip.data
        password = content["form"].password.data
        os.system(f'echo "{password}"')
        content["command_executed"] = f'sudo -S nmap -O {ip}'
        content["command_output"] = get_shell_output(content["command_executed"])
    return render_template(url_for('blueprint.srie_tp3_os_reco')+'.html', content=content)

@login_required
def srie_tp3_ldap():
    content = {
        "form" : LDAPForm(),
        "command_executed": "Waiting...",
        "command_output": "Waiting...", 
    }

    if content["form"].validate_on_submit():
        ip = content["form"].ip.data
        content["command_executed"] = f'nmap -n -sV --script "ldap* and not brute" {ip}'
        content["command_output"] = get_shell_output(content["command_executed"])
    return render_template(url_for('blueprint.srie_tp3_ldap')+'.html', content=content)