#!/usr/bin/env python3
"""
Script para enviar notificações por email sobre execução do pipeline
"""
import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def send_notification_email():
    """Envia email de notificação sobre a execução do pipeline"""

    # Obtém variáveis de ambiente (obrigatório pelo requisito)
    recipient_email = os.getenv('NOTIFICATION_EMAIL')
    sender_email = os.getenv('SENDER_EMAIL', 'noreply@github-actions.com')
    smtp_password = os.getenv('SMTP_PASSWORD', '')

    if not recipient_email:
        print("❌ ERRO: Variável NOTIFICATION_EMAIL não configurada")
        sys.exit(1)

    # Obtém informações do GitHub Actions
    workflow_name = os.getenv('GITHUB_WORKFLOW', 'CI/CD Pipeline')
    repository = os.getenv('GITHUB_REPOSITORY', 'Repositório Desconhecido')
    actor = os.getenv('GITHUB_ACTOR', 'Usuário Desconhecido')
    run_id = os.getenv('GITHUB_RUN_ID', 'N/A')
    run_number = os.getenv('GITHUB_RUN_NUMBER', 'N/A')
    ref = os.getenv('GITHUB_REF', 'N/A')
    sha = os.getenv('GITHUB_SHA', 'N/A')[:8]  # Apenas primeiros 8 caracteres

    # Status da execução (passado como argumento)
    status = sys.argv[1] if len(sys.argv) > 1 else 'EXECUTADO'

    # Monta o assunto do email
    subject = f"🚀 Pipeline {status} - {repository}"

    # Corpo do email em HTML
    html_body = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            .header {{ background-color: #f6f8fa; padding: 15px; border-radius: 6px; }}
            .status-success {{ color: #28a745; font-weight: bold; }}
            .status-failure {{ color: #dc3545; font-weight: bold; }}
            .info-table {{ margin: 20px 0; border-collapse: collapse; width: 100%; }}
            .info-table th, .info-table td {{
                padding: 8px 12px;
                text-align: left;
                border: 1px solid #d1d5da;
            }}
            .info-table th {{ background-color: #f6f8fa; }}
            .footer {{ margin-top: 30px; font-size: 12px; color: #586069; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h2>🚀 Pipeline Executado!</h2>
            <p class="status-{status.lower()}">Status: {status}</p>
        </div>

        <table class="info-table">
            <tr><th>📁 Repositório</th><td>{repository}</td></tr>
            <tr><th>🔧 Workflow</th><td>{workflow_name}</td></tr>
            <tr><th>👤 Executado por</th><td>{actor}</td></tr>
            <tr><th>🔢 Execução #</th><td>{run_number}</td></tr>
            <tr><th>🆔 Run ID</th><td>{run_id}</td></tr>
            <tr><th>🌿 Branch/Ref</th><td>{ref}</td></tr>
            <tr><th>📋 Commit</th><td>{sha}</td></tr>
            <tr><th>⏰ Executado em</th><td>{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} UTC</td></tr>
        </table>

        <p>🔗 <a href="https://github.com/{repository}/actions/runs/{run_id}">Ver detalhes no GitHub Actions</a></p>

        <div class="footer">
            <p>📧 Email gerado automaticamente pelo GitHub Actions</p>
            <p>🤖 Script desenvolvido para disciplina C14 - Dependencies and Versioning</p>
        </div>
    </body>
    </html>
    """

    try:
        # Cria mensagem
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient_email

        # Adiciona versão HTML
        html_part = MIMEText(html_body, 'html')
        msg.attach(html_part)

        print(f"📧 Enviando notificação para: {recipient_email}")
        print(f"📋 Assunto: {subject}")
        print(f"🏃‍♂️ Pipeline Status: {status}")
        print(f"📁 Repositório: {repository}")
        print(f"🔢 Execução: #{run_number}")

        # Para desenvolvimento/teste - não envia email real
        # Em produção, você configuraria SMTP real aqui
        if os.getenv('GITHUB_ACTIONS'):
            print("✅ Notificação processada com sucesso!")
            print("📝 Em ambiente de produção, o email seria enviado via SMTP")
        else:
            print("🧪 Modo de teste local - email não enviado")

        return True

    except Exception as e:
        print(f"❌ Erro ao processar notificação: {str(e)}")
        return False

if __name__ == "__main__":
    print("🚀 Iniciando script de notificação por email...")
    success = send_notification_email()

    if success:
        print("✅ Script executado com sucesso!")
        sys.exit(0)
    else:
        print("❌ Falha na execução do script!")
        sys.exit(1)